"""
component_main.py

@author: bgrande
"""

from kronos.utils import ComponentAbstract
import component_test


class Component(ComponentAbstract):

    """
    Convert between different file types.
    """

    def __init__(self, component_name="delly", component_parent_dir=None,
                 seed_dir=None):
        self.version = "v1.0.0"
        super(Component, self).__init__(
            component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        # Program or interpreter
        cmd = self.requirements["delly"]
        cmd_args = []
        args_dict = vars(self.args)
        # Handle multi-threading (force 1 thread if num_threads is not specified)
        if 'num_threads' in args_dict and args_dict['num_threads'] is not None:
            cmd = 'export OMP_NUM_THREADS={}; {}'.format(args_dict['num_threads'], cmd)
        else:
            cmd = 'export OMP_NUM_THREADS=1; {}'.format(cmd)
        # Optional arguments
        opt_args = {'vcf_file': '--outfile',
                    'sv_type': '--type',
                    'reference_fasta': '--genome',
                    'excluded_regions': '--exclude',
                    'map_qual': '--map-qual',
                    'mad_cutoff': '--mad-cutoff',
                    'min_flank': '--min-flank',
                    'vcfgeno': '--vcfgeno',
                    'geno_qual': '--geno-qual'}
        cmd_args.extend(["{} {}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and not isinstance(v, bool) and v is not None])
        cmd_args.extend(["{}".format(opt_args[k], v) for k, v in args_dict.items()
                         if k in opt_args and isinstance(v, bool)])
        # Positional arguments
        pos_args = ['tumour_bam', 'normal_bam']
        cmd_args.extend([args_dict[arg] for arg in pos_args if arg in args_dict and
                        not isinstance(args_dict[arg], list)])
        cmd_args.extend([" ".join(args_dict[arg]) for arg in pos_args if arg in args_dict and
                        isinstance(args_dict[arg], list)])
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
