"""
component_params.py

@author: bgrande
"""


input_files = {"normal": "__REQUIRED__",
               "tumor": "__REQUIRED__",
               "gc": "__REQUIRED__",
               "fasta": "__REQUIRED__",
               "normal2": "__OPTIONAL__"}

output_files = {"output": "__REQUIRED__"}

input_params = {"hom": "__OPTIONAL__",
                "het": "__OPTIONAL__",
                "chromosome": "__OPTIONAL__",
                "qlimit": "__OPTIONAL__",
                "qformat": "__OPTIONAL__",
                "N": "__OPTIONAL__",
                "compress_seqz": "__FLAG__"}

return_value = []
