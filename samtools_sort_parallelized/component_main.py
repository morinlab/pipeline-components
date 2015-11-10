"""
component_main.py

@author: ppraraj
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

    def __init__(self, component_name="samtools_sort_parallelized", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, args_dict, chunk):
        pattern = os.path.join(args_dict["input_dir"], "{}.bam".format(chunk))
        files = glob.glob(pattern)
        if len(files) > 1:
            logging.warn("Found more than BAM file that matches the chunk pattern: {}".format(pattern))
        elif len(files) == 0:
            raise ValueError("No BAM files matches the chunk pattern: {}".format(pattern))
        bam_file = files[0]
        args_dict["input_bam"] = bam_file
        exts = ["bam"]
        base = os.path.basename(bam_file)
        for ext in exts:
            if bam_file.endswith(ext):
                base = bam_file[:-len(ext)-1]
                break
        args_dict["output_bam"] = os.path.join(args_dict["output_dir"], base + ".sorted")
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
        cmd_args = ["sort"]

        # Parallelize if given chunk
        if chunk:
            self.focus(args_dict, chunk)

        # Extract special arguments
        spec_args = ["input_dir", "output_dir"]
        spec_args_dict = {k: v for k, v in args_dict.items() if k in spec_args}
        for arg in spec_args:
            del args_dict[arg]

        # Extract positional arguments
        pos_args = ["input_bam", "output_bam"]  # Order matters here
        pos_args_dict = {k: v for k, v in args_dict.items() if k in pos_args}
        for arg in pos_args:
            del args_dict[arg]

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

        # Add positional arguments
        cmd_args.extend([pos_args_dict[arg] for arg in pos_args if arg in pos_args_dict])

        #cmd_args.extend([">", spec_args_dict["output_bam"]])

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
