# setup.py

from setuptools import setup, find_packages


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="InstaAgent",
    version="0.1.0",
    author="Aditya AK",
    author_email="aakuskar.980@gmail.com",
    description="An AI-powered Instagram DM Auto-Agent for lead generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Adity-star/InstaAgent",
    packages=find_packages(where="InstaAgent"),
    package_dir={"": "InstaAgent"},
    python_requires=">=3.8",
   
)
