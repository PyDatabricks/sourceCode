from setuptools import setup, find_packages

setup(
    name="databricks", 
    version="0.11",
    description="Databricks Lib",
    author="DDRE",
    packages=find_packages(),
    install_requires=[
        "requests==2.31.0",
        "multipledispatch==1.0.0"
    ]
)