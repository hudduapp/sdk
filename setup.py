from setuptools import setup

import sdk

install_requires = [
    "requests~=2.27.1",
    "bcrypt~=3.2.2",
    "uuid~=1.30"
]  # keep this up to date


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name='sdk',
    version=sdk.__version__,
    description=sdk.__description__,

    url='https://github.com/hudduapp/sdk',
    author=sdk.__author__,
    author_email="some@mail.com",
    packages=["sdk", "sdk.utils", "sdk.thirdparty"],
    python_requires=">=3.7",
    install_requires=install_requires,
    project_urls={
        "GitHub": "https://github.com/hudduapp/sdk",
    }
)
