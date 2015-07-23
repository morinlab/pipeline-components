"""
component_main.py

@author: bgrande
"""

from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    vcf2maf_1_5_4
    """

    def __init__(self, component_name="vcf2maf_1_5_4", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.5.4"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):

        # Component options
        arg_prefix = "--"  # What is before every argument
        arg_sep = "_"  # Separator in every argument, such as "-", "_" or "". False to disable
        val_sep = " "  # Separator in a list of them for one argument, such as " " or ","
        arg_val_sep = " "  # Separator between argument name and value, such as " " or "="

        # Program or interpreter
        args_dict = vars(self.args)
        cmd = self.requirements["interpreter"]
        cmd_args = [self.requirements["script"]]

        # Optional arguments
        for raw_arg, val in args_dict.items():

            # Prepare argument for command line
            if arg_sep:
                raw_arg = raw_arg.replace("_", arg_sep)
            arg = "{}{}".format(arg_prefix, raw_arg)

            # Add argument to command line arguments
            # One value
            if not isinstance(val, bool) and not (isinstance(val, list) or isinstance(val, tuple)):
                cmd_args.extend(["{}{}{}".format(arg, arg_val_sep, val)])
            # List of values
            elif not isinstance(val, bool) and (isinstance(val, list) or isinstance(val, tuple)):
                cmd_args.extend(["{}{}{}".format(arg, arg_val_sep, val_sep.join(val))])
            # Flag
            elif isinstance(val, bool) and val:
                cmd_args.extend(["{}".format(arg, val)])
            # Everything else
            else:
                pass

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
