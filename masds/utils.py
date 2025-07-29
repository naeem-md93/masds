import os
import json


def read_json_file(fp: str) -> dict:
    with open(fp, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def write_json_file(fp: str, data: dict) -> None:
    with open(fp, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def read_text_file(fp: str) -> str:
    with open(fp, "r", encoding="utf-8") as f:
        return f.read()


def write_text_file(content: str, fp: str) -> None:
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)


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


import subprocess
import tempfile
import os
from typing import List, Tuple, Union


def execute_bash_script(
    script_lines: List[str], timeout: Union[int, float] = 30
) -> Tuple[bool, str, str]:
    """
    Execute a bash script given as a list of lines.

    Args:
        script_lines: The bash script, one line per list element.
        timeout: Maximum execution time in seconds.

    Returns:
        A tuple (success, stdout, stderr):
          - success: True if exit code == 0, False otherwise.
          - stdout: Captured standard output.
          - stderr: Captured standard error or timeout message.
    """
    # Join lines into a single script text
    script_text = "\n".join(script_lines)

    # Create a temporary file to hold the script
    with tempfile.NamedTemporaryFile(mode="w", suffix=".sh", delete=False) as tf:
        tf.write(script_text)
        temp_path = tf.name

    # Make it executable
    os.chmod(temp_path, 0o700)

    try:
        # Run the script
        completed = subprocess.run(
            [temp_path], capture_output=True, text=True, timeout=timeout
        )
        success = completed.returncode == 0
        stdout = completed.stdout
        stderr = completed.stderr

    except subprocess.TimeoutExpired as te:
        success = False
        stdout = (te.stdout or b"").decode("utf-8", errors="replace")
        stderr = f"Script timed out after {timeout} seconds."

    except subprocess.CalledProcessError as cpe:
        success = False
        stdout = (cpe.stdout or b"").decode("utf-8", errors="replace")
        stderr = (cpe.stderr or b"").decode("utf-8", errors="replace")

    finally:
        # Clean up the temp script
        try:
            os.remove(temp_path)
        except OSError:
            pass

    result = {"success": success, "stdout": stdout, "stderr": stderr}
    return result
