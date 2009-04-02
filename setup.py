from setuptools import setup, find_packages
import os

version = '1.6.2'

setup(name='Products.validation',
      version=version,
      description="Data validation package for Archetypes",
      long_description=open("README.txt").read() + "\n" + \
              open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "Operating System :: OS Independent",
        ],
      keywords='Zope catalog index',
      author='Benjamin Saller',
      author_email='plone-developers@lists.sourceforge.net',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
