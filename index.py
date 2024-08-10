import os

# Function to create the package structure
def create_package_structure(package_name):
    if package_name == '.':
        root_dir = os.getcwd()  # Use the current directory
    else:
        root_dir = package_name
        os.makedirs(root_dir, exist_ok=True)

    structure = {
        package_name if package_name != '.' else os.path.basename(root_dir): ['__init__.py', 'installer.py'],
        'tests': ['__init__.py', 'test_installer.py'],
        'root_files': ['setup.py', 'README.md', 'LICENSE', 'requirements.txt']
    }

    for folder, files in structure.items():
        if folder == 'root_files':
            for file in files:
                open(os.path.join(root_dir, file), 'a').close()
        else:
            os.makedirs(os.path.join(root_dir, folder), exist_ok=True)
            for file in files:
                open(os.path.join(root_dir, folder, file), 'a').close()

    print(f"Package structure created under {root_dir}")

# Prompt the user for the package name
package_name = input("Enter the package name (or '.' for the current directory): ")
create_package_structure(package_name)
