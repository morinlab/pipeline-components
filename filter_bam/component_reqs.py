"""
component_reqs.py

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
			'samtools': '/path/to/samtools/',
			'picardtools': '/path/to/picardtools/',
			'java': 'java'		
		}

## here goes the version of the component seed.
seed_version = '1.1'

## here goes the version of the component itself. 
version = '1.0.0'
