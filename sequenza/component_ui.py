"""
component_ui.py

@author: bgrande
"""

import argparse
parser = argparse.ArgumentParser(description="Generate CNV calls for input bam using Sequenza")
parser.add_argument('-r', '--ref_fa', nargs=1, type=str, required=False, default = ["/reference/genomes/human/hg19a/genome/GRCh37-lite.fa"], help="Reference genome.fa file for mpileup step")
parser.add_argument('-n', '--input_normal_bam', nargs=1, type=str, required=True, help="Input normal bam")
parser.add_argument('-t', '--input_tumour_bam', nargs=1, type=str, required=True, help="Input tumour bam")
parser.add_argument('-odir', '--output_dir', nargs=1, type=str, required=True, help="Output directory address")
parser.add_argument('-su', '--seq_utils', nargs=1, type=str, required=False, default = ["/genesis/extscratch/morinlab/software/R_libs/sequenza/exec/sequenza-utils.py"],help="Sequenza utils python script location")
parser.add_argument('-sa', '--seq_analyze', nargs=1, type=str, required=False, default=["/genesis/extscratch/morinlab/software/sequenza/run-sequenza/sequenza_analysis.R"], help="Sequenza analysis script")
parser.add_argument('-gr', '--gc_ref', nargs=1, type=str, required=False, default = ["/genesis/extscratch/morinlab/shared/slin/GRCh37.gc50Base.txt.gz"], help="GC reference file for normalization")
parser.add_argument('-s', '--sample_id', nargs=1, type=str, required=True, help="Name of sample (patient)")
parser.add_argument('-g', '--gender', nargs=1, type=str, required=True, help="Gender of sample (patient). m or f")
parser.add_argument('-p', '--parallel', default=False, help="Generate mpileups for each chromosome - reduce computational time",action="store_true")
#Parse command line arguments

args, unknown = parser.parse_known_args()

