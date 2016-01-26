"""
component_reqs.py
@author: jgrewal
"""

## here goes the list of the environment variables, if any,
## required to export for the component to function properly.
env_vars = {
# 			'env_var1' : ['value1', 'value2'],
# 			'env_var2' : 'value3'
			}

## here goes the max amount of the memory required. 
memory = '5G'

## set this to True if the component is parallelizable.
parallel = False

## here goes the list of the required software/apps
## called by the component.  
requirements = {
		'python': 'python',
		'samtools': 'samtools',
#                'python': "/home/bgrande/software/xhost09/bin/",#'python',
#                'samtools': "/home/bgrande/software/xhost09/bin/"#'samtools'    
				}

## here goes the version of the component seed.
seed_version = 'v2.16'

## here goes the version of the component itself. 
version = '2.0'
