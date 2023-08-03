from setuptools import setup, find_packages

with open("requirements/requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="app",
    version="0.1.0",
    description="My Flask app starter",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.9",
)