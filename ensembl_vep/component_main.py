"""
component_main.py
This module contains Component class which extends
the ComponentAbstract class. It is the core of a component.

@author: bgrande
"""

from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    """
    run_ensembl_vep annotates the mutations
    in a VCF file using the Ensembl Variant
    Effect Predictor.

    Inputs:
    VCF file

    Outputs:
    Ensembl VEP-annotated VCF file
    """

    def __init__(self, component_name="run_ensembl_vep",
                 component_parent_dir=None, seed_dir=None):

        self.version = "v1.0.0"

        # initialize ComponentAbstract
        super(Component, self).__init__(component_name,
                                        component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args, chunk):
        pass

    def make_cmd(self, chunk=None):
        cmd = self.requirements["perl"] + " " + self.requirements["variant_effect_predictor.pl"]
        cmd_args = ["--{} {}".format(k, v) for k, v in vars(self.args).items() if v is not True]
        cmd_args.extend(["--{}".format(k) for k, v in vars(self.args).items() if v is True])
        return cmd, cmd_args


# To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()


if __name__ == '__main__':
    import component_ui
    _main()
