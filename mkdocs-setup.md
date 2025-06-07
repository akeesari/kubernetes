
## Introduction

This documentation is built using markdown language, MkDocs and mkdocs-material.

## Prerequisites

- Visual Studio code
- Create new repo called `mkdocs` in GitHub
- Clone the repo locally

In order to run this project locally your need to install following:

- Python 3.7 or later
- pip (Python package manager)
- Install mkdocs-material

Download and install Python3

```sh
brew install python3

# validate
python3 --version
# or
python --version
```

Download and installing pip

```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# You can check by running:
pip3 --version
# or
pip --version
```

you can find more info here- https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

Install mkdocs-material
 
```sh
pip install mkdocs-material

# Confirm the installation:
mkdocs --version
```

you can find more info here - https://squidfunk.github.io/mkdocs-material/getting-started/
   
## Create a Project Directory

```sh
mkdir my-docs-site
cd my-docs-site
```
Create a New MkDocs Project

```sh
mkdocs new .
```

You need to run following bash script to install required software to run this project locally.

```sh
bash ./init_setup.sh
```

## Running the site locally

Execute the following command to run the site locally with Localhost URL.

```sh
mkdocs serve 
```

output
```
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 1.44 seconds
INFO     -  [19:20:51] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [19:20:51] Serving on http://127.0.0.1:8000/mkdocs/
```

browse the site with following URL:

http://127.0.0.1:8000/mkdocs/


## References
- https://www.youtube.com/watch?v=OOxL-r1L334&t=958s - YouTube video, helped me to create the mkdocs site.
- https://www.markdownguide.org/ - markdown language
- https://squidfunk.github.io/mkdocs-material/ - Material for MkDocs
- https://squidfunk.github.io/mkdocs-material/getting-started/ - getting-started, used for project setup
- https://mermaid-js.github.io/mermaid/#/ - mermaid 
- https://daringfireball.net/projects/markdown/syntax#autolink