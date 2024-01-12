from pathlib import Path
from make_relevancy_folder import make_relevancy_folder 
import sys

if __name__ == "__main__":
    folder1 = sys.argv[1]
    folder2 = sys.argv[2]
    batch_size = 100 
    if len(sys.argv) > 3:
        batch_size = int(sys.argv[3])
    print(f"Making relevancy folder of {folder1} in {folder2}")
    make_relevancy_folder(Path(folder1), Path(folder2), batch_size=batch_size)