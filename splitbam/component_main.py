""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 4 March 2015
@Date Modified: 4 March 2015
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
		- samflag (optional). Default is 8.
    """

    def __init__(self, component_name="splitbam", 
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
	cmd = os.path.join(self.requirements['samtools'], 'samtools view -bh')
	mysamcommand=cmd
	intrim=re.search(r"[^/]*$",self.args.input_file).group()
	myoutprefix = "".join([self.args.output_dir,"/",intrim])
	cmd_args=['-F'+self.args.samflag]
	cmd_args=cmd_args + ['-o '+myoutprefix  +".paired.bam"] + [self.args.input_file]
	cmd_args=cmd_args + ['; '+mysamcommand] + ['-f' + self.args.samflag] + ['-o ' + myoutprefix + ".unpaired.bam"] + [self.args.input_file]
	#cmd_args=['-F'+self.args.samflag, '-o '+ self.args.output_dir +"/"+self.args.input_file+'.paired.bam', self.args.input_file, '; '+mysamcommand,'-f'+self.args.samflag,'-o '+ self.args.output_dir + "/" + self.args.input_file+'.unpaired.bam',self.args.input_file]
	return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

