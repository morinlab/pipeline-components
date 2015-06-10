""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 18 February 2015
@Date Modified: 10 June 2015
"""

from pipeline_factory.utils import ComponentAbstract
import os
import glob
import re

class Component(ComponentAbstract):
    
    """
   This PicardTools component forms FASTQ files from an input bam file.

   Input:
	- input BAM (must be a bam with properly paired reads)
	- (optional) output fastq directory

   Outputs:
	- two (for paired-end reads) FASTQ files 
    """

    def __init__(self, component_name="picard_samtofastq", 
                 component_parent_dir=None, seed_dir=None):
	self.version = "v3.0.0"
        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args,chunk):
	pass

    def make_cmd(self, chunk=None):
	path = os.path.join(self.requirements['picardtools'], 'SamToFastq.jar')
        cmd = self.requirements['java'] + 'java -Xmx' + self.args.javamem + ' -XX:-UseGCOverheadLimit -XX:-UseParallelGC ' + ' -jar ' + path
	cmd_args = [
			'VERBOSITY='+self.args.verbosity,
			'QUIET='+self.args.quiet,
			'VALIDATION_STRINGENCY='+self.args.val_stringency,
	]
	infile = self.args.input_bam
	infile_prefix = re.search(r"[^/]*$",infile).group() #Get name of paired bam file
	infile_prefix = re.sub("\.paired\.bam$","",infile_prefix)  #remove the .bam from the end
	if(self.args.outfile1 is not None) & (self.args.outfile2 is not None): #Output is output_dir/outfilex
		out1 = "".join([self.args.output_dir,"/",self.args.outfile1])
		out2 = "".join([self.args.output_dir,"/",self.args.outfile2])
	else:
		out1 = "".join([self.args.output_dir,"/",infile_prefix,".R1.fq"])
		out2 = "".join([self.args.output_dir,"/",infile_prefix,".R2.fq"])

	cmd_args = cmd_args + ['INPUT='+infile] + ['FASTQ='+out1] + ['SECOND_END_FASTQ='+out2]
	if(!(self.args.no_compression)):
		cmd_args = cmd_args + ['& gzip ' + out1 + ' & gzip ' + out2]
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

