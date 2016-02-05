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
memory = '1G'

## TODO: set this to True if the component is parallelizable.
parallel = False

## TODO: here goes the list of the required software/apps
## called by the component.  
requirements = {
			'python' : 'python',
			'samtools' : 'samtools',
			'cmd_maker' : '/home/jgrewal/projects/lab_pipeline/pipeline-components/file_eater/component_seed/count_comparefiles.py',
			'file_remover' : '/home/jgrewal/projects/lab_pipeline/pipeline-components/file_eater/component_seed/compare_deleteinput.py'		
		}

## TODO: here goes the version of the component seed.
seed_version = '1.00.0'

## TODO: here goes the version of the component itself. 
version = '1.5.0'
