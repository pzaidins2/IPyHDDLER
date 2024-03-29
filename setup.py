from setuptools import setup, find_packages

setup(
    name='IPyHDDLER',
    version='0.0.0',
    packages=[ 'ipyhddler' ],
    url='https://github.com/pzaidins2/IPyHDDLER.git',
    license='',
    author='paulz',
    author_email='pzaidins@umd.edu',
    description='Parser for HDDL <-> IPyHOPPER',
    install_requires=["ordered_set"],
    dependency_links=['https://github.com/pzaidins2/IPyHOPPER.git']
)
