import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="frmc-glenngaetz",
    version="0.0.1",
    author="Glenn Gaetz",
    author_email="glenngaetz@gmail.com",
    description="Fundraising metrics calculations",
    long_description=long_description,
    url="https://github.com/glenngaetz/frmc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operation System :: OS Independent",
    ],
    python_requires='>=3.6',
)
