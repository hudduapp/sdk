from setuptools import setup, find_packages
import sdk

install_requires = ["bcrypt=3.2.0", "requests=2.27.1"]

# Conditional dependencies:


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="sdk",
    version=sdk.__version__,
    description=sdk.__description__,
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/hudduapp/sdk",
    author=sdk.__author__,
    author_email="some@mail.com",
    license="MIT",
    packages=["sdk", "sdk.utils", "sdk.adapters"],
    python_requires=">=3.7",
    install_requires=install_requires,
    project_urls={
        "GitHub": "https://github.com/hudduapp/sdk",
    },
)
