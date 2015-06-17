""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 02 April 2015
@Date Modified: 02 April 2015
"""

from pipeline_factory.utils import ComponentAbstract
import os
import re

class Component(ComponentAbstract):
    
    """
	This component converts a bam file (containig a mix of paired and unpaired reads)
	into a single fastq file. The component used bedtools bamtofasq to accomplish this.
    """

    def __init__(self, component_name="bedtools_bamtofastq", 
                 component_parent_dir=None, seed_dir=None):
        
        ## pass the version of the component here.
        self.version = "v1.00.0"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    ## write the focus method if the component is parallelizable.
    ## Note that it should return cmd, cmd_args.
    def focus(self, cmd, cmd_args, chunk):
        pass 
#         return cmd, cmd_args

    ## this method should make the command and command arguments 
    ## used to run the component_seed via the command line. Note that 
    ## it should return cmd, cmd_args. 
    def make_cmd(self, chunk=None):
	out1 = self.args.output_fastq
	cmd=self.requirements['bedtools'] + ' ' + "bamtofastq"
	out1 = re.sub("\.gz$","",out1)
	cmd_args=["-i " + self.args.input_bam, "-fq " + out1]
	if not (self.args.no_compression):
		cmd_args = cmd_args + [' ; gzip ' + out1 ]
 	return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

