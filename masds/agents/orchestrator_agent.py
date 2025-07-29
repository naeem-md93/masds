import os
import subprocess
from tqdm import tqdm

from .. import constants as C, utils
from .implementer_agent import implement_a_task
from .validator_agent import validate_an_implementation
from .index_agent import index_a_project
from .readme_agent import update_README


def init_a_branch(branch_name: str) -> None:
    subprocess.call(["git", "checkout", "-b", branch_name])


def restore_a_branch() -> None:
    subprocess.call(["git", "checkout", "-f"])


def commit_and_merge_a_branch(branch_name, commit_msg: str) -> None:
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", f"{commit_msg}"])
    subprocess.call(["git", "checkout", "main"])
    subprocess.call(["git", "merge", branch_name])


def init_a_git_repo():
    subprocess.call(["git", "init"])
    subprocess.call(["git", "config", "--global", "init.defaultBranch", "main"])
    subprocess.call(["git", "checkout", "-b", "main"])
    subprocess.call(["touch", "mmd.txt"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", '"initital commit"'])
    subprocess.call(["rm", "mmd.txt"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", '"initial commit"'])


def orchestrate_a_project(prd, db, tasks):
    init_a_git_repo()

    t = tqdm(enumerate(tasks))
    for idx, t_data in t:
        t.set_description_str(f"({idx + 1}/{len(tasks)}) - {t_data['title']}")

        init_a_branch(t_data["branch_name"])

        val_msgs = []

        impl = implement_a_task(prd, db, val_msgs, t_data)
        utils.write_json_file(f"./.masds_cache/task_{idx}_try_0_impl.json", impl)

        exec = utils.execute_bash_script(impl["implementation"])
        utils.write_json_file(f"./.masds_cache/task_{idx}_try_0_exec.json", exec)

        val_resp = validate_an_implementation(t_data, impl["implementation"], exec)

        is_finished = val_resp["is_finished"]
        counter = 1
        while not is_finished:
            val_msgs.append(val_resp["implementer_msg"])
            restore_a_branch()
            impl = implement_a_task(prd, db, val_msgs, t_data)
            utils.write_json_file(
                f"./.masds_cache/task_{idx}_try_{counter}_impl.json", impl
            )

            exec = utils.execute_bash_script(impl["implementation"])
            utils.write_json_file(
                f"./.masds_cache/task_{idx}_try_{counter}_exec.json", exec
            )

            val_resp = validate_an_implementation(t_data, impl, exec)
            is_finished = val_resp["is_finished"]
            counter += 1

        readme_md = (
            utils.read_text_file("./README.md") if os.path.exists("./README.md") else ""
        )
        readme_md = update_README(readme_md, t_data, impl["implementation"])
        utils.write_text_file(readme_md, "./README.md")
        commit_and_merge_a_branch(t_data["branch_name"], val_resp["commit_msg"])
        db = index_a_project("./")
        utils.write_json_file("./.masds_cache/db.json", db)
