import os

# Define the folder structure
folder_structure = {
    ".vscode": ["settings.json"],
    ".github/workflows": ["unittests.yml"],
    "data/raw": [],
    "data/processed": [],
    "notebooks": ["__init__.py", "README.md"],
    "src": [
        "__init__.py",
        "database/__init__.py",
        "database/fetch_data.py",
        "preprocessing/__init__.py",
        "preprocessing/clean_data.py",
        "analysis/__init__.py",
        "analysis/eda.py",
        "visualization/__init__.py",
        "visualization/dashboard.py",
        "modeling/__init__.py",
        "modeling/pca.py",
        "utils/__init__.py",
        "utils/utils.py",
    ],
    "tests": [
        "__init__.py",
        "test_fetch_data.py",
        "test_clean_data.py",
        "test_analysis.py",
    ],
    "scripts": [
        "__init__.py",
        "fetch_data.py",
        "run_eda.py",
        "generate_dashboard.py",
    ],
}

# Additional files in the root
root_files = ["Dockerfile", "requirements.txt", "README.md", ".gitignore", "LICENSE"]

# Create the folder structure
def create_project_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, "w") as f:
                pass  # Create empty files

# Specify the project root folder
project_root = "telecom-user-analysis"

# Create the folder structure
os.makedirs(project_root, exist_ok=True)
create_project_structure(project_root, folder_structure)

# Create root-level files
for file in root_files:
    open(os.path.join(project_root, file), "w").close()

print(f"Project structure for '{project_root}' created successfully!")
