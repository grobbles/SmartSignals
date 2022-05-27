import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open("requirements.txt", "r") as requirements_file:
    requirements.append(requirements_file.read())

setuptools.setup(
    name="SmartSignals",
    version="0.0.0",
    author="Uwe Roder",
    author_email="uweroder@gmail.com",
    description="A Python library to .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grobbles/SmartSignals",
    packages=["smart_signals"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)",
        "Programming Language :: Python :: 3"
    ],
    keywords="signals event slot",
    install_requires=requirements
)