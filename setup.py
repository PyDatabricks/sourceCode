from setuptools import (
    setup,
    find_packages
)
import os

_PATH_ROOT = os.path.dirname(__file__)
_PATH_REQUIRES = os.path.join(_PATH_ROOT, "requirements")


def _load_requirements(path_dir: str = _PATH_ROOT, file_name: str = "requirements.txt") -> "list[str]":
    with open(os.path.join(path_dir, file_name)) as fp:
        reqs = [ln.strip() for ln in fp.readlines()]
    return [r for r in reqs if r and not r.startswith("#")]


setup(
    name='databricks',
    version='0.1',
    url='https://github.com/the-gigi/pathology',
    license='None',
    author='Tiago Andrade',
    author_email='twsandrade@gmail.com',
    description='Add static script_dir() method to Path',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    zip_safe=False,
    python_requires=">=3.7",
    install_requires="requirements.txt"
)