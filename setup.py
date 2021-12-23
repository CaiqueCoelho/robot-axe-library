import sys
from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


PY3 = sys.version_info > (3,)

VERSION = None
version_file = join(dirname(abspath(__file__)), 'src', 'AxeLibrary', 'version.py')
with open(version_file) as file:
    code = compile(file.read(), version_file, 'exec')
    exec(code)

CLASSIFIERS = """
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]


setup(
      name='robot-axelibrary',
      version=VERSION,
      description='Robot Framework Library wrapper axe-selenium-python',
      long_description='Robot Framework Library wrapper axe-selenium-python',
      author='Caíque Coelho',
      author_email='caiquedpfc@gmail.com',
      url='',
      license='MIT',
      keywords='robotframework testing automation axe selenium python',
      platforms='any',
      classifiers=CLASSIFIERS.splitlines(),
      package_dir={'': 'src'},
      packages=['AxeLibrary'],
      install_requires=[
          'robotframework',
          'axe-selenium-python'
      ],)