"""
component_main.py

@author: bgrande
"""

import os.path
from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    This strelka component calls SNVs and indels on a
    tumour-normal pair of BAM files.

    Inputs:
    - Tumour BAM file
    - Normal BAM file

    Outputs:
    - VCF file for SNVs
    - VCF file for indels
    """

    def __init__(self, component_name="strelka", component_parent_dir=None, seed_dir=None):
        self.version = "v1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["perl"]
        cmd_args = [self.requirements["configureStrelkaWorkflow.pl"]]
        args_dict = vars(self.args)
        # Handle is_genome param
        component_extra_dir = os.path.join(os.path.dirname(__file__), "component_extra")
        if args_dict["is_genome"]:
            config = os.path.join(component_extra_dir, "strelka_config_bwa_genome.ini")
        else:
            config = os.path.join(component_extra_dir, "strelka_config_bwa_nongenome.ini")
        args_dict["config"] = config
        # Ensure that there is a directory in the file path
        # If not, prepend file path with "./"
        # This prevents "Can't resolve directory path..." errors
        if os.path.dirname(args_dict["normal_bam"]) == "":
            args_dict["normal_bam"] = os.path.join(".", args_dict["normal_bam"])
        if os.path.dirname(args_dict["tumour_bam"]) == "":
            args_dict["tumour_bam"] = os.path.join(".", args_dict["tumour_bam"])
        if os.path.dirname(args_dict["reference"]) == "":
            args_dict["reference"] = os.path.join(".", args_dict["reference"])
        if os.path.dirname(args_dict["config"]) == "":
            args_dict["config"] = os.path.join(".", args_dict["config"])
        # Optional arguments
        opt_args = {"normal_bam": "--normal",
                    "tumour_bam": "--tumor",
                    "reference": "--ref",
                    "config": "--config",
                    "output_dir": "--output-dir"}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                        if k in opt_args and v is not True])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                        if k in opt_args and v is True])
        cmd_args.append("&&")
        # Run make command
        cmd_args.extend([self.requirements["make"], "-C", args_dict["output_dir"]])
        if "num_threads" in args_dict:
            cmd_args.extend(["-j", args_dict["num_threads"]])
        cmd_args.append("&&")
        # Symlink final output files to destinations
        cmd_args.extend(["cp", os.path.join(args_dict["output_dir"], "results", "passed.somatic.snvs.vcf"), args_dict["passed_snvs_vcf"]])
        cmd_args.append("&&")
        cmd_args.extend(["cp", os.path.join(args_dict["output_dir"], "results", "passed.somatic.indels.vcf"), args_dict["passed_indels_vcf"]])
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
