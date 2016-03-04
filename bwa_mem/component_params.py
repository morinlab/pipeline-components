"""
component_params.py

@author: bgrande
"""


input_files = {"reads_fastq1": "__REQUIRED__",
               "reads_fastq2": "__OPTIONAL__",
               "bwa_index_prefix": "__REQUIRED__"}

output_files = {"output_bam": "__REQUIRED__"}

input_params = {"t": "__OPTIONAL__",
                "k": "__OPTIONAL__",
                "w": "__OPTIONAL__",
                "d": "__OPTIONAL__",
                "r": "__OPTIONAL__",
                "c": "__OPTIONAL__",
                "P": "__FLAG__",
                "A": "__OPTIONAL__",
                "B": "__OPTIONAL__",
                "O": "__OPTIONAL__",
                "E": "__OPTIONAL__",
                "L": "__OPTIONAL__",
                "U": "__OPTIONAL__",
                "p": "__FLAG__",
                "R": "__OPTIONAL__",
                "T": "__OPTIONAL__",
                "a": "__FLAG__",
                "C": "__FLAG__",
                "H": "__FLAG__",
                "M": "__FLAG__",
                "v": "__OPTIONAL__"}

return_value = []
