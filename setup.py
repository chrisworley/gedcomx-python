from setuptools import setup, find_packages
from os.path import join, dirname
import gedcomx

setup(
    name='gedcomx-python',
    version=gedcomx.__version__,
	url='http://github.com/chrisworley/gedcomx-python',
	author='Christopher Worley',
	author_email='chris@chris-worley.com',
	packages=find_packages(),
	long_description="Python support for GEDCOMX project",
	install_requires=['requests']
)
