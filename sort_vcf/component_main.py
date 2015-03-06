""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 06 March 2015
@Date Modified: 06 March 2015
"""

from pipeline_factory.utils import ComponentAbstract
import os

class Component(ComponentAbstract):
    
    """
    	This component is a simple bash script that sorts a .vcf file karyotypically.
	Input:
		- input file (.vcf). Required.
		- output file name. Optional. Default output is to inputname.karo.vcf.
    """

    def __init__(self, component_name="sort_vcf", 
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
	path=os.path.join(self.seed_dir,'vcfsort.sh')
	cmd='bash ' + path
	cmd_args = [self.args.input_file]
	outfile = "".join([self.args.input_file,".karo.vcf"])
	if self.args.output_file is not None:
		cmd_args = cmd_args + ["; mv "+ outfile +" "+self.args.output_file]

	return cmd, cmd_args
## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

