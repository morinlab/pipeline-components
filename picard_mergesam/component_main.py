""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 03 March 2015
@Date Modified: 03 March 2015
"""

from pipeline_factory.utils import ComponentAbstract
import os
import glob
class Component(ComponentAbstract):
    
    """
	This PicardTools component generates a merged BAM from multiple input SAM/BAM files. 
	Input:
		- Directory where input bams are located. Required. #Might update this to input a regex to identify batch of bams in input dir
		- name of output BAM file. Required.
		- sort order for output file. Default is Coordinate. Possible values {unsorted, queryname, coordinate}.
		- use threading (Flag). Default is true. Possible values {true, false}.
    """

    def __init__(self, component_name="picard_mergesam", 
                 component_parent_dir=None, seed_dir=None):
        
        ## pass the version of the component here.
        self.version = "v1.0.0"

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
        path=os.path.join(self.requirements['picardtools'], 'MergeSamFiles.jar')
        cmd = self.requirements['java'] + 'java -Xmx4G' + ' -jar ' + path
	infiles= ' I= '.join(glob.glob(self.args.input_dir+"/"+self.args.input_regex))#[fn for fn in os.listdir(self.args.input_file) if re.match(r'*.bam',fn)])
	cmd_args =  ['INPUT='+infiles, 'OUTPUT='+self.args.output_file,'SORT_ORDER='+self.args.sort_order,'USE_THREADING='+self.args.use_threading]
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
