"""
component_ui.py

@author: jgrewal
Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

java -Xmx4G -jar /s

import argparse

#==============================================================================
# make a UI 
#==============================================================================
## TODO: pass the name of the component to the 'prog' parameter and a
## brief description of your component to the 'description' parameter.
parser = argparse.ArgumentParser(prog='picard_samtofastq', 
                                 description = "This tool takes in a bam file and generates fastq file(s) from it")

## TODO: create the list of input options here. Add as many as desired.
parser.add_argument("--input.file", required=True,help="Bam file to be converted to fastq")
parser.add_argument("--fastq.output.file1", required=True,help="Output fasta file 1")
parser.add_argument("--fastq.output.file2",default='null', help="Output fasta file 2 (if paired bam)")
#parser.add_argument("--javamem",default='4G',help="memory allocation to java")
#parser.add_argument("--fastq.unpaired.output",default='null',help="Output unpaired fasta file (if paired bam)")
#parser.add_argument("--out.dir",default='null',help="Output directory (if processing by read groups)")


## parse the argument parser.
args, unknown = parser.parse_known_args()
