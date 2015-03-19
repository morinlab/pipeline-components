"""
component_main.py

@author: bgrande
"""

from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    This bam_to_fastq component converts a BAM file
    into a FASTQ file.

    Input:
    - One BAM file (intended for single-end reads)

    Output:
    - One FASTQ file
    """

    def __init__(self, component_name="bam_to_fastq", component_parent_dir=None, seed_dir=None):
        self.version = "v1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["python"]
        cmd_args = [self.requirements["bam_to_fastq.py"]]
        args_dict = vars(self.args)
        # Positional arguments
        pos_args = ["input_bam", "output_fastq"]
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
