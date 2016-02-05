"""
component_reqs.py
@author: jgrewal
"""

## TODO: here goes the list of the environment variables, if any,
## required to export for the component to function properly.
env_vars = {
# 			'env_var1' : ['value1', 'value2'],
# 			'env_var2' : 'value3'
			}

## TODO: here goes the max amount of the memory required. 
memory = '20G'

## TODO: set this to True if the component is parallelizable.
parallel = False

## TODO: here goes the list of the required software/apps
## called by the component.  
requirements = {
                                'picardtools': '/home/jgrewal/software/picard/picard-tools-1.119/',
                                'python': '/home/jgrewal/anaconda/bin/python/',
                                'java': '/gsc/software/linux-x86_64-centos5/java-1.7.0-u13/bin/'

				}

## TODO: here goes the version of the component seed.
seed_version = '1.119'

## TODO: here goes the version of the component itself. 
version = '1.0.0'
