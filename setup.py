from setuptools import find_packages, setup


def parse_version():
    with open("thehive4py/__init__.py") as init_fp:
        for line in init_fp:
            if line.strip().startswith("__version__"):
                return line.split("=")[1].strip().strip('"')
        raise ValueError("Unable to parse version number")


REQUIREMENTS = ["requests==2.26.*"]


EXTRAS_REQUIRE = {"lint": ["flake8", "black", "mypy"], "test": ["pytest"]}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["lint"] + EXTRAS_REQUIRE["test"]


def read(fname):
    """Read the content of the file `fname`."""
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="thehive4py",
    version=parse_version(),
    description="Python client for TheHive5",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Szabolcs Antal",
    author_email="antalszabolcs01@gmail.com",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS_REQUIRE,
    license="AGPL-V3",
    keywords="thehive api rest client",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    python_requires=">=3.8",
)
