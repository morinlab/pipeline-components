"""
component_ui.py

@author: bgrande
"""

import argparse

#==============================================================================
# make a UI
#==============================================================================

parser = argparse.ArgumentParser(prog='run_ensembl_vep',
                                 description = """Annotate mutations in a VCF file
                                 using the Ensembl Variant Effect Predictor.""")

parser.add_argument("input_file", help="Input VCF file")
parser.add_argument("output_file", help="Output VEP-annotated VCF file")
parser.add_argument("dir", help="Ensembl VEP cache directory")
parser.add_argument("fasta", help="Reference genome FASTA file")
parser.add_argument("--assembly", default="GRCh37")
parser.add_argument("--fork", default="1")
parser.add_argument("--quiet", action="store_true")
parser.add_argument("--offline", action="store_true")
parser.add_argument("--no_stats", action="store_true")
parser.add_argument("--everything", action="store_true")
parser.add_argument("--check_existing", action="store_true")
parser.add_argument("--total_length", action="store_true")
parser.add_argument("--allele_number", action="store_true")
parser.add_argument("--no_escape", action="store_true")
parser.add_argument("--gencode_basic", action="store_true")
parser.add_argument("--xref_refseq", action="store_true")
parser.add_argument("--vcf", action="store_true")

args, unknown = parser.parse_known_args()
