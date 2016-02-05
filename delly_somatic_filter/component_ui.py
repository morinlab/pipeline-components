"""
component_ui.py

@author: autogen_component.py
"""

import argparse
parser = argparse.ArgumentParser(description='Filter for somatic SVs.')
parser.add_argument('-v', '--vcf', metavar='variants.vcf', required=True, dest='vcfFile', help='input vcf file (required)')
parser.add_argument('-o', '--out', metavar='out.vcf', required=True, dest='outFile', help='output vcf file (required)')
parser.add_argument('-t', '--type', metavar='DEL', required=True, dest='svType', help='SV type [DEL, DUP, INV, INS, TRA] (required)')
parser.add_argument('-a', '--altaf', metavar='0.1', required=False, dest='altAF', help='min. alt. AF (optional)')
parser.add_argument('-m', '--minsize', metavar='500', required=False, dest='minSize', help='min. size (optional)')
parser.add_argument('-n', '--maxsize', metavar='500000000', required=False, dest='maxSize', help='max. size (optional)')
parser.add_argument('-r', '--ratioGeno', metavar='0.75', required=False, dest='ratioGeno', help='min. fraction of genotyped samples (optional)')
parser.add_argument('-f', '--filter', dest='siteFilter', action='store_true', help='Filter sites for PASS')

args, unknown = parser.parse_known_args()

