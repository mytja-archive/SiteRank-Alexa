import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alexa-siterank", # Replace with your own username
    version="1.0.2",
    author="mytja",
    description="Get siterank & other data from Alexa Web Information Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mytja/SiteRank-Alexa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'httpx',
    ],
    python_requires='>=3',
)
