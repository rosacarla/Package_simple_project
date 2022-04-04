from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_simple_dio",
    version="0.0.1",
    author="Carla Edila",
    author_email="rosa.carla@pucpr.edu.br",
    description="Example of package creation",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rosacarla/Package_simple_project",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)