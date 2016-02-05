"""
component_main.py
This module contains Component class which extends
the ComponentAbstract class. It is the core of a component.

@author: bgrande
"""

from kronos.utils import ComponentAbstract


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
        cmd_args = ["--input-vep", self.args.input_vep,
                    "--output-maf", self.args.output_maf]
        if "tumour_id" in vars(self.args):
            cmd_args.extend(["--tumor-id", self.args.tumour_id])
        if "normal_id" in vars(self.args):
            cmd_args.extend(["--normal-id", self.args.normal_id])
        return cmd, cmd_args

        # Program or interpreter
        cmd = self.requirements["perl"]
        cmd_args = [self.requirements["vcf2maf.pl"]]
        args_dict = vars(self.args)
        # Optional arguments
        opt_args = {"input_vep": "--input-vep",
                    "output_maf": "--output-maf",
                    "tumour_id": "--tumor-id",
                    "normal_id": "--normal-id",
                    "vcf_tumour_id": "--vcf-tumor-id",
                    "vcf_normal_id": "--vcf-normal-id"}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                        if k in opt_args and v is not True])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                        if k in opt_args and v is True])
        # Return cmd and cmg_args
        return cmd, cmd_args


# To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()


if __name__ == '__main__':
    import component_ui
    _main()
