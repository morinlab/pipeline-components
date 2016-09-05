"""
component_main.py

@author: ppararaj
"""

import glob
import os.path
import logging
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    def __init__(self, component_name="varscan2_processSomatic", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.0.0"
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
        cmd = self.requirements["java_binary"]
        cmd_args = []

        # Add memory to command
        memory = args_dict.pop("java_memory", "2G")
        cmd_args.extend(["-Xmx{}".format(memory)])

        # Add varscan2 binary
        cmd_args.extend(["-jar {}".format(self.requirements["varscan2_binary"])])

        # Extract special arguments
        spec_args = ["somatic_output","somatic_hc_output","germline_output","germline_hc_output","loh_output","loh_hc_output"]
        spec_args_dict = {k: v for k, v in args_dict.items() if k in spec_args}
        for arg in spec_args:
            del args_dict[arg]

        # Extract positional arguments
        pos_args = ["varscan2_command", "varscan2_somatic_output"]  # Order matters here
        pos_args_dict = {k: v for k, v in args_dict.items() if k in pos_args}
        for arg in pos_args:
            del args_dict[arg]

        # Add positional arguments
        for arg in pos_args:
            if arg in pos_args_dict:
                if isinstance(pos_args_dict[arg], (list, tuple)):
                    cmd_args.extend(pos_args_dict[arg])
                else:
                    cmd_args.append(pos_args_dict[arg])

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

        # Extract path and basename from input
        basename = ""
        if pos_args_dict["varscan2_somatic_output"].endswith(".vcf"):
            basename = pos_args_dict["varscan2_somatic_output"][:-4]
        else:
            basename = pos_args_dict[1]

        # Move processed files
        cmd_args.append("&&")
        cmd_args.extend(["mv", basename + ".LOH.vcf", spec_args_dict["loh_output"]])
        cmd_args.append("&&")
        cmd_args.extend(["mv", basename + ".LOH.hc.vcf", spec_args_dict["loh_hc_output"]])

        cmd_args.append("&&")
        cmd_args.extend(["mv", basename + ".Germline.vcf", spec_args_dict["germline_output"]])
        cmd_args.append("&&")
        cmd_args.extend(["mv", basename + ".Germline.hc.vcf", spec_args_dict["germline_hc_output"]])

        cmd_args.append("&&")
        cmd_args.extend(["mv", basename + ".Somatic.vcf", spec_args_dict["somatic_output"]])
        cmd_args.append("&&")
        cmd_args.extend(["mv", basename + ".Somatic.hc.vcf", spec_args_dict["somatic_hc_output"]])

        # Return cmd and cmg_args
        return cmd, cmd_args
