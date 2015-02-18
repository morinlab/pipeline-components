"""
component_reqs.py

@author: jgrewal
Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

## here goes the list of the environment variables, if any,
## required to export for the component to function properly.
env_vars = {
# 			'env_var1' : ['value1', 'value2'],
# 			'env_var2' : 'value3'
			}

## here goes the max amount of the memory required. 
memory = '4G'

## set this to True if the component is parallelizable.
parallel = False
 
## here goes the list of the required software/apps
## called by the component.  
requirements = {
		'picardtools': 'path to picard tools',
                'java': 'path to java',				
}

## here goes the version of the component seed.
seed_version = '0.99.0'

## here goes the version of the component itself. 
version = '0.99.0'
