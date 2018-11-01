from setuptools import setup, find_packages

version = '2.1.1'

setup(
    name='Products.validation',
    version=version,
    description="Data validation package for Zope",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Framework :: Zope2",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='Zope validation regex email',
    author='Benjamin Saller',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.org/project/Products.validation',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    extras_require={},
    install_requires=[
        'setuptools',
        'six',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
        'Acquisition',
        'DateTime',
        'Zope2',
    ],
)
