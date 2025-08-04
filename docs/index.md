<div align="center">
  <a href="https://github.com/TheHive-Project/TheHive4py" target="_blank">
   <img src="https://strangebee.com/wp-content/uploads/2024/07/Icon4Nav_TheHive.png" alt="TheHive Logo">
  </a>
  <b style="display: block; font-size: 2rem">thehive4py</b>
 </p>
  <p align="center">
      <em>the de facto Python API client of <a href="https://strangebee.com/thehive/">TheHive</a></em>
  </p>
  <p align="center">
      <a href="https://github.com/TheHive-Project/TheHive4py/releases" target="_blank">
          <img src="https://img.shields.io/github/v/release/Thehive-project/thehive4py?logo=github&logoColor=FFC72C&labelColor=0049D4" alt="release">
      </a>
      <a href="https://github.com/TheHive-Project/TheHive4py/actions/workflows/main-cicd.yml" target="_blank">
          <img src="https://img.shields.io/github/actions/workflow/status/TheHive-Project/TheHive4py/main-cicd.yml?logo=github&logoColor=FFC72C&labelColor=0049D4" alt="build">
      </a>
      <a href="https://app.codecov.io/github/TheHive-Project/TheHive4py" target="_blank">
          <img src="https://img.shields.io/codecov/c/gh/TheHive-Project/TheHive4py?logo=codecov&logoColor=FFC72C&labelColor=0049D4" alt="codecov">
      </a>
      <a href="https://pypi.org/project/thehive4py" target="_blank">
          <img src="https://img.shields.io/pypi/dm/thehive4py?logo=python&logoColor=FFC72C&labelColor=0049D4" alt="pypi">
      </a>
      <a href="./LICENSE" target="_blank">
          <img src="https://img.shields.io/github/license/TheHive-Project/TheHive4py?logo=unlicense&logoColor=FFC72C&labelColor=0049D4" alt="license">
      </a>
      <a href="https://discord.com/invite/XhxG3vzM44" target="_blank">
          <img src="https://img.shields.io/discord/779945042039144498?logo=discord&logoColor=FFC72C&labelColor=0049D4" alt="discord">
      </a>
  </p>
</div>

---
**Documentation**: <a href="https://thehive-project.github.io/TheHive4py/" target="_blank">https://thehive-project.github.io/TheHive4py/</a>

**Source Code**: <a href="https://github.com/TheHive-Project/TheHive4py" target="_blank">https://github.com/TheHive-Project/TheHive4py</a>

---

# Introduction 

Welcome to `thehive4py`, the Python library designed to simplify interactions with StrangeBee's TheHive. Whether you're a cybersecurity enthusiast or a developer looking to integrate TheHive into your Python projects, this library has got you covered.

Feel free to explore the library's capabilities and contribute to its development. We appreciate your support in making TheHive integration in Python more accessible and efficient.


# Requirements
`thehive4py` works with all currently supported python versions. One can check the official version support and end of life status [here](https://devguide.python.org/versions/).

# Installation
The `thehive4py` can be installed with pip like:

```bash
pip install thehive4py
```


# Quickstart

```python
from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")
```

# Licensing

This project is licensed under the terms of the MIT license.

