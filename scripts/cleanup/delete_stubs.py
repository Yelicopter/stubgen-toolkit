import os

SRC_DIR = 'FILL IN SOURCE DIRECTORY HERE'

for root, dirs, files in os.walk(SRC_DIR):
    for file in files:
        if file.endswith('.pyi'):
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f'Removed: {file_path}')
            except Exception as e:
                print(f'Error removing {file_path}: {e}')