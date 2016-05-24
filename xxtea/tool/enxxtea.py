# coding=utf8

import os
import os.path
import sys
import shutil
from walkdir import *
import string

def removeHeadTailSep(odir):
	odir = odir.strip('/')
	odir = odir.strip('\\')
	return odir

def replaceOdirToNdir(inputdir, odir, ndir):
	lenth = len(odir)
	relativedir = inputdir[lenth:]
	relativedir = removeHeadTailSep(relativedir)
	dirlist = [ndir, relativedir]
	retdir = os.sep.join(dirlist)
	return retdir

def dofile():
	if len(sys.argv) != 6:
		print('usage: python enxxtea.py ./src_ori lua ./src test test')
		return
	rootdir = sys.argv[1]
	fileter = sys.argv[2]
	outdir = sys.argv[3]
	key = sys.argv[4]
	sign = sys.argv[5]

	rootdir = removeHeadTailSep(rootdir)
	outdir = removeHeadTailSep(outdir)


	files, dirs = getAllFileInRootDir(rootdir, fileter)
	if os.path.exists(outdir):
		shutil.rmtree(outdir)
	for e in dirs:
		realpath = replaceOdirToNdir(e, rootdir, outdir)
		if not os.path.exists(realpath):
			os.makedirs(realpath)
	for file in files:
		outfile = replaceOdirToNdir(file, rootdir, outdir)
		#luajit compile
		luajitcommond = []
		luajitcommond.append('luajit.exe')
		luajitcommond.append('-b')
		luajitcommond.append(file)
		luajitcommond.append(outfile)
		luajitcc = " ".join(luajitcommond)
		print('compile file: ' + file + ' to \n\t=====>' + outfile)
		os.system(luajitcc)
		
		#encode file
		commond = []
		commond.append('xxtea.exe')
		commond.append(outfile)
		commond.append(outfile)
		commond.append(key)
		commond.append(sign)
		commond.append('en')
		cc = " ".join(commond)
		print('encode file: ' + outfile)
		os.system(cc)

if __name__ == "__main__":
	dofile()