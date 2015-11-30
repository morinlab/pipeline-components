"""
component_main.py

@author: bgrande
"""

import glob
import os.path
import logging
from pipeline_factory.utils import ComponentAbstract


class Component(ComponentAbstract):

    """
    Template
    """

    def __init__(self, component_name="template", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, args_dict, chunk):
        pass

    def make_cmd(self, chunk=None):

        # Component options
        arg_prefix = "--"  # What is before every argument
        arg_sep = "_"  # Separator in every argument, such as "-" or "". Set to "_" to leave as is
        val_sep = " "  # Separator in a list of them for one argument, such as " " or ","
        arg_val_sep = " "  # Separator between argument name and value, such as " " or "="
        flag_val = ""  # Value for setting a flag argument to true, such as "" or "true"

        # Program or interpreter
        args_dict = vars(self.args)
        cmd = self.requirements["python"]
        cmd_args = [self.requirements["sequenza-utils.py"]]

        # Parallelize if given chunk
        if chunk:
            self.focus(args_dict, chunk)

        # Extract special arguments
        spec_args = ["compress_seqz", "output"]
        spec_args_dict = {k: v for k, v in args_dict.items() if k in spec_args}
        for arg in spec_args:
            del args_dict[arg]

        # Extract positional arguments
        pos_args = []  # Order matters here
        pos_args_dict = {k: v for k, v in args_dict.items() if k in pos_args}
        for arg in pos_args:
            del args_dict[arg]

        # Command-line arguments
        for arg, val in args_dict.items():

            # Prepare formatted argument for command line
            arg = arg.replace("_", arg_sep)
            if arg in exceptions:
                fmtd_arg = "{}{}".format("-", arg)
            else:
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

        # Add positional arguments
        for arg in pos_args:
            if arg in pos_args_dict:
                if isinstance(pos_args_dict[arg], (list, tuple)):
                    cmd_args.extend(pos_args_dict[arg])
                else:
                    cmd_args.append(pos_args_dict[arg])

        # Handle special arguments
        if "compress_seqz" in spec_args_dict:
            cmd_args.extend([
                "|",
                "gzip",
                ">",
                spec_args_dict["output"]
            ])
        else:
            cmd_args.extend([
                ">",
                spec_args_dict["output"]
            ])

        # Return cmd and cmg_args
        return cmd, cmd_args
