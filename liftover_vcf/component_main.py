""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 6 March 2015
@Date Modified: 6 March 2015
"""

from kronos.utils import ComponentAbstract
import os

class Component(ComponentAbstract):
    
    """
    	This is a wrapper for the gatk liftoverVCF.pl script. It is used to liftover vcfs aligned to an old reference, to vcfs relative to a new reference. The vcf, and the two references, must be karyotypically sorted.
    """

    def __init__(self, component_name="liftover_vcf", 
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
	path=os.path.join(self.seed_dir,'gatk/liftOverVCF.pl')
	cmd=path
	cmd_args=['-vcf '+self.args.input_vcf,'-out '+self.args.output_file,'-chain '+self.args.chain_file,'-oldRef '+self.args.old_ref,'-newRef '+self.args.new_ref]    	
	cmd_args=cmd_args + ['-gatk '+self.seed_dir+'/gatk/']	#self.requirements['gatk']]
	return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

