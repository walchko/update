=========
Updt (Update)
=========

.. image:: https://travis-ci.org/walchko/updt.svg?branch=master
    :target: https://travis-ci.org/walchko/updt
.. image:: https://img.shields.io/pypi/v/updt.svg
    :target: https://pypi.python.org/pypi/updt/
    :alt: Latest Version
.. image:: https://img.shields.io/pypi/dm/updt.svg
    :target: https://pypi.python.org/pypi/updt/
    :alt: Downloads
.. image:: https://img.shields.io/pypi/l/updt.svg
    :target: https://pypi.python.org/pypi/updt/
    :alt: License

A simple tool for admins to keep various command line tools updated. It currently supports:

- pip
- homebrew
- apt-get
- rpi-update

--------
Install
--------

The preferred way is to use `pypi.org <https://pypi.python.org/pypi>`_ ::

    pip install updt

You can also do::

    git clone https://github.com/walchko/updt.git
    cd updt
    python setup.py install

If you plan on doing some development, instead of `install` you can do `develop`.

------
Usage
------

To run::

	updt

args:

-h, --help        help
-p, --no_pip      do not update pip
-t, --no_tools    do not update system tools

The default is to update everything, but switches allow you to select what gets updated.

--------
Changes
--------
=============  ========  ======
Date           Version   Notes
=============  ========  ======
11 Jul 15      0.1.0     created
=============  ========  ======
