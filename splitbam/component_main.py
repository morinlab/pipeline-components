""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 4 March 2015
@Date Modified: 31 March 2015
"""

from pipeline_factory.utils import ComponentAbstract
import os
import re

class Component(ComponentAbstract):
    
    """
    	This component takes a BAM input and generates three output files, <infile_name>.paired.bam, <infile_name>.unpaired.bam, splitting paired reads into separate bam (R1), and the reads without a mate into a separate bam (R2).
	INPUT:
		- input BAM file. Required.
		- output directory (optional). Default is current directory (./).
		- names of output files (outfile1 is f*, outfile 2 is F*)
		- samflag (optional). Default is 2.
    """

    def __init__(self, component_name="splitbam", 
                 component_parent_dir=None, seed_dir=None):
        
        ## pass the version of the component here.
        self.version = "v2.5"

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
	cmd = self.requirements['samtools'] +  ' view -bh'
	mysamcommand=cmd
	if (self.args.output_file1 is not None) & (self.args.output_file2 is not None): #Output is output_dir/output_filex
		cmd_args=['-f'+self.args.samflag]
		cmd_args=cmd_args + ['-o ' + "".join([self.args.output_dir,"/",self.args.output_file1])] + [self.args.input_file] 
		cmd_args=cmd_args + ['; '+ mysamcommand] + ['-F' + self.args.samflag]
		cmd_args=cmd_args + ['-o ' + "".join([self.args.output_dir,"/",self.args.output_file2])] + [self.args.input_file]
	else:
		intrim=re.search(r"[^/]*$",self.args.input_file).group()
		intrim=re.sub("\.bam$","",intrim)
		myoutprefix = "".join([self.args.output_dir,"/",intrim])
		cmd_args=['-F'+self.args.samflag]
		cmd_args=cmd_args + ['-o '+myoutprefix  +".F" + self.args.samflag+".bam"] + [self.args.input_file]
		cmd_args=cmd_args + ['; '+mysamcommand] + ['-f' + self.args.samflag] + ['-o ' + myoutprefix + ".f"+self.args.samflag+".bam"] + [self.args.input_file]
	return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

