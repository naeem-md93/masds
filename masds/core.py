import os
import subprocess
from .agents.prd_agent import write_a_prd
from .agents.index_agent import index_a_project
from .agents.decompose_agent import decompose_a_project
from .agents.orchestrator_agent import orchestrate_a_project
from . import utils


def develop_a_project(project_dir: str, project_desc: str) -> None:
    subprocess.call(["mkdir", project_dir])
    os.chdir(project_dir)

    subprocess.call(["mkdir", ".masds_cache"])

    prd = write_a_prd(project_desc)
    utils.write_json_file("./.masds_cache/prd.json", prd)
    # prd = utils.read_json_file("../prd.json")

    db = index_a_project("./")
    utils.write_json_file("./.masds_cache/db.json", db)

    tasks = decompose_a_project(prd=prd["prd"], db=db)
    utils.write_json_file("./.masds_cache/tasks.json", tasks)

    orchestrate_a_project(prd=prd["prd"], db=db, tasks=tasks["tasks"])
