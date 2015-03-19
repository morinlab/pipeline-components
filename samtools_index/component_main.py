"""
component_main.py

@author: bgrande
"""

from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    This samtools_index component indexes a BAM file.

    Input:
    - One BAM file

    Output:
    - One BAM index file (BAI)
    """

    def __init__(self, component_name="samtools_index", component_parent_dir=None, seed_dir=None):
        self.version = "v1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["samtools"]
        cmd_args = ["index"]  # samtools index subcommand
        args_dict = vars(self.args)
        # Positional arguments
        pos_args = ["bam_file"]
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
