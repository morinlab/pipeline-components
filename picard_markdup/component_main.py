""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

from pipeline_factory.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    """
    This PicardTools component generates a markdup'd BAM from an input BAM file (coordinate sorted).
	Input:
		- input BAM file (coordinate sorted)
		- name of output BAM file
		- name of output metrics file
    """

    def __init__(self, component_name="picard_markdup", 
                 component_parent_dir=None, seed_dir=None):
        
        ## TODO: pass the version of the component here.
        self.version = "v1.0.0"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    ## TODO: write the focus method if the component is parallelizable.
    ## Note that it should return cmd, cmd_args.
    def focus(self, cmd, cmd_args, chunk):
        pass 
#         return cmd, cmd_args

    ## TODO: this method should make the command and command arguments 
    ## used to run the component_seed via the command line. Note that 
    ## it should return cmd, cmd_args. 
    def make_cmd(self, chunk=None):
	path=os.path.join(self.requirements['picardtools'], 'MarkDuplicates.jar')
	cmd = self.requirements['java'] + 'java -Xmx4G' + ' -jar ' + path
	cmd_args = ['INPUT='+self.args.input_file, 'OUTPUT='+self.args.output_file, 'METRICS_FILE='+self.args.metrics_file]
	return cmd, cmd_args

    def test(self):
	import component_test
	component_test.run()
## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

