"""
component_main.py

@author: bgrande
"""

from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    Filter for somatic SVs.
    """

    def __init__(self, component_name="somaticFilter", component_parent_dir=None,
                 seed_dir=None):
        self.version = "2.4.1d"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        args_dict = vars(self.args)
        cmd = self.requirements["star_binary"]
        cmd_args = []
        # Optional arguments
        opt_args = {'runMode': '--runMode',
                    'genomeDir': '--genomeDir',
                    'genomeFastaFiles': '--genomeFastaFiles',
                    'runThreadN': '--runThreadN',
                    'readFilesIn': '--readFilesIn',
                    'sjdbFileChrStartEnd': '--sjdbFileChrStartEnd',
                    'sjdbOverhang': '--sjdbOverhang',
                    'outFileNamePrefix': '--outFileNamePrefix',
                    'outSAMtype': '--outSAMtype',
                    'readFilesCommand': '--readFilesCommand',
                    'outSAMmode': '--outSAMmode'}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and not isinstance(v, bool) and v is not None and
                         not isinstance(v, list)])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and isinstance(v, bool) and v])
        cmd_args.extend(["{} {}".format(opt_args[k], " ".join(v)) for k, v in args_dict.items()
                         if k in opt_args and not isinstance(v, bool) and v is not None and
                         isinstance(v, list)])
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
