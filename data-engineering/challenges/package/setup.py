from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="read_text_from_image_with_python",
    version="0.0.4",
    author="Sabrina B. M.",
    author_email="sabrinabm94@gmail.com",
    description="Package to extract text from images using Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sabrinabm94/python/tree/master/data-engineering/challenges/package",
    packages=find_packages(),
    python_requires=">=3.8",
)
