import os

def create_structure(base_dir="f1-podium-predictor"):
    folders = [
        "data/raw",
        "data/processed",
        "notebooks",
        "scripts",
        "app",
        "dashboard",
        "models",
        "tests"
    ]

    files = [
        "README.md",
        ".gitignore",
        "requirements.txt"
    ]

    print(f"Creating project in: {os.path.abspath(base_dir)}")

    # Create folders
    for folder in folders:
        path = os.path.join(base_dir, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    # Create empty files
    for file in files:
        path = os.path.join(base_dir, file)
        with open(path, 'w') as f:
            f.write("")  # Create an empty file
        print(f"Created file: {path}")

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_structure()
