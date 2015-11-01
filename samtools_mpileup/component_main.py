"""
component_main.py

@author: ppararaj
"""

import glob
import os.path
import logging
from pipeline_factory.utils import ComponentAbstract
#import component_test


class Component(ComponentAbstract):

    """
    Template
    """

    def __init__(self, component_name="samtools_mpileup", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, args_dict, chunk):
        args_dict["r"] = chunk

        input_bam = os.path.basename(args_dict["input_bam"])
        exts = ["bam"]
        for ext in exts:
            if input_bam.endswith(ext):
                input_bam = input_bam[:-len(ext)-1]
                break

        # Expecting a directory in output_file since it's a parallel run
        outdir = args_dict["output_file"]
        if not os.path.isdir(outdir):
            raise ValueError("Expecting a directory when parallel_run = True.")

        if chunk.isdigit() and int(chunk) < 10:
            chunk = '%02d' % int(chunk)

        args_dict["output_file"] = os.path.join(outdir, "{}_{}.pileup".format(input_bam, chunk))

        return

    def make_cmd(self, chunk=None):

        # Component options
        arg_prefix = "-"  # What is before every argument
        arg_sep = "_"  # Separator in every argument, such as "-" or "". Set to "_" to leave as is
        val_sep = " "  # Separator in a list of them for one argument, such as " " or ","
        arg_val_sep = " "  # Separator between argument name and value, such as " " or "="
        flag_val = ""  # Value for setting a flag argument to true, such as "" or "true"

        # Program or interpreter
        args_dict = vars(self.args)
        cmd = self.requirements["samtools"]
        cmd_args = ["mpileup"]

        # Parallelize if given chunk
        if chunk:
            self.focus(args_dict, chunk)

        # Extract special arguments
        spec_args = ["output_file"]
        spec_args_dict = {k: v for k, v in args_dict.items() if k in spec_args}
        for arg in spec_args:
            del args_dict[arg]

        # Extract positional arguments
        pos_args = ["input_bam"]  # Order matters here
        pos_args_dict = {k: v for k, v in args_dict.items() if k in pos_args}
        for arg in pos_args:
            del args_dict[arg]

        # Command-line arguments
        for arg, val in args_dict.items():

            # Prepare formatted argument for command line
            if arg_sep:
                arg = arg.replace("_", arg_sep)

            fmtd_arg = ''
            if arg == "rf" or arg == "ff":
                fmtd_arg = "--{}".format(arg)
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
        cmd_args.extend([pos_args_dict[arg] for arg in pos_args if arg in pos_args_dict])

        # Handle special arguments
        cmd_args.extend([">", spec_args_dict["output_file"]])

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
