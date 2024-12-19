import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'

setup(
    name="easy-ams",
    version=version,
    author="Łukasz Radecki",
    author_email="lukasz.radecki@edu.uekat.pl",
    description="Attendance management system",
    url="https://github.com/Lukas249/SON_Python_Students",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.12",
)
