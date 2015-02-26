""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
"""

from pipeline_factory.utils import ComponentAbstract
import os

class Component(ComponentAbstract):
    
    """
    TODO: This component is explicitly for samtools view. It takes a bam input and generates an output corresponding to the params specified for samtools view.

    INPUT:
	- input BAM file
	- options
    """

    def __init__(self, component_name="samtools_view", 
                 component_parent_dir=None, seed_dir=None):
        
        self.version = "v2.16"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args, chunk):
	if(self.args.splitbam=='True'):	#Set samflag 'intervals' when splitbam is True
		if(chunk== 'f4'):
			prefix=".paired"
		if(chunk== 'F4'):
			prefix=".unpaired"
		outfile=re.sub('.bam$','',self.args.input_file)
        	cmd_args=cmd_args + ['-' + str(chunk)] + ['-o ' + outfile+prefix+'.bam']#chunk is either f4 or F4
		return cmd, cmd_args

    def make_cmd(self, chunk=None):
	cmd = os.path.join(self.requirements['samtools'], 'samtools view')
	if (self.args.splitbam):
		cmd_args = [
			'-bh '
		]
		#cmd, cmd_args = self.focus(cmd, cmd_args,chunk)
		if hasattr(self.args,'flag4'):
			if (self.args.flag4=="True"):
				cmd_args=cmd_args + ['-f4'] + ['-o ' +self.args.output_file]#+ self.args.input_file+'paired.bam']#chunk is either f4 or F4
			if (self.args.flag4=="False"):
                                cmd_args=cmd_args + ['-F4'] + ['-o ' +self.args.output_file]#+ self.args.input_file+'unpaired.bam']#chunk is either f4 or F4
		else:
			cmd_args.extend((
				'-o '+self.args.output_file
			))
		if hasattr(self.args, 'test') & 0:
			[
			cmd_args.extend((
				'-c'
			))
			]
		cmd_args=cmd_args+[self.args.input_file]
	else:
		cmd_args = [
			self.args.options, #If not splitting bam, assuming user defines all remaining components for samtools view ? command
			'-o '+self.args.output_file,
			self.args.input_file
		]
        return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

