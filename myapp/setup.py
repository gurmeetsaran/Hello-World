from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='myapp',
      version=version,
      description="helloword",
      long_description="""\
helloworld""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='gurmeet',
      author_email='gurmeetx@gmail.com',
      url='https://github.com/gurmeetsaran/Hello-World',
      license='',
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
