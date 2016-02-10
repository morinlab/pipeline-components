"""
component_main.py

@author: autogen_component.py
"""

from kronos.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    Convert between different file types.
    """

    def __init__(self, component_name="convert_files", component_parent_dir=None,
                 seed_dir=None):
        self.version = "v1.0.0"
        super(Component, self).__init__(
            component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["python"]
        cmd_args = [self.requirements["convert_files.py"]]
        args_dict = vars(self.args)
        # Optional arguments
        opt_args = {'output_dir': '--output_dir'}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and (v is not True and v is not False)])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and (v is True or v is False)])
        # Positional arguments
        pos_args = ['input_type', 'input_parser', 'output_type', 'input_files']
        cmd_args.extend([args_dict[arg] for arg in pos_args if arg in args_dict and
                        type(args_dict[arg]) is not list])
        cmd_args.extend([" ".join(list(args_dict[arg])) for arg in pos_args if arg in args_dict and
                        type(args_dict[arg]) is list])
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
