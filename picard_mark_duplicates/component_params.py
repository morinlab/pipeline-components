"""
component_params.py

@author: bgrande
"""


input_files = {"INPUT": "__REQUIRED__",
               "REFERENCE_SEQUENCE": "__OPTIONAL__"}

output_files = {"OUTPUT": "__REQUIRED__",
                "METRICS_FILE": "__REQUIRED__",
                "TMP_DIR": "__OPTIONAL__"}

input_params = {"picard_command": "MarkDuplicates",
                "java_memory": "__OPTIONAL__",
                "VERBOSITY": "__OPTIONAL__",
                "QUIET": "__FLAG__",
                "VALIDATION_STRINGENCY": "__OPTIONAL__",
                "COMPRESSION_LEVEL": "__OPTIONAL__",
                "MAX_RECORDS_IN_RAM": "__OPTIONAL__",
                "CREATE_INDEX": "__FLAG__",
                "CREATE_MD5_FILE": "__FLAG__",
                "GA4GH_CLIENT_SECRETS": "__OPTIONAL__",
                "MAX_FILE_HANDLES_FOR_READ_ENDS_MAP": "__OPTIONAL__",
                "SORTING_COLLECTION_SIZE_RATIO": "__OPTIONAL__",
                "PROGRAM_RECORD_ID": "__OPTIONAL__",
                "PROGRAM_GROUP_VERSION": "__OPTIONAL__",
                "PROGRAM_GROUP_COMMAND_LINE": "__OPTIONAL__",
                "PROGRAM_GROUP_NAME": "__OPTIONAL__",
                "COMMENT": "__OPTIONAL__",
                "REMOVE_DUPLICATES": "__FLAG__",
                "ASSUME_SORTED": "__FLAG__",
                "DUPLICATE_SCORING_STRATEGY": "__OPTIONAL__",
                "READ_NAME_REGEX": "__OPTIONAL__",
                "OPTICAL_DUPLICATE_PIXEL_DISTANCE": "__OPTIONAL__"}

return_value = []
