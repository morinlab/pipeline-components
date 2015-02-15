"""
component_main.py
This module contains Component class which extends
the ComponentAbstract class. It is the core of a component.

@author: Bruno Grande
"""

from pipeline_factory.utils import ComponentAbstract
import os


class Component(ComponentAbstract):

    """
    run_vcf2maf converts an Ensembl VEP-annotated
    VCF file into a MAF file.

    Inputs:
    Ensembl VEP-annotated VCF file

    Outputs:
    MAF file
    """

    def __init__(self, component_name="run_vcf2maf",
                 component_parent_dir=None, seed_dir=None):

        self.version = "v1.0.0"

        # initialize ComponentAbstract
        super(Component, self).__init__(component_name,
                                        component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args, chunk):
        pass

    def make_cmd(self, chunk=None):
        cmd = self.requirements["perl"] + " " + self.requirements["vcf2maf.pl"]
        cmd_args = ["--{} {}".format(k, v) for k, v in vars(self.args).items()]
        return cmd, cmd_args


# To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()


if __name__ == '__main__':
    import component_ui
    _main()
