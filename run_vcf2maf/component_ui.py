"""
component_ui.py

@author: Bruno Grande
"""

import argparse

#==============================================================================
# make a UI
#==============================================================================

parser = argparse.ArgumentParser(prog='run_vcf2maf',
                                 description = """Run vcf2maf on an Ensembl VEP-annotated
                                 VCF file to create a MAF file.""")

parser.add_argument("input-vep", help="Ensembl VEP-annotated VCF file")
parser.add_argument("output-maf", help="Output MAF file")
parser.add_argument("--tumour-id", help="Tumour sample ID or name")
parser.add_argument("--normal-id", help="Normal sample ID or name")

args, unknown = parser.parse_known_args()
