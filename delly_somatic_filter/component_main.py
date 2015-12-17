"""
component_main.py

@author: autogen_component.py
"""

from kronos.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    Filter for somatic SVs.
    """

    def __init__(self, component_name="somaticFilter", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["python"]
        cmd_args = [self.requirements["somaticFilter.py"]]
        args_dict = vars(self.args)
        # Optional arguments
        opt_args = {'svType': '-t', 'vcfFile': '-v', 'siteFilter': '-f', 'minSize': '-m', 'outFile': '-o', 'maxSize': '-n', 'ratioGeno': '-r', 'altAF': '-a'}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and not isinstance(v, bool) and v is not None])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and isinstance(v, bool) and v])
        # Positional arguments
        pos_args = []
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
