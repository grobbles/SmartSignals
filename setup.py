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
    description="The SmartSignal lib is an event driven system similar to QT.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grobbles/SmartSignals",
    packages=["smart_signals"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Communications",
        "Topic :: Utilities"
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords=["signals", "events", "slot", "qt"],
    install_requires=requirements
)
