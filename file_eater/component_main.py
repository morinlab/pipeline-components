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

class Component(ComponentAbstract):
    
    """
	This component takes in a list of files and deleted them!
    """

    def __init__(self, component_name="file_eater", 
                 component_parent_dir=None, seed_dir=None):
        
        ## pass the version of the component here.
        self.version = "v1.00.0"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    ## TODO: write the focus method if the component is parallelizable.
    ## Note that it should return cmd, cmd_args.
    def focus(self, cmd, cmd_args, chunk):
        pass 
#         return cmd, cmd_args

    ## this method should make the command and command arguments 
    ## used to run the component_seed via the command line. Note that 
    ## it should return cmd, cmd_args. 
    def make_cmd(self, chunk=None):
        cmd = "rm "
	args_dict = vars(self.args)
	pos_args = ['input_files']
	cmd_args = [" "]
	cmd_args.extend([args_dict[arg] for arg in pos_args if arg in args_dict and
                        not isinstance(args_dict[arg], list)])
        cmd_args.extend([" ".join(args_dict[arg]) for arg in pos_args if arg in args_dict and
                        isinstance(args_dict[arg], list)])
	return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

