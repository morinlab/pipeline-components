""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

from pipeline_factory.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    """
    TODO: add component doc here. 
    """

	#add seed_dir (~~/picard-tools-v.vv/)
    def __init__(self, component_name="picard_samtofastq", 
                 component_parent_dir=None, seed_dir=None):
	self.version = "v0.99.0"
        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
	path = os.path.join(self.requirements['picardtools'], 'SamToFastq.jar')
        cmd = self.requirements['java'] + ' -Xmx' +self.args.javamem + ' -jar ' + path
	if self.args.output_per_rg():
		cmd_args = ['INPUT='+self.args.input_file,
				'OUTPUT_PER_RG=true',
				'RG_TAG='+self.args.rg_tag,
				'OUTPUT_DIR='+self.args.out_dir
			]
	else:
		cmd_args = ['INPUT='+self.args.input_file,
			'FASTQ='+self.args.fastq.output.file1,
			'SECOND_END_FASTQ='+self.args.fastq_output_file2,
			'UNPAIRED_FASTQ='+self.args.fastq_unpaired_output
			]

	cmd_args.extend((
			'RE_REVERSE='+self.args.rereverse_bases,
                        'INTERLEAVE='+self.args.interleave,
                        'INCLUDE_NON_PF_READS='+self.args.include_non_pf_reads,
                        'CLIPPING_ATTRIBUTE='+self.args.clipping_attribute,
                        'CLIPPING_ACTION='+self.args.clipping_action,
                        'READ1_TRIM='+self.args.read1_trim,
                        'READ1_MAX_BASES_TO_WRITE='+self.args.read1_maxbases,
                        'READ2_TRIM='+self.args.read2_trim,
                        'READ2_MAX_BASES_TO_WRITE='+self.args.read2_maxbases,
                        'INCLUDE_NON_PRIMARY_ALIGNMENTS='+self.args.include_nonprimary
			))

	cmd_args.extend((
			'VERBOSITY='+self.args.verbosity,
			'QUIET='+self.args.quiet,
			'VALIDATION_STRINGENCY='+self.args.val_stringency,
			'TMP_DIR='+self.tmp_dir
			))
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

