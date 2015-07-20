"""
component_params.py

@author: bgrande
"""


input_files = {"INPUT": "__REQUIRED__",
               "REFERENCE_SEQUENCE": "__OPTIONAL__"}

output_files = {"OUTPUT": "__REQUIRED__",
                "TMP_DIR": "__OPTIONAL__"}

input_params = {"picard_command": "AddOrReplaceReadGroups",
                "java_memory": "__OPTIONAL__",
                "VERBOSITY": "__OPTIONAL__",
                "QUIET": "__FLAG__",
                "VALIDATION_STRINGENCY": "__OPTIONAL__",
                "COMPRESSION_LEVEL": "__OPTIONAL__",
                "MAX_RECORDS_IN_RAM": "__OPTIONAL__",
                "CREATE_INDEX": "__FLAG__",
                "CREATE_MD5_FILE": "__FLAG__",
                "GA4GH_CLIENT_SECRETS": "__OPTIONAL__",
                "SORT_ORDER": "__OPTIONAL__",
                "RGID": "__OPTIONAL__",
                "RGLB": "__REQUIRED__",
                "RGPL": "__REQUIRED__",
                "RGPU": "__REQUIRED__",
                "RGSM": "__REQUIRED__",
                "RGCN": "__OPTIONAL__",
                "RGDS": "__OPTIONAL__",
                "RGDT": "__OPTIONAL__",
                "RGPI": "__OPTIONAL__",
                "RGPG": "__OPTIONAL__",
                "RGPM": "__OPTIONAL__"}

return_value = []
