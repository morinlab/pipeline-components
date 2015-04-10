#This script takes in 2 files containing read counts, compares the 2 files, and if they are the same
#It deletes the filenamess passed in for removal

import commands
import os
import re
import argparse
import difflib

def cmd_readcount(infile, filetype, outfile, whichsam):
	if filetype == "fastq":
        	mycmd = "cat " + infile + " | wc -l | xargs -n 1 bash -c 'echo $(($1/4))' args "
	elif filetype == "bam":
		mycmd = whichsam + " view -c " + infile + " >> " + outfile
	return mycmd

def main():
	"""Run count_comparefiles.py
	"""

	#Specify command line arguments
	parser = argparse.ArgumentParser(description="Get total counts for file list, depending on file type")
        parser.add_argument('-c1', '--countfile1', nargs=1, type=str, required=True, help="File with first sum of counts")
        parser.add_argument('-c2', '--countfile2', nargs=1, type=str, required=True, help="File with second sum of counts")
	parser.add_argument('-ri', '--input_list', nargs='+', type=str, required=True, help="List of input file names to be deleted")

	#Parse command line arguments
	args = parser.parse_args()
	count_sums = 0
	countfile1 = args.countfile1[0]
	countfile2 = args.countfile2[0]
	checkmatch = os.system("diff "+ countfile1 + " " + countfile2)
	if checkmatch == 0 : 
		os.system("rm "+ " ".join(args.input_list))
		os.system("rm "+ countfile1 + " " + countfile2)
		print "SUCCESSFULLY REMOVED INPUT FILES"
	else:
		print "ERROR! OUTPUT FILE READ COUNTS ARE DIFFERENT FROM INPUT!"
if __name__ == '__main__':
	main()
