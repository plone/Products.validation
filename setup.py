from setuptools import setup, find_packages

version = '2.1'

setup(
    name='Products.validation',
    version=version,
    description="Data validation package for Zope",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.txt").read()),
    classifiers=[
        "Framework :: Zope2",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ],
    keywords='Zope validation regex email',
    author='Benjamin Saller',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/Products.validation',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
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
