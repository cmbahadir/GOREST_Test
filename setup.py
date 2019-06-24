from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='GOREST-TEST',
    version='1.0',
    description='API and Front-End test of gorest.co.in using pytest and selenium-webdriver',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cmbahadir/gorest-test',
    author='Cihan Mete BAHADIR',
    author_email='selftronics@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='test selenium-webdriver api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=['pytest','requests','selenium'],
    # # extras_require={
    # #     'dev': ['check-manifest'],
    # #     'test': ['coverage'],
    # # },
    # # package_data={  # Optional
    # #     'sample': ['package_data.dat'],
    # # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # # data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # # entry_points={  # Optional
    # #     'console_scripts': [
    # #         'sample=sample:main',
    # #     ],
    # # },

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    # # project_urls={  # Optional
    # #     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    # #     'Funding': 'https://donate.pypi.org',
    # #     'Say Thanks!': 'http://saythanks.io/to/example',
    # #     'Source': 'https://github.com/pypa/sampleproject/',
    # # },
)