#================================================================================
#import python modules as well as pipelinui
#--------------------------------------------------------------------------------
import sys
import ruffus
import traceback
import os

#================================================================================
#import factory modules
#--------------------------------------------------------------------------------
from pipeline_factory.utils import Task
from pipeline_factory.helpers import JobFailureError
from pipeline_factory.job_manager import ClusterJobManager, LocalJobManager
import pipeline_factory.pipelineui
from pipeline_factory.run_manager import RunManager
from pipeline_factory.logger import PipelineLogger, LogWarnErr, LogInfo

#================================================================================
#initialization
#--------------------------------------------------------------------------------
EXIT_CODE = -1
args = pipeline_factory.pipelineui.args
sample_id = args.sample_id
rm = RunManager(args.run_id, args.pipeline_name, args.working_dir)
ljm = LocalJobManager(rm.logs_dir, rm.outputs_dir)
pl = PipelineLogger(args.verbose)
l = pl.get_logger(args.pipeline_name, args.log_file)

#================================================================================
#environment preparations
#--------------------------------------------------------------------------------
sys.path.insert(0, args.components_dir)

#================================================================================
#import components
#--------------------------------------------------------------------------------
from file_eater import component_main as file_eater_main

#================================================================================
#generating tasks
#--------------------------------------------------------------------------------
__TASK_1___component = file_eater_main.Component('file_eater', component_parent_dir=args.components_dir)
__TASK_1___task = Task('__TASK_1__', __TASK_1___component)
__TASK_1___task.update_comp_args(__pipeline__input_filenames='("__SAMPLES__","paired_bam") ("__SAMPLES__","unpaired_bam") ("__SAMPLES__","paired_bam")', __pipeline__out_files='/extscratch/morinlab/projects/MCL_realignment/results/mytestdir/20150409104727/PT004_Tumor_bam_to_fastq_dev/outputs/TASK_MERGE_PAIRED_BAM_PT004_Tumor.pairedreads.bam', __pipeline__filetype_in='bam', __pipeline__filetype_out='bam', __pipeline__output_files=None, )
__TASK_1___prefix = rm.get_filename_prefix(__TASK_1___component.component_name, '__TASK_1__')
__TASK_1___task.update_comp_output_filenames(__TASK_1___prefix, rm.outputs_dir, args.no_prefix)
__TASK_1___task.update_comp_env_vars({})
__TASK_1___task.update_comp_reqs({'python': '/extscratch/morinlab/projects/MCL_realignment/software/python', 'samtools': '/extscratch/morinlab/projects/MCL_realignment/software/samtools/samtools'})

#================================================================================
#ruffus pipeline
#--------------------------------------------------------------------------------
@ruffus.follows(*[])
@ruffus.parallel(__TASK_1___component.component_name, '__TASK_1__')
@ruffus.check_if_uptodate(rm.sentinel_file_exists)
@LogWarnErr(l)
@LogInfo(l)
def file_eater___TASK_1___function(component_name, task_name):
    print '%s for %s started in %s pipeline' % (task_name, component_name, args.pipeline_name)
    run_script = rm.generate_script(__TASK_1___task, None, None)
    job_name = rm.get_filename_prefix(component_name, task_name)
    try:
        ljm.run_job(cmd=run_script, job_name=job_name)
        rm.generate_sentinel_file(component_name, task_name)
    except JobFailureError as e:
        EXIT_CODE = 98
        print >> sys.stderr, 'job {job_id} failed with return code {exit_code} due to error: {err_msg}'.format(**e.__dict__)
    except KeyboardInterrupt:
        raise
    except:
        EXIT_CODE = 98
        traceback.print_exc()

@ruffus.follows(*[file_eater___TASK_1___function, ])
def __last_task___function():
    pass

#================================================================================
#main body
#--------------------------------------------------------------------------------
try:
    if not args.print_only:
        ruffus.pipeline_run(__last_task___function, multiprocess=args.num_jobs, verbose=0)
    else:
        cwd = os.getcwd()
        os.chdir(rm.pipeline_dir)
        ruffus.pipeline_printout_graph(args.pipeline_name + '.' + args.extension, args.extension, [__last_task___function], draw_vertically = args.draw_vertically, no_key_legend = args.no_key_legend, user_colour_scheme = {'colour_scheme_index': 1, 'Pipeline': {'fontcolor': '"#FF3232"'}, 'Task to run': {'linecolor': '"#0044A0"'}, 'Key': {'fontcolor': 'Red', 'fillcolor': '"#F6F4F4"'}, 'Final target': {'fontcolor': 'black', 'fillcolor': '"#EFA03B"', 'dashed': 0}})
        os.chdir(cwd)
    EXIT_CODE = 0

except:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    ##exception object is of type <class 'ruffus.ruffus_exceptions.RethrownJobError'>.
    ##exc_obj.args[0][3] gives the message in the original exception.
    if exc_obj.args[0][3] == '(breakpoint)':
        print 'breakpoint happened in %s pipeline' % (args.pipeline_name)
        ljm.kill_all()
        EXIT_CODE = 99

    else:
        print >> sys.stderr, '{0} pipeline failed due to error: {1}, {2}'.format(args.pipeline_name, exc_type, exc_obj)
        ljm.kill_all()
        EXIT_CODE = -1

finally:
    print '{0} pipeline finished with exit code {1}'.format(args.pipeline_name, EXIT_CODE)
    sys.exit(EXIT_CODE)
