import setuptools  # type: ignore

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="viewdns-python",
    version="0.1.0-dev1",
    author="Michael Scribellito",
    author_email="mscribellito@gmail.com",
    description="Python module to interact with ViewDNS.info API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onemoretime/viewdns-python",
    project_urls={
        "Bug Tracker": "https://github.com/onemoretime/viewdns-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "viewdns"},
    packages=setuptools.find_packages(where="viewdns"),
    python_requires=">=3.8",
)