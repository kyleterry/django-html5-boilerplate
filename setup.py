from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='django-html5-boilerplate',
      version=version,
      description="A nice, simple and small base template for html5 Django projects.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django html5 boilerplate template',
      author='Kyle Terry',
      author_email='kyle@kyleterry.com',
      url='http://kyleterry.com',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
