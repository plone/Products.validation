from setuptools import setup, find_packages

version = '2.0.2'

setup(
    name='Products.validation',
    version=version,
    description="Data validation package for Archetypes",
    long_description=(open("README.txt").read() + "\n" +
                      open("CHANGES.txt").read()),
    classifiers=[
        "Framework :: Zope2",
        "Operating System :: OS Independent",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Zope catalog index',
    author='Benjamin Saller',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/Products.validation',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        test=[
            'Products.Archetypes[test]',
        ]
    ),
    install_requires=[
        'setuptools',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
        'Acquisition',
        'DateTime',
        'Zope2',
    ],
)
