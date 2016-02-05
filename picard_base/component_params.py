"""
component_params.py

@author: bgrande
"""


input_files = {"INPUT": "__REQUIRED__",
               "REFERENCE_SEQUENCE": "__OPTIONAL__"}

output_files = {"OUTPUT": "__REQUIRED__",
                "TMP_DIR": "__OPTIONAL__"}

input_params = {"picard_command": "__REQUIRED__",
                "java_memory": "__OPTIONAL__",
                "VERBOSITY": "__OPTIONAL__",
                "QUIET": "__FLAG__",
                "VALIDATION_STRINGENCY": "__OPTIONAL__",
                "COMPRESSION_LEVEL": "__OPTIONAL__",
                "MAX_RECORDS_IN_RAM": "__OPTIONAL__",
                "CREATE_INDEX": "__FLAG__",
                "CREATE_MD5_FILE": "__FLAG__",
                "GA4GH_CLIENT_SECRETS": "__OPTIONAL__"}

return_value = []
