import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

project_name = "InstaAgent"

def create_project_structure(project_name: str = "InstaAgent"):
    list_of_files = [
        f"{project_name}/main.py",
        f"{project_name}/requirements.txt",
        f"{project_name}/.env",
        f"{project_name}/vercel.json",
        
        f"{project_name}/services/__init__.py",
        f"{project_name}/services/gpt_service.py",
        f"{project_name}/services/meta_service.py",
        f"{project_name}/services/lead_service.py",
        f"{project_name}/services/notify_service.py",

        f"{project_name}/utils/__init__.py",
        f"{project_name}/utils/intent_scorer.py",
        f"{project_name}/utils/message_parser.py",

        f"{project_name}/tests/__init__.py",
        f"{project_name}/tests/test_main.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/exception/__init__.py",

        "README.md",
        "Dockerfile",
        ".dockerignore",
        "setup.py"
    ]

    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Directory created or already exists: {filedir}")

        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                f.write(f"# {filename}\n")
            logging.info(f"Created new file: {filepath}")
        else:
            logging.info(f"File already exists and is not empty: {filepath}")

def main():
    create_project_structure(project_name=project_name)

if __name__ == "__main__":
    main()
