"""
component_main.py

@author: ppararaj
"""

import glob
import os.path
import logging
from pipeline_factory.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    Template
    """

    def __init__(self, component_name="bam2fq", component_parent_dir=None,
                 seed_dir=None):
        self.version = "1.0.0"
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, args_dict, chunk):
		pass
        return

    def make_cmd(self, chunk=None):
        sam_path = self.requirements["samtools"]
        py_path = self.requirements["python"]
        seed_path = os.path.join(self.seed_dir, 'bam2fq.py')
        
        sam_cmd = sam_path + ' view ' + self.args.bam + ' | '
        seed_cmd = py_path + ' ' + seed_path + ' '
        cmd_args = ['--num_reads ' + self.args.num_reads + ' - ',
                    self.args.outdir]

        cmd = sam_cmd + seed_cmd
        
        # Parallelize if given chunk
        if chunk:
            self.focus(args_dict, chunk)

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
