# coding: utf-8

from setuptools import setup, find_packages

from distutils.command.build_py import build_py

import os

with open('README.md') as file:
    long_description = file.read()

MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')


def _get_requirements_from_files(groups_files):
    groups_reqlist = {}

    for k, v in groups_files.items():
        with open(v, 'r') as f:
            pkg_list = f.read().splitlines()
        groups_reqlist[k] = pkg_list

    return groups_reqlist


def setup_package():
    # get all file endings and copy whole file names without a file suffix
    # assumes nested directories are only down one level
    _groups_files = {
        'base': 'requirements.txt', #basic requirements
        'tests': 'requirements_tests.txt', #requirements for tests
        'docs': 'requirements_docs.txt' #requirements for building docs
    }

    reqs = _get_requirements_from_files(_groups_files)
    install_reqs = reqs.pop('base')
    extras_reqs = reqs

    # get all file endings and copy whole file names without a file suffix
    # assumes nested directories are only down one level
    #example_data_files = set()
    #for i in os.listdir("libpysal/examples"):
    #    if i.endswith(('py', 'pyc')):
    #        continue
    #    if not os.path.isdir("libpysal/examples/" + i):
    #        if "." in i:
    #            glob_name = "examples/*." + i.split(".")[-1]
    #        else:
    #            glob_name = "examples/" + i
    #    else:
    #        glob_name = "examples/" + i + "/*"

    #    example_data_files.add(glob_name)

    setup(
        name='osnap',
        version=VERSION,
        description="Open Source Neighborhood Analysis Program.",
        long_description=long_description,
        maintainer="OSNAP Developers",
        maintainer_email='pysal-dev@googlegroups.com',
        url='http://osnap.cloud',
        # download_url='https://pypi.python.org/pypi/oslnap',
        license='BSD',
        py_modules=['osnap'],
        packages=find_packages(),
        setup_requires=["pytest-runner"],
        tests_require=["pytest"],
        keywords=['spatial statistics', 'neighborhoods', 'demography'],
        classifiers=[
            'Development Status :: 1 - Alpha',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: GIS',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'
        ],
        install_requires=install_reqs,
        extras_require=extras_reqs,
        cmdclass={'build_py': build_py},
        include_package_data=True,
        package_data={'osnap': ['data/variables.csv']},
        python_requires='>3.4')


if __name__ == '__main__':
    setup_package()
