import os
import subprocess

from .graph import build_graph


def init_project(project_dir: str):
    os.makedirs("./.masds_cache", exist_ok=True)
    os.makedirs(project_dir, exist_ok=True)
    os.chdir(os.path.join(os.getcwd(), project_dir))
    subprocess.call(["git", "init"])
    subprocess.call(["git", "config", "--global", "init.defaultBranch", "main"])


def build_project(project_dir: str, project_description: str) -> None:
    init_project(project_dir)

    executor = build_graph()

    initial_state = {"description": project_description}

    final_state = executor.invoke(initial_state)

    return final_state
