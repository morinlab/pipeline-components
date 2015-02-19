"""
component_main.py

@author: bgrande
"""

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

    def focus(self, cmd, cmd_args, chunk):
        pass

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["bwa"]
        cmd_args = []
        args_dict = vars(self.args)
        # Optional arguments
        opt_args = {"num_threads": "-t"}
        cmd_args.append(["{} {}".format(opt_args[k], v) for k, v in args_dict
                        if k in opt_args and v is not True])
        cmd_args.append(["{}".format(opt_args[k], v) for k, v in args_dict
                        if k in opt_args and v is True])
        # Positional arguments
        pos_args = ["reference", "fastq_1", "fastq_2"]
        cmd_args.append([args_dict[arg] for arg in pos_args if arg in args_dict])
        # Return cmd and cmg_args
        return cmd, cmd_args

    def test(self):
        component_test.run()


# To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()


if __name__ == '__main__':
    import component_ui
    _main()
