import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="updt",
    version="0.1.0",
    author="Kevin Walchko",
    keywords=['pip','apt-get','update'],
    author_email="kevin.walchko@outlook.com",
    description="A simple python script to update various tools via the command line.",
    license="MIT",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',

        # Operating systems this runs on
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',

        # what does this do?
        'Topic :: Utilities',
        'Topic :: System :: Shells',
        'Environment :: Console'
    ],
    install_requires=['psutil'],
    url="https://github.com/walchko/updt",
    long_description=read("README.rst"),
    #description-file = 'README.md',
    #packages=["updt"],
    entry_points={
        'console_scripts': [
            'updt=updt:main',
        ],
    },
)
