import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

projectName = 'wasteDetection'

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{projectName}/__init__.py",
    f"{projectName}/components/__init__.py",
    f"{projectName}/components/data_ingestion.py",
    f"{projectName}/components/data_validation.py",
    f"{projectName}/components/model_trainner.py",
    f"{projectName}/constant/__init__.py",
    f"{projectName}/constant/training_pipeline/__init__.py",
    f"{projectName}/constant/_application.py",
    f"{projectName}/constant/entity/config_entity.py",
    f"{projectName}/constant/entity/artifact_entity.py",
    f"{projectName}/exception/__init__.py",
    f"{projectName}/logger/__init__.py",
    f"{projectName}/pipline/__init__.py",
    f"{projectName}/pipline/training.py",
    f"{projectName}/utils/__init__.py",
    f"{projectName}/utils/main_utils.py",
    "research/trial.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirement.txt",
    "setup.py",
    "test.py"
]
for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory:{filedir} for the name: {filename}')

    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f'Creating empty file: {filename}')
    else:
        logging.info(f'{filename} is already created')            