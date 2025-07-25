import os
import json


def read_json_file(fp: str) -> dict:
    with open(fp, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def write_json_file(fp: str, data: dict) -> None:
    with open(fp, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def write_text_file(content: str, fp: str) -> None:
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)


def read_project_files(project_dir: str) -> dict[str, dict[str, str]]:
    result = {}

    for p_root, _, p_files in os.walk(project_dir):
        for f in p_files:
            fp = os.path.join(p_root, f)
            result[fp] = {
                "path": fp,
            }

    return result


def read_project_dirs(project_dir: str) -> dict[str, dict]:
    result = {}
    for p_root, p_dirs, p_files in os.walk(project_dir):
        n_dirs = [os.path.join(p_root, d) for d in p_dirs]
        n_files = [os.path.join(p_root, d) for d in p_files]

        result[p_root] = {"path": p_root, "dirs": n_dirs, "files": n_files}

    return result


def remove_markdown_fences(text: str, fence_type: str) -> str:
    return text.replace(f"```{fence_type}", "").replace("```", "")


def convert_str_to_json(text: str) -> dict:
    return json.loads(text)


def convert_response_to_json(response: str) -> dict:
    try:
        response = remove_markdown_fences(response, "json")
        response = convert_str_to_json(response)
    except Exception as e:
        print(f"{response=}")
        print(f"{e=}")
        raise Exception

    return response
