import json
import os
from pathlib import Path


def convert_file(filename: Path):
    keep = dict(json.loads(filename.read_bytes()))

    # read file and create md
    md = ""

    # title
    title = keep.get("title")
    md += f"# {title}\n\n"

    # content
    content = keep.get("textContent", "")
    md += content + "\n\n"

    # listContent
    list_contents = keep.get("listContent", [])
    for task in list_contents:
        check = "x" if task["isChecked"] else " "
        md += f"- [{check}] {task['text']}\n"
    md += "\n\n"

    # tags
    tags = keep.get("labels", [])
    md += "\n" + ", ".join([f"#{t['name'].replace(' ', '_')}" for t in tags])

    return md, keep.keys()


def convert_all(folder: str):

    # input and output folder
    inp_folder = Path(folder)
    if not inp_folder.exists():
        return "Folder location is not valid."

    out_folder = Path(folder + "_out")
    out_folder.mkdir(parents=True, exist_ok=True)

    # read directory
    _, _, inp_files = list(os.walk(inp_folder))[0]

    # all_keys: set = set()
    for f in inp_files:
        if not f.endswith(".json"):
            continue
        md, keys = convert_file(inp_folder / f)
        out_file = out_folder / f.replace(".json", ".md")
        with out_file.open("w+", encoding="utf-8") as fs:
            fs.write(md)

    return "convertion done."


convert_all(r"E:\programms\python\KeepSidian\files")
