"""
component_main.py

@author: bgrande
"""

import glob
import os.path
import re
import logging
from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    This bwa_mem component aligns FASTQ files to a
    given reference genome.

    Inputs:
    - One (single-end) or two (paired-end) FASTQ files
    - An indexed reference genome

    Outputs:
    - An unsorted, unindexed BAM alignment file
    """

    def __init__(self, component_name="bwa_mem", component_parent_dir=None, seed_dir=None):
        self.version = "v1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args, chunk, args_dict):
        print args_dict
        # Check if input_dir and output_dir are specified
        if "input_dir" not in args_dict or "output_dir" not in args_dict:
            raise Exception("When interval file specified, you must give an input_dir and an "
                            "output_dir.")
        # Retrieve FASTQ files based on chunks
        glob_pattern = os.path.join(args_dict["input_dir"], "*{}*fastq*".format(chunk))
        print "glob_pattern:", glob_pattern
        fastq_files = sorted(glob.glob(glob_pattern), key=lambda x: os.path.basename(x))
        print "fastq_files:", fastq_files
        args_dict["fastq_1"] = fastq_files[0]
        if len(fastq_files) == 2:
            args_dict["fastq_2"] = fastq_files[1]
        elif len(fastq_files) > 2:
            raise Exception("There are more than two FASTQ files matching this pattern: "
                            "{}".format(glob_pattern))
        # Create output_bam file name
        if "output_bam" in args_dict:
            logging.warning("Overwritting output_bam according to input file and output_dir.")
        fastq_1_filename = os.path.basename(fastq_files[0])
        fastq_1_prefix = re.match(r".*{}".format(chunk), fastq_1_filename).group(0)
        args_dict["output_bam"] = os.path.join(args_dict["output_dir"], fastq_1_prefix + ".bam")
        print args_dict
        return cmd, cmd_args, args_dict

    def make_cmd(self, chunk=None):
        print "args:", self.args
        # Program or interpreter
        cmd = self.requirements["bwa"]
        cmd_args = ["mem"]
        args_dict = vars(self.args)
        # Optional arguments
        opt_args = {"num_threads": "-t"}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and not isinstance(v, bool) and v is not None])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and isinstance(v, bool)])
        # Positional arguments
        pos_args = ["reference", "fastq_1", "fastq_2"]
        if chunk is not None:
            print "CHUNK IS NOT NONE"
            cmd, cmd_args, args_dict = self.focus(cmd, cmd_args, chunk, args_dict)
        elif chunk is None and ("input_dir" in args_dict or "output_dir" in args_dict):
            logging.warning("input_dir and output_dir only used when given an interval file "
                            "listing chunks.")
        cmd_args.extend([args_dict[arg] for arg in pos_args if arg in args_dict and
                        not isinstance(args_dict[arg], list) and args_dict[arg] is not None])
        cmd_args.extend([" ".join(args_dict[arg]) for arg in pos_args if arg in args_dict and
                        isinstance(args_dict[arg], list) and args_dict[arg] is not None])
        # Pipe output (SAM format) to samtools to convert to BAM format
        cmd_args.extend([" | ", self.requirements["samtools"], " view -bS - > ",
                        args_dict["output_bam"]])
        # Return cmd and cmg_args
        return cmd, cmd_args

    def test(self):
        component_test.run_tests()


# To run as stand alone
def _main():
    comp = Component()
    # comp.args = component_ui.args
    # comp.run()
    comp.test()


if __name__ == '__main__':
    # import component_ui
    _main()
