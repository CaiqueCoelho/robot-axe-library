import pathlib
import sys
from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


PY3 = sys.version_info > (3,)

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

version_file = join(dirname(abspath(__file__)), 'src', 'RobotAxeLibrary', 'version.py')
with open(version_file) as file:
    code = compile(file.read(), version_file, 'exec')
    exec(code)

CLASSIFIERS = [
"License :: OSI Approved :: MIT License",
"Programming Language :: Python",
"Programming Language :: Python :: 2",
"Programming Language :: Python :: 2.7",
"Programming Language :: Python :: 3",
"Programming Language :: Python :: 3.6",
"Programming Language :: Python :: 3.7",
"Programming Language :: Python :: 3.8",
"Topic :: Software Development :: Testing",
]


setup(
      name='robot-axelibrary',
      version=VERSION,
      description='Robot Framework Library wrapper axe-selenium-python',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Caique Coelho',
      author_email='caiquedpfc@gmail.com',
      url='https://github.com/CaiqueCoelho/robot-axe-library',
      license='MIT',
      keywords='robotframework testing automation axe selenium python',
      platforms='any',
      classifiers=CLASSIFIERS,
      package_dir={'': 'src'},
      packages=['RobotAxeLibrary'],
      include_package_data=True,
      install_requires=[
          'robotframework',
          'axe-selenium-python'
      ],)