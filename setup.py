from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='foobar3',
      version='1.0',
      description='A minimal stub package to test success of pip install',
      long_description=long_description,
      author='Winson Luk',
      author_email='winson.luk@gmail.com',
      license='MIT',
      packages=['foobar3'],
      zip_safe=False)
