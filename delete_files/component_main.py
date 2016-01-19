"""
component_main.py

@author: bgrande
"""
import os
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    """
    Split FASTQ files into smaller ones.
    """

    def __init__(self, component_name="delete_files", component_parent_dir=None,
                 seed_dir=None):
        self.version = "v1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = ''
        cmd_args = []
        args_dict = vars(self.args)
        # Build command
        # Deal with files using rm
        if "files" in args_dict and args_dict["files"]:
            cmd_args.append("rm")
            if isinstance(args_dict["files"], list):
                cmd_args.extend(args_dict["files"])
            else:
                cmd_args.append(args_dict["files"])
                print args_dict["files"]
            cmd_args.append(";")
        # Deal with input_dir using find
        # find /path/to/directory -type f -maxdepth 1 -exec rm -iv {} \;
        if "input_dir" in args_dict and args_dict["input_dir"]:
            cmd_args.extend(["find", args_dict["input_dir"], "-maxdepth", "1", "-type", "f"])
            if args_dict["file_extension"]:
                cmd_args.extend(["-name", '"{}"'.format(args_dict["file_extension"])])
            cmd_args.extend(["-exec", "rm", "{}", "\;"])
        # Return cmd and cmg_args
        return cmd, cmd_args


# To run as stand alone
def _main():
    comp = Component()
    comp.args = component_ui.args
    comp.run()


if __name__ == '__main__':
    import component_ui
    _main()
