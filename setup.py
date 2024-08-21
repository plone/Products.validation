from setuptools import find_packages
from setuptools import setup


version = "3.0.0"

setup(
    name="Products.validation",
    version=version,
    description="Data validation package for Zope",
    long_description=(open("README.rst").read() + "\n" + open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 6 - Mature",
        "Framework :: Zope",
        "Framework :: Zope :: 5",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="Zope validation regex email",
    author="Benjamin Saller",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/plone/Products.validation",
    license="GPL",
    packages=find_packages(),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    extras_require={},
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "Zope",
    ],
)
