"""
component_main.py
This module contains Component class which extends
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 3 March 2015
@Date Modified: 3 March 2015
"""

from pipeline_factory.utils import ComponentAbstract
import os

class Component(ComponentAbstract):

    """
	This BamUtils tool generates a softclipped BAM from an input BAM file.
	Input:
		- Input file
		- Name of Output file
    """

    def __init__(self, component_name="clipoverlap",
                 component_parent_dir=None, seed_dir=None):

        ## pass the version of the component here.
        self.version = "v2.16"

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
	path = self.requirements['bamutils_bam_bin']
	cmd = path + ' clipOverlap '
	cmd_args = ['--in '+self.args.input_file, '--out '+self.args.output_file]
	return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

