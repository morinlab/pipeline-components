""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

"""

from pipeline_factory.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    """
	This component takes in a bam file, read-sorts it, and then separates read pairs into a separate bam, and lone reads into another.
	Input params:
	 - input_bam (Input bam file). Required.
	 - output_paired (Name of output bam file, with paired reads). Required.
	 - output_unpaired (Name of output bam file, with unpaired reads). Required.
	 - output_readnames (Name of output text file, with list of paired readnames). Required.
	 - sort_order (Sort order of ouptut bams. Can be one of : coordinate, unsorted, queryname). Required.
	 - delete_input (Flag to remove input files once they have been filtered out). Optional.
	Requirements:
	 - Samtools
	 - NGSUtils' Bamutils
    """

    def __init__(self, component_name="filter_bam", 
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

    ## TODO: this method should make the command and command arguments 
    ## used to run the component_seed via the command line. Note that 
    ## it should return cmd, cmd_args. 
    def make_cmd(self, chunk=None):
	cmd = self.requirements['samtools'] + ' sort -no '
	cmd_view = self.requirements['samtools'] +  ' view - | '
	cmd_trim = "cut -f 1 | uniq -c | grep -P '^\s+2' | sed -r 's/^\s+2\s+//'"

	picard_path=os.path.join(self.requirements['picardtools'], 'FilterSamReads.jar')
	cmd_filtreads = self.requirements['java'] + 'java -Xmx4G' + ' -jar ' + picard_path
	cmd_args = [self.args.input_bam + " tempfile | ", cmd_view , cmd_trim, " > " + self.args.output_readnames + " ;"]
	cmd_args = cmd_args + [cmd_filtreads, 'INPUT='+self.args.input_bam, 'FILTER=includeReadList', 'RLF='+self.args.output_readnames,'SO='+self.args.sort_order,'OUTPUT='+self.args.output_paired, ' ;']
	cmd_args = cmd_args + [cmd_filtreads, 'INPUT='+self.args.input_bam, 'FILTER=excludeReadList', 'RLF='+self.args.output_readnames,'SO='+self.args.sort_order,'OUTPUT='+self.args.output_unpaired]
	if(self.args.delete_input=="true"):
		cmd_args = cmd_args + ["; rm "+self.args.input_bam]
	cmd_args = cmd_args + ["; rm *.read ; rm *_reads.txt"]
	return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

