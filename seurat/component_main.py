"""
component_main.py

@author: ppararaj
"""

import glob
import os.path
import logging
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    def __init__(self, component_name="seurat", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):

        # Component options
        arg_prefix = "--"  # What is before every argument
        arg_sep = "_"  # Separator in every argument, such as "-" or "". Set to "_" to leave as is
        val_sep = " "  # Separator in a list of them for one argument, such as " " or ","
        arg_val_sep = " "  # Separator between argument name and value, such as " " or "="
        flag_val = ""  # Value for setting a flag argument to true, such as "" or "true"

        # Program or interpreter
        args_dict = vars(self.args)
        cmd = self.requirements["java_binary"]
        cmd_args = []

        # Add memory to command
        memory = args_dict.pop("java_memory", "2G")
        cmd_args.extend(["-Xmx{}".format(memory)])

        # Add seurat binary
        cmd_args.append("-jar {}".format(self.requirements["seurat_binary"]))

        seurat_args = ["T","I_dna_normal","I_dna_tumor"]

        if "I_rna_normal" in arg_dict:
            seurat_args.append("I_rna_normal")

        if "I_rna_tumor" in arg_dict:
            seurat_args.append("I_rna_tumor")

        seurat_args_dict = {k: v for k, v in args_dict.items() if k in seurat_args}
        for arg in seurat_args:
            del arg_dict[arg]

        # Extract special arguments
        spec_args = ["output_snv","output_indel"]
        spec_args_dict = {k: v for k, v in args_dict.items() if k in spec_args}
        for arg in spec_args:
            del args_dict[arg]

        seurat_args_mapping = { "I_dna_normal": "I:dna_normal",
                                "I_dna_tumor": "I:dna_tumor",
                                "I_rna_normal": "I:rna_normal",
                                "I_rna_tumor": "I:rna_tumor"
                              }

        # Seurat specific arguments
        for arg, val in seurat_args_dict.items():

            if arg in seurat_args_mapping:
                arg = seurat_args_mapping[arg]

            # Prepare formatted argument for command line
            if arg_sep:
                arg = arg.replace("_", arg_sep)
            fmtd_arg = "{}{}".format("-", arg)

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

        # Move SNVs into separate file
        cmd_args.append("&&")
        cmd_args.append("cat <( grep '#' " + args_dict["out"] + ") <( grep -v '#' " + args_dict["out"] + " | awk '$8 ~ \"TYPE=somatic_SNV\" {print}') > " + spec_args_dict["output_snv"])

        # Move indels into separate file
        cmd_args.append("&&")
        cmd_args.append("cat <( grep '#' " + args_dict["out"] ") <( grep -v '#' " + args_dict["out"] + " | awk '$8 ~ \"TYPE=somatic_insertion\" || $8 ~ \"TYPE=somatic_deletion\" {print}') > " + spec_args_dict["output_indel"])

        # Return cmd and cmg_args
        return cmd, cmd_args
