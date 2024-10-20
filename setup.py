from setuptools import setup, find_packages

setup(
    name="PyPrivacyTool",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Pillow",
        "PyPDF2",
        "mutagen",
        # add other dependencies
    ],
    entry_points={
        "console_scripts": [
            "pyprivacytool=pyprivacytool.main:main",
            "metadata_remover=pyprivacytool.metadata_remover:main",
            "secure_delete=pyprivacytool.secure_delete:main",
        ],
    },
    description="A suite of privacy enhancing tools.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/PyPrivacyTool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
