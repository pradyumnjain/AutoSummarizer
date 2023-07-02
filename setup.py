import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "AutoSummarizer"
AUTHOR_USER_NAME = "pradyumnjain"
SRC_REPO = "AutoSummarizer"
AUTHOR_EMAIL = "pradyumn25jain@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Efficiently distill lengthy text into concise summaries, enabling quick comprehension and information retrieval",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    # The setuptools.find_packages() function is used to discover and retrieve all Python packages (i.e., directories containing an __init__.py file) within a specified directory or directories.
    packages=setuptools.find_packages(where="src")
)
