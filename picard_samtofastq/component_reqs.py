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
		'picardtools': '/gsc/software/linux-x86_64/picard-tools-1.71/',
                'java': '/gsc/software/linux-x86_64-centos5/java-1.7.0-u13/bin/',				
}

## here goes the version of the component seed.
seed_version = 'version 1.71'

## here goes the version of the component itself. 
version = 'v1.0.5'
