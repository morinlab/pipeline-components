"""
component_main.py

@author: bgrande
"""

from kronos.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    Picard Tools AddOrReplaceReadGroups
    """

    def __init__(self, component_name="picard_addorreplacereadgroups", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.136"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        args_dict = vars(self.args)
        cmd = self.requirements["java_binary"]
        cmd_args = []
        # Add memory to command
        memory = args_dict.pop("java_memory", "2G")
        cmd_args.extend(["-Xmx{}".format(memory)])
        # Optional arguments (i.e., all arguments for GATK)
        cmd_args.extend(["-jar", self.requirements["picard_binary"]])
        cmd_args.extend([args_dict.pop("picard_command")])
        cmd_args.extend(["{}={}".format(k, v) for k, v in args_dict.items()
                         if not isinstance(v, bool) and not isinstance(v, list)])
        cmd_args.extend(["{}={}".format(k, " ".join(v)) for k, v in args_dict.items()
                         if not isinstance(v, bool) and (isinstance(v, list) or
                                                         isinstance(v, tuple))])
        cmd_args.extend(["{}=true".format(k, v) for k, v in args_dict.items()
                         if isinstance(v, bool) and v])
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
