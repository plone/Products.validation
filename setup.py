from pathlib import Path
from setuptools import setup


version = "4.0.0"

long_description = (
    f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst').read_text()}\n"
)

setup(
    name="Products.validation",
    version=version,
    description="Data validation package for Zope",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 6 - Mature",
        "Framework :: Zope",
        "Framework :: Zope :: 5",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="Zope validation regex email",
    author="Benjamin Saller",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/plone/Products.validation",
    license="GPL",
    include_package_data=True,
    zip_safe=False,
    extras_require={},
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "Zope",
    ],
)
