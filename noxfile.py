import os

import nox

PROJECT_DIR = os.path.dirname(__file__)
THEHIVE4PY_DIR = os.path.join(PROJECT_DIR, "thehive4py/")
TESTS_DIR = os.path.join(PROJECT_DIR, "tests/")
EXAMPLES_DIR = os.path.join(PROJECT_DIR, "examples/")

nox.options.default_venv_backend = "none"
nox.options.tags = ["audit", "lint"]


@nox.session(tags=["ci", "lint"])
def style(session: nox.Session):
    """Run style checks with ruff."""
    session.run("ruff", "check", THEHIVE4PY_DIR, TESTS_DIR, EXAMPLES_DIR, __file__)


@nox.session(tags=["ci", "lint"])
def format(session: nox.Session):
    """Run format checks with ruff."""
    session.run(
        "ruff", "format", "--check", THEHIVE4PY_DIR, TESTS_DIR, EXAMPLES_DIR, __file__
    )


@nox.session(tags=["ci", "lint"])
def type(session: nox.Session):
    """Run type checks with mypy."""
    session.run("mypy", "--install-types", "--non-interactive", THEHIVE4PY_DIR)


@nox.session(tags=["ci", "audit"])
def cve(session: nox.Session):
    """Run cve checks with pip-audit."""
    session.run("pip-audit", PROJECT_DIR)


@nox.session(tags=["ci", "audit"])
def security(session: nox.Session):
    """Run security checks with bandit."""
    session.run("bandit", "-r", THEHIVE4PY_DIR)


@nox.session(tags=["ci", "test"])
def test(session: nox.Session):
    """Run integration tests with pytest."""

    if not session.posargs:
        session.run("pytest", "-v", "--cov")
    else:
        session.run("pytest", *session.posargs)


@nox.session(tags=["cd", "build"])
def build(session: nox.Session):
    """Build with the build module."""
    session.run("rm", "-rf", "build/", "dist/")
    session.run("python", "-m", "build", "--sdist", "--wheel")


@nox.session(tags=["cd", "upload"])
def upload(session: nox.Session):
    """Upload to PyPI using twine."""

    session.run(
        "bash",
        "-c",
        r"""
        TAG=${GITHUB_REF#refs/*/}
        VERSION=$(grep -Po '(?<=version = ")[^"]*' pyproject.toml)
        if [ "$TAG" != "$VERSION" ]; then
          echo "Tag value and package version are different: ${TAG} != ${VERSION}"
          exit 1
        else
          echo "Matching tag value and package version!"
        fi
        """,
    )
    session.run("twine", "upload", "dist/*")


@nox.session(tags=["cd", "docs"], name="build-docs")
def build_docs(session: nox.Session):
    """Build docs locally."""
    session.run("mkdocs", "build", "--clean", "--strict")


@nox.session(tags=["cd", "docs"], name="deploy-docs")
def deploy_docs(session: nox.Session):
    """Deploy docs to gh-pages."""
    session.run(
        "mike",
        "deploy",
        "main",
        "latest",
        "--update-aliases",
        "--push",
        "--allow-empty",
    )


@nox.session(tags=["utils", "docs"], name="serve-docs")
def serve_docs(session: nox.Session):
    """Serve docs locally."""
    session.run("mkdocs", "serve", "--clean", "--strict")


@nox.session(tags=["utils", "docs"], name="linkify-release-notes")
def linkify_release_notes(session: nox.Session):
    """Linkify plain github release notes for the docs."""
    session.run("./scripts/linkify_release_notes.py")


@nox.session(tags=["cd", "docs"], name="check-release-notes")
def check_release_notes(session: nox.Session):
    """Check release notes for deployment."""
    session.run("./scripts/linkify_release_notes.py", "--check")
    session.run(
        "bash",
        "-c",
        r"""
        VERSION=$(grep -Po '(?<=version = ")[^"]*' pyproject.toml)
        if ! grep -qF "## $VERSION " "docs/release-notes.md"; then
          echo "No release notes found for version '$VERSION'"
          exit 1
        else
          echo "Release notes found for version '$VERSION'"
        fi
        """,
    )
