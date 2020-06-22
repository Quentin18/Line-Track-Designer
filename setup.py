import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="line-track-designer",
    version="0.0.1",
    author="Quentin Deschamps",
    author_email="quentindeschamps18@gmail.com",
    description="A library to design line following tracks for robots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quentin18/Line-Track-Designer",
    packages=["line_track_designer"],
    include_package_data=True,
    # install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
