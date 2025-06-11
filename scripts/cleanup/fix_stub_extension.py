import os

folder_path = 'PATH'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, file[:-3] + '.pyi')
            os.rename(old_path, new_path)
