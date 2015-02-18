"""
component_params.py
@author: jgrewal
Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

## TODO: here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
                 'input.file' : '__REQUIRED__', 
		 'javamem' : 4G
                }

## TODO: here goes the list of the output files.
output_files = {
                 'fastq.output.file1' : '__REQUIRED__',
                 'fastq.output.file2' : null , # '__OPTIONAL__'
		 'fastq.unpaired.output' : null, #'__OPTIONAL__'
                 'out.dir' : null, 
		'log_file': 'samToFastq_run.log'
		}

## TODO: here goes the list of the input parameters excluding input/output files.
input_params = {
		 'output_per_rg' : false,
		 'rg.tag' : PU,
                 'rereverse.bases' : false, #'__FLAG__',
		 'interleave' : false,
                 'include.non.pf.reads' : false, #'__FLAG__',
		 'clipping.attribute' : null, #'__OPTIONAL__',
                 'clipping.action' : null, #'__OPTIONAL__',
		 'read1.trim' : 0,
		 'read1.maxbases' : null,
		 'read2.trim' : 0,
		 'read2.maxbases' : null,
		 'include.nonprimary' : false,
                 'val.stringency' : SILENT, #'__REQUIRED__',
		 'verbosity' : INFO,
		 'quiet' : false,
		 'tmp.dir' : null
		}

## TODO: here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
