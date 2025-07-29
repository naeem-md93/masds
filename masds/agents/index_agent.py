import pathlib
from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern


HARDCODED_SKIP = [".git", ".masds_cache", "package-lock.json"]


def is_text_file(file_path, block_size=2048):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            f.read(block_size)
        return True
    except Exception:
        return False


def load_gitignore(path: pathlib.PosixPath):
    gitignore_path = path / ".gitignore"

    if not gitignore_path.exists():
        return PathSpec([])

    with gitignore_path.open("r") as f:
        lines = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]

    return PathSpec.from_lines(GitWildMatchPattern, lines)


def index_a_directory(rel, item, spec):
    children = []
    for c in item.iterdir():
        rel_c = (rel / c.name).as_posix()
        if (
            (not spec.match_file(rel_c))
            and (not spec.match_file(rel_c + "/"))
            and (c.name not in HARDCODED_SKIP)
        ):
            children.append(c.name)

    return {"type": "directory", "note": "", "contents": children}


def index_a_file(item):
    if is_text_file(item):
        try:
            with open(item, "r", encoding="utf-") as f:
                content = f.read()
            return {"type": "text-file", "note": "", "contents": content}
        except Exception as e:
            return {
                "type": "file",
                "note": f"Could not read file: {str(e)}",
                "contents": "",
            }
    else:
        return {
            "type": "binary-file",
            "note": "Can not open this file as text.",
            "contents": "",
        }


def run_indexer(
    path: pathlib.PosixPath, base: pathlib.PosixPath, spec: PathSpec, index: dict
) -> None:
    for item in path.iterdir():
        rel = item.relative_to(base)
        rel_str = rel.as_posix()

        if rel.parts[-1] in HARDCODED_SKIP:
            continue

        if spec.match_file(rel_str) or spec.match_file(rel_str + "/"):
            continue

        if item.is_dir():
            index[rel_str] = index_a_directory(rel, item, spec)
            run_indexer(item, base, spec, index)
        else:
            index[rel_str] = index_a_file(item)


def index_a_project(path: str) -> dict:
    root = pathlib.Path(path).resolve()
    spec = load_gitignore(root)
    index = {}
    run_indexer(root, root, spec, index)

    for k, v in index.items():
        print(f"{k=} - {v=}")

    return index


if __name__ == "__main__":
    index_a_project("./multi_agent/")
