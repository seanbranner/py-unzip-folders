import shutil
import json
from pathlib import Path
import os

json_path = Path('config.json')

with open(json_path, 'r') as f:
    config = json.load(f)

root_path = Path(config['APP']['PATH'])

all_files_in_dir = os.listdir(root_path)

for zip_file in all_files_in_dir:
    zip_file_path = root_path.joinpath(zip_file)
    target_dir_path = Path(str(zip_file_path)[:-4])

    try:
        shutil.unpack_archive(zip_file_path, target_dir_path,"zip")
    except:
        print("Not ZIP")
