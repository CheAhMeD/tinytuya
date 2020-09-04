import setuptools

from tinytuya import __version__

with open("tinytuya/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tinytuya",
    version=__version__,
    author="Jason Cox",
    author_email="jason@jasonacox.com",
    description="Python module to interface with Tuya WiFi smart devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jasonacox/tinytuya',
    packages=setuptools.find_packages(),
    install_requires=[
        'pyaes',  # NOTE this is optional, AES can be provided via PyCrypto or PyCryptodome
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)