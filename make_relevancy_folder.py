from detect import relevant_files 
import subprocess 
import os
from pathlib import Path

def make_relevancy_folder(folder1: str, folder2: str) -> None:
    cwd = os.getcwd()
    proc = subprocess.Popen(['ls', folder1], stdout=subprocess.PIPE, cwd=cwd)
    stdout = proc.stdout 
    assert stdout is not None
    results = stdout.read().splitlines()
    s_results = [f"{folder1}/{r.decode()}" for r in results]
    rel_files = relevant_files(s_results)
    if Path(folder2).exists():
        print(f"Selected output folder {folder2} already exists. Aborting...")
        return
    os.system(f"mkdir {folder2}")
    for file in rel_files: 
        p = Path(file)
        fname = p.name
        os.system(f"cp {folder1}/{fname} {folder2}/{fname}")
    print(f"Sorted out {100 * (1 - len(rel_files) / len(s_results))}% of the {len(s_results)} files. New files can be found in \"{folder2}\"")

