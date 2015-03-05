""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 18 February 2015
@Date Modified: 4 March 2015
"""

from pipeline_factory.utils import ComponentAbstract
import os
import glob
import re

class Component(ComponentAbstract):
    
    """
   This PicardTools component forms FASTQ files from an input bam file.

   Input:
	- input BAM directory (must have one .paired.bam, one .unpaired.bam)
	- (optional) output fastq directory

   Outputs:
	- One (single-end) or two (paired-end) FASTQ files 
    """

    def __init__(self, component_name="picard_samtofastq", 
                 component_parent_dir=None, seed_dir=None):
	self.version = "v2.1"
        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args,chunk):
	if (chunk==1): #First do paired bam
		infile = "".join(glob.glob(self.args.input_dir+"/"+"*.paired.bam"))#Get full address of paired bam file
		infile_prefix = re.search(r"[^/]*$",infile).group() #Get name of paired bam file
		infile_prefix = re.sub("\.paired\.bam$","",infile_prefix)  #remove the .bam from the end
		out1 = "".join([self.args.output_dir,"/",infile_prefix,".R1.fq"])
		out2 = "".join([self.args.output_dir,"/",infile_prefix,".R2.fq"])
		cmd_args = cmd_args + ['INPUT='+infile] + ['FASTQ='+out1] + ['SECOND_END_FASTQ='+out2]
	if (chunk==2): #Then do unpaired bam
		infile= "".join(glob.glob(self.args.input_dir+"/"+"*.unpaired.bam"))
		infile_prefix= re.search(r"[^/]*$",infile).group()
		infile_prefix = re.sub("\.unpaired\.bam$","",infile_prefix) 
		out_unpaired = "".join([self.args.output_dir,"/",infile_prefix,".unpaired.fq"])
		cmd_args = cmd_args + ['INPUT='+infile] + ['FASTQ='+out_unpaired]
	return cmd, cmd_args

    def make_cmd(self, chunk=1):
	path = os.path.join(self.requirements['picardtools'], 'SamToFastq.jar')
        cmd = self.requirements['java'] + 'java -Xmx4G' + ' -jar ' + path
	cmd_args = [
			'VERBOSITY='+self.args.verbosity,
			'QUIET='+self.args.quiet,
			'VALIDATION_STRINGENCY='+self.args.val_stringency,
	]
	
	if chunk is not None:
		cmd, cmd_args = self.focus(cmd, cmd_args,chunk)

        return cmd, cmd_args	

    def test(self):
	import component_test
	component_test.run()

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()
#   m.test()


if __name__ == '__main__':
    import component_ui
    _main()

