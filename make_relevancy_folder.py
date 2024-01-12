from detect import relevant_files 
import subprocess 
import os
from pathlib import Path

def make_relevancy_folder(folder1: str, folder2: str, batch_size: int = 100) -> None:
    results = sorted(os.listdir(folder1))
    s_results = [f"{folder1}\{r}" for r in results]
    if Path(folder2).exists():
        print(f"Selected output folder {folder2} already exists. Aborting...")
        return
    os.system(f"mkdir \"{folder2}\"")
    print("Relevancy folder created")
    num_rel_files = 0
    for i in range(0, len(s_results), batch_size):
        j = min(i + batch_size, len(s_results))
        print(f"Next file: {s_results[i]}")
        rel_files = relevant_files(s_results[i:j])
        num_rel_files += len(rel_files)
        for rel_file in rel_files: 
            p = Path(rel_file.file)
            fname = p.name
            sub_str = ""
            if rel_file.sub_group is not None: 
                sub_group_p = p.parent / rel_file.sub_group 
                if not sub_group_p.exists():
                    sub_group_p.mkdir()
                sub_str = f"\{sub_group_p}"
                    
            os.system(f"copy \"{folder1}\{fname}\" \"{folder2}{sub_str}\{fname}\"")
        print(f"{100 * j / len(s_results)}% Complete [{j} out of {len(s_results)}]")
    print(f"Sorted out {100 * (1 - num_rel_files / len(s_results))}% of the {len(s_results)} files. New files can be found in \"{folder2}\"")

