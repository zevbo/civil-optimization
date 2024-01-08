from make_relevancy_folder import make_relevancy_folder 
import sys

if __name__ == "__main__":
    folder1 = sys.argv[1]
    folder2 = sys.argv[2]
    print(f"Making relevancy folder of {folder1} in {folder2}")
    make_relevancy_folder(folder1, folder2)