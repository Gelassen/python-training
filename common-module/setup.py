import site
print(site.getsitepackages())

from setuptools import setup, find_packages

setup(
    name='common_module',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)