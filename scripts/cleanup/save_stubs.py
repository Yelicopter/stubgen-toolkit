import shutil
import os

def copy_folder_structure(src_path, dest_path):
    if not os.path.isdir(src_path):
        print(f"Source path {src_path} is not a directory.")
        return
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    for root, dirs, files in os.walk(src_path):
        rel_path = os.path.relpath(root, src_path)
        dest_dir = os.path.join(dest_path, rel_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)

if __name__ == "__main__":
    src = ""
    dest = ""
    copy_folder_structure(src, dest)