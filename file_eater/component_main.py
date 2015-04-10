""" 
component_main.py
This module contains Component class which extends 
the ComponentAbstract class. It is the core of a component.

@author: jgrewal
@Date Created: 02 April 2015
@Date Modified: 09 April 2015
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
        self.version = "v1.5.0"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    ## TODO: write the focus method if the component is parallelizable.
    ## Note that it should return cmd, cmd_args.
    def focus(self, cmd, cmd_args, chunk):
        pass 
#         return cmd, cmd_args

    def readcount_fastq(fastq_file):
	mycmd = "cat " + fastq_file + " | wc -l | xargs -n 1 bash -c 'echo $(($1*4))' args "
	
    ## this method should make the command and command arguments 
    ## used to run the component_seed via the command line. Note that 
    ## it should return cmd, cmd_args. 
    def make_cmd(self, chunk=None):
	#Process input files
	mycmd = self.requirements['python'] + " " + self.requirements['cmd_maker']
	inputcounterfile = "tempcounterin.txt"
	outputcounterfile = "tempcounterout.txt"
	inputsumfile = "tempsumin.txt"
	outputsumfile = "tempsumout.txt"

	args_dict = vars(self.args)

	pos_args = ['input_filenames']	
	infile_list = [" "]
	infile_list.extend([args_dict[arg] for arg in pos_args if arg in args_dict and not isinstance(args_dict[arg], list)])
	infile_list.extend([" ".join(args_dict[arg]) for arg in pos_args if arg in args_dict and isinstance(args_dict[arg], list)])

	print "ACTUAL IN LIST: "
	print self.args
	print "IN LIST: "
	print infile_list
	pos_args = ['out_files']
	outfile_list = [" "]
        outfile_list.extend([args_dict[arg] for arg in pos_args if arg in args_dict and not isinstance(args_dict[arg], list)])
        outfile_list.extend([" ".join(args_dict[arg]) for arg in pos_args if arg in args_dict and isinstance(args_dict[arg], list)])

	indir = self.args.in_dir
	outdir = self.args.out_dir
	cmd_args_in = mycmd + " -i " + indir.join(infile_list) + " -t " + self.args.filetype_in + " -o " + inputcounterfile + " --samtools " + self.requirements['samtools']
	cmd_args_out = mycmd + " -i " + outdir.join(outfile_list) + " -t " + self.args.filetype_out + " -o " + outputcounterfile + " --samtools " + self.requirements['samtools']
        cmd = " && ".join(["touch "+inputcounterfile, "touch "+outputcounterfile, cmd_args_in, cmd_args_out])
	cmd_args = ["&& awk '{ sum += $1 } END { print sum }' " + inputcounterfile + " > " + inputsumfile + " && ", "awk '{ sum += $1 } END { print sum }' " + outputcounterfile + " > " + outputsumfile + " && ", " rm " + inputcounterfile + " " + outputcounterfile]
	cmd_args = cmd_args + [ " && " + self.requirements['python'] + " " + self.requirements['file_remover'] + " -c1 " + inputsumfile + " -c2 " + outputsumfile + " -ri " + indir.join(infile_list)] 

	#args_dict = vars(self.args)
	#pos_args = ['input_files']
	#cmd_args = [" "]
	#cmd_args.extend([args_dict[arg] for arg in pos_args if arg in args_dict and
         #               not isinstance(args_dict[arg], list)])
        #cmd_args.extend([" ".join(args_dict[arg]) for arg in pos_args if arg in args_dict and
        #                isinstance(args_dict[arg], list)])
	return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

