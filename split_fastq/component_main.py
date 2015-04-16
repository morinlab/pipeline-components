"""
component_main.py

@author: autogen_component.py
"""

from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    Split FASTQ files into smaller ones.
    """

    def __init__(self, component_name="split_fastq", component_parent_dir=None,
                 seed_dir=None):
        self.version = "v1.1.4"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["python"]
        cmd_args = [self.requirements["split_fastq.py"]]
        args_dict = vars(self.args)
        # Optional arguments
        opt_args = {
            'no_compression': '--no_compression', 'interval_file': '--interval_file',
            'num_buffer': '--num_buffer', 'output_dir': '--output_dir',
            'num_reads': '--num_reads', 'no_symlink': '--no_symlink'}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and not isinstance(v, bool) and v is not None])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and isinstance(v, bool)])
        # Positional arguments
        pos_args = ['fastq_files']
        cmd_args.extend([args_dict[arg] for arg in pos_args if arg in args_dict and
                        not isinstance(args_dict[arg], list)])
        cmd_args.extend([" ".join(args_dict[arg]) for arg in pos_args if arg in args_dict and
                        isinstance(args_dict[arg], list)])
        # Return cmd and cmg_args
        return cmd, cmd_args

    def test(self):
        component_test.run_tests()


# To run as stand alone
def _main():
    comp = Component()
    comp.args = component_ui.args
    comp.run()


if __name__ == '__main__':
    import component_ui
    _main()
