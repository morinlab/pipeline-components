"""
component_ui.py

@author: jgrewal
"""

import argparse

#==============================================================================
# make a UI 
#==============================================================================
## pass the name of the component to the 'prog' parameter and a
## brief description of your component to the 'description' parameter.
parser = argparse.ArgumentParser(prog='picard_samtofastq', 
                                 description = "This tool takes in a directory containing two BAM files (*.paired.bam, *.unpaired.bam) and generates 3 different fastq files from them (2 paired, 1 single-end)")

## create the list of input options here. Add as many as desired.
parser.add_argument("--input_dir", required=True,help="Directory with BAM files")
parser.add_argument("--output_dir", required=False,default="./",help="Output directory")
parser.add_argument("--verbosity", required=False,default="INFO",help="Verbosity of logging")
parser.add_argument("--quiet",required=False,default="false",help="Suppress job-summary info on System.err?")
parser.add_argument("--val_stringency",required=False,default="SILENT",help="Validation stringency for all SAM files read by this program. Possible values: {STRICT,LENIENT,SILENT}")
#parser.add_argument("--javamem",default='4G',help="memory allocation to java")
#parser.add_argument("--fastq.unpaired.output",default='null',help="Output unpaired fasta file (if paired bam)")
#parser.add_argument("--out.dir",default='null',help="Output directory (if processing by read groups)")

## parse the argument parser.
args, unknown = parser.parse_known_args()
