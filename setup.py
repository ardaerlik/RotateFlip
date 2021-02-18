import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RotateFlip",
    version="0.0.1",
    author="Arda Erlik",
    author_email="arda.erlik@gmail.com",
    description="A small image editing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ardaerlik/RotateFlip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
