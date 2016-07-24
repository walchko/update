===============
Update
===============

.. image:: https://travis-ci.org/walchko/updt.svg?branch=master
    :target: https://travis-ci.org/walchko/updt
.. image:: https://img.shields.io/pypi/v/update.svg
    :target: https://pypi.python.org/pypi/update/
    :alt: Latest Version
.. image:: https://img.shields.io/pypi/dm/update.svg
    :target: https://pypi.python.org/pypi/update/
    :alt: Downloads
.. image:: https://img.shields.io/pypi/l/update.svg
    :target: https://pypi.python.org/pypi/update/
    :alt: License

A simple tool for admins to keep various command line tools updated. It currently supports:

- pip
- homebrew
- apt-get
- rpi-update

Still in development

--------
Install
--------

The preferred way is to use `pypi.org <https://pypi.python.org/pypi>`_ ::

	pip install update

You can also do::

	git clone https://github.com/walchko/update.git
	cd update
	python setup.py install

If you plan on doing some development, instead of `install` you can do `develop`.

------
Usage
------

::

	[kevin@Tardis ~]$ update -h
	usage: A simple automation tool to update your system. [-h] [-k]

	optional arguments:
	  -h, --help      show this help message and exit
	  -k, --kernel    update linux kernel, default is not too

The default is everything gets updated except the linux kernel.

::

	kevin@Tardis tmp $ update
	OS: macOS
	Executing NOT as root
	-[pip]----------
	  [>] pip list --outdated
	  >> Found 4 packages
	  [>] pip install -U setuptools
	  [>] pip install -U PySDL2
	  [>] pip install -U requests-toolbelt
	  [>] pip install -U rst2pdf
	-[brew]----------
	  [>] brew update
	  [>] brew outdated
	  >> Found 15 packages
	  [>] brew upgrade gd
	  [>] brew upgrade git
	  [>] brew upgrade harfbuzz
	  [>] brew upgrade imagemagick
	  [>] brew upgrade iperf3
	  [>] brew upgrade libtool
	  [>] brew upgrade little-cms2
	  [>] brew upgrade luajit
	  [>] brew upgrade node
	  [>] brew upgrade pandoc
	  [>] brew upgrade pkg-config
	  [>] brew upgrade poco
	  [>] brew upgrade srcclr/srcclr/srcclr
	  [>] brew upgrade webp
	  [>] brew upgrade zeromq
	-[npm]----------
	  [>] npm outdated -g | awk 'NR>1 {print $1}'
	  >> Found 1 packages
	  [>] npm update -g  npm

--------------
Development
--------------

::

	python setup.py develop
	python setup.py sdist
	twine upload dist/*

--------
Changes
--------

=============  ========  ======
Date           Version   Notes
=============  ========  ======
23 Jul 16      0.4.0     rename
11 Jul 15      0.1.0     created
=============  ========  ======
