import setuptools

with open("README.md", "r") as fh: #open read me
    long_description = fh.read() 

if __name__ == "__main__":
    setuptools.setup(
        name="facial-recognition", # Replace with your own username
        version="0.0.0",
        author="Sid, Olivia, Rebecca, Austin, Ines",
        author_email="",
        description="Identifies faces and saves their names",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/sidhanthholalkere/facial-recognition.git",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: Who Needs a Licence",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )