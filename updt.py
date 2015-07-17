#!/usr/bin/env python

import commands # execute tools
import sys      # get os
import argparse # command line
import time     # sleep
import os       # check for root/sudo

def outdated(pkg):
	"""
	Sometimes the list commands returns Warnings, so you need to account for that.
	[kevin@Tardis updt]$ pip list | grep pip
	pip (7.1.0)
	"""
	ans = commands.getoutput('pip show %s | grep ^Version:'%pkg)
	pip_curr = ans.split()[1]
	
	ans = commands.getoutput('pip list | grep %s'%pkg)
	a=ans.split('\n')
	sys_curr = ''
	for i in a:
		b = i.split()
		if b[0] == pkg:
			sys_curr = b[1].replace('(','').replace(')','')
			break
	
	#print pip_curr,sys_curr,pip_curr==sys_curr
	
	if pip_curr==sys_curr: return False
	else: return True

def pip():
	print '-[pip]----------'
	# update and setuptools first
	pkgs = ['pip','setuptools']
	print 'update pip and setuptools'
	for p in pkgs:
		if outdated(p):
			ans = commands.getoutput('pip install -U %s'%(p))
			if ans: print ans
		else: print p,'is already up to date'
	
	# find outdated packages
	p = commands.getoutput('pip list --outdated').split('\n')
	pkgs = []
	for i in p:
		if i.find('===') > 0: continue
		
		pkg = i.split()[0]
		# print pkg
		if pkg   == 'Warning:': continue
		elif pkg == 'Could': continue
		elif pkg == 'Some': continue
		elif pkg == 'You': continue
		pkgs.append(pkg)
	
	if not pkgs:
		print 'Nothing to update'
		return
		
	# update packages
	print 'Found',len(pkgs),'packages:',' '.join( pkgs )
	time.sleep(5)
	for p in pkgs:
		print 'Updating:',p
		ans = commands.getoutput('pip install -U %s'%(p))
		if ans: print ans

def brew():
	print '-[brew]----------'
	print 'brew update'
	ans = commands.getoutput('brew update')
	if ans: print ans
	print 'brew upgrade packages'
	ans = commands.getoutput('brew upgrade')
	if ans: print ans
	
	print 'brew prune old sym links'
	ans = commands.getoutput('brew prune')
	if ans: print ans
	print 'brew cleanup old packages'
	ans = commands.getoutput('brew cleanup')
	if ans: print ans

def kernel():
	print '-[kernel]----------'
	ans=commands.getoutput('uname -a')
	arm = ans.find('arm')
	
	# this is not an ARM linux computer ... can't do this
	if arm == -1: 
		print 'Not an ARM computer (RPi) ... cannot update kernel'
		return
	
	commands.getoutput('apt-get upgrade rpi-update')
	commands.getoutput('rpi-update')	

def aptget():
	print '-[apt-get]----------'
	ans=commands.getoutput('apt-get update')
	if ans: print ans
	ans=commands.getoutput('apt-get upgrade')
	if ans: print ans

def getArgs():
	parser = argparse.ArgumentParser('A simple automation tool to update your system.')
	parser.add_argument('-k', '--kernel', help='update linux kernel, default is not too', action='store_true')
	parser.add_argument('-p', '--no_pip', help='do not update pip', action='store_true')
	parser.add_argument('-t', '--no_tools', help='do not update system tools', action='store_true')
	args = vars(parser.parse_args())
	
	return args

def main():
# 	checkVersion('pip')
# 	checkVersion('setuptools')
# 	exit()
	
	# get command line
	args = getArgs()
	
	system = sys.platform
	if system == 'darwin': 
		if not args['no_pip']: pip()
		if not args['no_tools']: brew()
		
	elif system == 'linux' or system == 'linux2': 
		if os.geteuid() != 0:
				exit('You need to be root/sudo for linux ... exiting')
		
		if not args['no_pip']: pip()
		if not args['no_tools']: aptget()
		if args['kernel']: kernel()

		
	
if __name__ == "__main__":
  main()