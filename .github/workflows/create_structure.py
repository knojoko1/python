import os

# List of directories to create corresponding to your README structure
directories = [
    "basics",
    "functions",
    "oop",
    "data_structures",
    "scripts"
]

def create_repository_structure():
    print("Creating repository folder structure...")
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            # Create a .gitkeep file so Git tracks the empty folder
            gitkeep_path = os.path.join(directory, ".gitkeep")
            with open(gitkeep_path, "w") as f:
                f.write("")
            print(f"✅ Created directory: {directory}/")
        else:
            print(f"⚠️ Directory already exists: {directory}/")
            
    print("Folder structure setup complete!")

if __name__ == "__main__":
    create_repository_structure()
