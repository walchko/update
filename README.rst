===============
Updt (Update)
===============

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

Still in development

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

::

	[kevin@Tardis updt]$ updt -h
	usage: A simple automation tool to update your system. [-h] [-k]

	optional arguments:
	  -h, --help      show this help message and exit
	  -k, --kernel    update linux kernel, default is not too

The default is everything gets updated except the linux kernel.

::

	kevin@Tardis tmp $ updt.py
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


--------
Changes
--------
=============  ========  ======
Date           Version   Notes
=============  ========  ======
23 Jul 16      0.3.0     error fix
23 Jul 16      0.2.0     refactoring
11 Jul 15      0.1.0     created
=============  ========  ======
