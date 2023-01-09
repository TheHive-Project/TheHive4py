<div>
  <p align="center">
    <img src="https://thehive-project.org/img/logo.png" width="700"/>  
  </p>
</div>
<div>
  <p align="center">
    <a href="https://chat.thehive-project.org" target"_blank">
      <img src="https://img.shields.io/discord/779945042039144498" alt="Discord">
    </a>
    <a href="./LICENSE" target"_blank">
      <img src="https://img.shields.io/github/license/TheHive-Project/TheHive4py" alt="License">
    </a>
    <a href="https://pypi.org/project/thehive4py" target"_blank">
      <img src="https://img.shields.io/pypi/dm/thehive4py" alt="Pypi page">
    </a>
    <a href="https://github.com/TheHive-Project/TheHive4py/actions/workflows/ci.yml" target"_blank">
      <img src="https://github.com/TheHive-Project/TheHive4py/actions/workflows/ci.yml/badge.svg" alt="ci action badge">
    </a>
  </p>
</div>


# thehive4py

    IMPORTANT: The library is still under development and is in beta phase. Use it with caution and expect breaking changes before the first stable release!

Rebooted version of thehive4py for TheHive5! Stay tuned, more to come!

## Development


### Setting up a virtual environment (optional)

You can setup a venv (see the [official docs for this](https://docs.python.org/3/tutorial/venv.html):

```
# Create and activate venv
python3 -m venv <path_of_venv>
source <path_of_venv>/bin/activate
```

### Install the package for development 

To install the package with the dev dependencies one can run:

```
pip install -e '.[dev]'
```

### Run CI checks before pushing changes

To check the integrity of changes made one can run:

```
python scripts/ci.py 
```

or to execute the checks automatically just install the pre-commit hooks come with the repo:

```
pre-commit install
```

### Run CD commands to build and publish

To build the package one can run:

```
python scripts/cd.py build
```