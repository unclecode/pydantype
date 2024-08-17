import re
from setuptools import setup, find_packages

# Read the version from __init__.py
def get_version():
    init_py = open('src/pydantic_to_typeddict/__init__.py').read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="pydantic_to_typeddict",
    version=get_version(),
    author="Unclecode",
    author_email="unclecode@kidocode.com",
    description="A library to convert Pydantic models to TypedDict",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unclecode/pydantic_to_typeddict",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
)