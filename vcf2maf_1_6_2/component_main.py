"""
component_main.py

@author: bgrande
"""

import logging
from kronos.utils import ComponentAbstract
import component_test
import os.path


class Component(ComponentAbstract):

    """
    vcf2maf 1.6.2
    """

    def __init__(self, component_name="vcf2maf_1_6_2", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.6.2"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):

        # Component options
        arg_prefix = "--"  # What is before every argument
        arg_sep = "-"  # Separator in every argument, such as "-" or "". Set to "_" to leave as is
        val_sep = " "  # Separator in a list of them for one argument, such as " " or ","
        arg_val_sep = " "  # Separator between argument name and value, such as " " or "="
        flag_val = ""  # Value for setting a flag argument to true, such as "" or "true"

        # Program or interpreter
        args_dict = vars(self.args)
        cmd = ""
        cmd_args = []

        # Symlink reference files (workaround for vcf2maf/VEP deleting FAI file)
        output_dir = os.path.dirname(args_dict["output_maf"])
        ref_fasta_basename = os.path.basename(args_dict["ref_fasta"])
        ref_fasta_linked = os.path.join(output_dir, ref_fasta_basename)
        ref_fasta_idx_linked = ref_fasta_linked + ".fai"
        cmd_args.extend(["ln", "-s", args_dict["ref_fasta"], ref_fasta_linked, "&&"])
        cmd_args.extend(["ln", "-s", args_dict["ref_fasta"] + ".fai", ref_fasta_idx_linked, "&&"])

        # Build vcf2maf command
        cmd_args.extend([self.requirements["perl"], self.requirements["vcf2maf.pl"]])
        # Command-line arguments
        for arg, val in args_dict.items():

            # Prepare formatted argument for command line
            if arg_sep:
                arg = arg.replace("_", arg_sep)
            fmtd_arg = "{}{}".format(arg_prefix, arg)

            # Add argument to command line arguments
            # One value
            if not isinstance(val, bool) and not isinstance(val, (list, tuple)):
                cmd_args.extend(["{}{}{}".format(fmtd_arg, arg_val_sep, val)])
            # List of values
            elif not isinstance(val, bool) and isinstance(val, (list, tuple)):
                cmd_args.extend(["{}{}{}".format(fmtd_arg, arg_val_sep, val_sep.join(val))])
            # Flag
            elif isinstance(val, bool) and val:
                if flag_val == "":
                    cmd_args.extend(["{}".format(fmtd_arg, val)])
                else:
                    cmd_args.extend(["{}{}{}".format(fmtd_arg, arg_val_sep, flag_val)])
            # Ignore flags set to false
            elif isinstance(val, bool) and not val:
                pass
            # Everything else
            else:
                logging.warn("Command-line argument skipped: {}".format(arg))

        # Clean up .vep.vcf files
        vcf_annot = os.path.splitext(args_dict["input_vcf"])[0] + ".vep.vcf"
        cmd_args.extend(["&&", "rm", "-f", vcf_annot])

        # Clean up reference symlinks
        cmd_args.extend(["&&", "rm", "-f", ref_fasta_linked, ref_fasta_idx_linked])

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
