"""
component_reqs.py

"""

## TODO: here goes the list of the environment variables, if any,
## required to export for the component to function properly.
env_vars = {
# 			'env_var1' : ['value1', 'value2'],
# 			'env_var2' : 'value3'
			}

## TODO: here goes the max amount of the memory required. 
memory = '5G'

## TODO: set this to True if the component is parallelizable.
parallel = False

## here goes the list of the required software/apps
## called by the component.  
requirements = {
                                'bedtools' : 'bedtools',
# 				'python': '/path/python/bin/python',
				}

## here goes the version of the component seed.
seed_version = '2.17.0'

## here goes the version of the component itself. 
version = '1.00.0'
