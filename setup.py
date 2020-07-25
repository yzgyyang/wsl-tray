import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wsl-tray",
    version="0.2",
    author="Guangyuan Yang",
    author_email="yzgyyang@outlook.com",
    description=(
        "wsl-tray is a lightweight Windows tray application "
        "for easily managing WSL 2 VMs."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yzgyyang/wsl-tray",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.7',
)
