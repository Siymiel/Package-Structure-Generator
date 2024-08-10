# Package Structure Generator

This script is designed to dynamically create a basic Python package structure in a specified directory. The structure includes necessary files like `__init__.py`, `installer.py`, `setup.py`, and others typically needed to organize and distribute a Python package.

## Features

- **Custom Package Name**: Specify the name of the package, and the script will create a directory with that name and set up the package structure within it.
- **Current Directory Option**: Use a period (`.`) as the package name to create the package structure within the current directory.

## Package Structure

When you run the script, it generates the following structure:

```bash
<package_name>
├── LICENSE
├── README.md
├── requirements.txt
├── <package_name>
│   ├── __init__.py
│   └── installer.py
├── setup.py
└── tests
    ├── __init__.py
    └── test_installer.py
```
3 directories, 8 files


If you specify `.` as the package name, the structure will be created within the current directory:

```bash
<current_directory>
├── LICENSE
├── README.md
├── requirements.txt
├──< current_directory>
│   ├── __init__.py
│   └── installer.py
├── setup.py
└── tests
    ├── __init__.py
    └── test_installer.py
```


## Usage

1. Run the script in your terminal or IDE.
2. When prompted, enter the desired package name:
   - **Package Name**: The script will create a new directory with this name and populate it with the package structure.
   - **Period (`.`)**: The script will create the package structure within the current directory.

### Example

- **To create a package named `awesome_package`**:

- **To create the package structure in the current directory**:

Enter the package name (or '.' for the current directory): .


## Requirements

- Python 3.x

No external libraries are required to run this script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



