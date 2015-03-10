"""
component_main.py

@author: bgrande
"""

from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    This split_fastq component partitions large FASTQ files
    into smaller ones, mainly for parallelization.

    Inputs:
    - One (single-end) or two (paired-end) FASTQ files

    Outputs:
    - One or more FASTQ files
    """

    def __init__(self, component_name="split_fastq", component_parent_dir=None, seed_dir=None):
        self.version = "v1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["python"]
        cmd_args = [self.requirements["split_fastq"]]
        args_dict = vars(self.args)
        # Optional arguments
        opt_args = {"output_dir": "--output_dir",
                    "interval_file": "--interval_file",
                    "num_reads": "--num_reads",
                    "num_buffer": "--num_buffer",
                    "no_compression": "--no_compression"}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                        if k in opt_args and v is not True])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                        if k in opt_args and v is True])
        # Positional arguments
        pos_args = ["fastq_1", "fastq_2"]
        cmd_args.extend([args_dict[arg] for arg in pos_args if arg in args_dict])
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
