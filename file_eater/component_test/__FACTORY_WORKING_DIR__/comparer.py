#================================================================================
#config file content
#--------------------------------------------------------------------------------
config_file_content = '''
__PIPELINE_INFO__: 
    name: 
    version: 
    author: 
    data_type: 
    input_type: 
    output_type: 
    host_cluster: 
    date_created: 
    date_last_updated: 
    factory_version: '1.10.2'
__GENERAL__: 
    python:  '/extscratch/morinlab/projects/MCL_realignment/software/python'
    samtools: '/extscratch/morinlab/projects/MCL_realignment/software/samtools/samtools'
__SHARED__: 
__SAMPLES__: 
    PT004:
       orig_bam: '/extscratch/morinlab/projects/MCL_realignment/data/PT004_tumour_sub0.01.bam'
       paired_bam: '/extscratch/morinlab/projects/MCL_realignment/results/mytestdir/20150409104727/PT004_Tumor_bam_to_fastq_dev/outputs/TASK_MERGE_PAIRED_BAM_PT004_Tumor.pairedreads.bam'
       unpaired_bam: '/extscratch/morinlab/projects/MCL_realignment/results/mytestdir/20150409104727/PT004_Tumor_bam_to_fastq_dev/outputs/TASK_FILTER_UNPAIRED_BAM_PT004_Tumor.unpaired.clean.bam' 
__TASK_1__: 
    reserved: 
        # do not change this section.
        component_name: 'file_eater'
        component_version: '1.5.0'
        seed_version: '1.00.0'
    run: 
        # NOTE: component cannot run in parallel mode.
        use_cluster: False
        memory: '1G'
        num_cpus: 1
        forced_dependencies: []
        add_breakpoint: False
        env_vars: 
        boilerplate: 
    component: 
        input_files: 
            out_files:
                 ("__SAMPLES__","orig_bam"),
                 ("__SAMPLES__","paired_bam"),
            input_filenames: 
               ("__SAMPLES__","paired_bam")
               ("__SAMPLES__","unpaired_bam")
               ("__SAMPLES__","paired_bam")
        output_files: 
        parameters: 
            filetype_in: 'bam'
            filetype_out: 'bam'
'''

#================================================================================
#import modules
#--------------------------------------------------------------------------------
import sys
from pipeline_factory.helpers import make_dir, kill_jobs, flushqueue, make_intermediate_cmd_args, KeywordsManager
import ruffus
import pipeline_factory.pipelineui
from datetime import datetime
import os
from multiprocessing import Queue
from pipeline_factory.logger import PipelineLogger, LogWarnErr, LogInfo
import subprocess

#================================================================================
#argument validation
#--------------------------------------------------------------------------------
job_ids = Queue()
job_rcs = Queue()
rc = 0
args = pipeline_factory.pipelineui.args

args.components_dir = os.path.abspath(args.components_dir)

if args.pipeline_name is None:
    pipeline_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]

else:
    pipeline_name = args.pipeline_name

if args.run_id is None:
    run_id = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

else:
    run_id = args.run_id

make_dir(args.working_dir)
args.working_dir = os.path.join(args.working_dir, run_id)
make_dir(args.working_dir)

if args.log_file is None:
    log_file = os.path.join(args.working_dir, '_'.join([pipeline_name, run_id]) + '.log')

else:
    log_file = os.path.join(args.working_dir, '_'.join([args.log_file, run_id]) + '.log')

#================================================================================
#make a copy of the config file
#--------------------------------------------------------------------------------
cfile = os.path.join(args.working_dir, pipeline_name + '_' + run_id + '.yaml')
with open(cfile, 'w') as cf:
    cf.write(config_file_content)

#================================================================================
#limit the maximum number of simultaneous jobs
#--------------------------------------------------------------------------------
max_num_total = 104
max_num_pips = 4
max_num_jobs = int(max_num_total / max_num_pips)
if args.num_pipelines > max_num_pips:
    args.num_pipelines = max_num_pips
if args.num_jobs > max_num_jobs:
    args.num_jobs = max_num_jobs
#================================================================================
#logger initialization
#--------------------------------------------------------------------------------
pl = PipelineLogger(args.verbose)
l = pl.get_logger(pipeline_name, log_file)
pl.log_pipeline_header(l, args, pipeline_name, run_id)

args = vars(pipeline_factory.pipelineui.args)

#================================================================================
#ruffus pipeline
#--------------------------------------------------------------------------------
@ruffus.follows()
@LogWarnErr(l)
@LogInfo(l)
def task_0(pipeline_name='PT004_comparer'):
    sample_id = 'PT004'
    intermediate_path = os.path.join(os.path.dirname(sys.argv[0]),'intermediate_pipeline_scripts')
    pipeline_script = '{0}/{1}.py'.format(intermediate_path, pipeline_name)

    args['pipeline_name'] = pipeline_name
    args['run_id'] = run_id
    args['sample_id'] = sample_id
    args['log_file'] = log_file

    km = KeywordsManager(pipeline_name, run_id, sample_id, args['working_dir'])
    old_script_content = open(pipeline_script, 'r').read()
    new_script_content = km.replace_keywords(old_script_content)
    f = open(pipeline_script, 'w')
    f.write(new_script_content)
    f.close()

    cmd = '{0} {1}'.format(args['python_installation'], pipeline_script)
    cmd_args = make_intermediate_cmd_args(args)
    cmd = cmd + ' ' + ' '.join(cmd_args)
    print 'running PT004_comparer pipeline with command: %s' % (cmd)

    proc = subprocess.Popen(cmd, shell=True)
    job_ids.put(proc.pid)
    cmdout, cmderr = proc.communicate()
    job_rcs.put(proc.returncode)
    print 'PT004_comparer pipeline finished with exit code %s' % (proc.returncode)

    if cmdout is not None:
        print >> sys.stdout, cmdout

    if cmderr is not None:
        print >> sys.stderr, cmderr

#================================================================================
#running pipeline
#--------------------------------------------------------------------------------
try:
    ruffus.pipeline_run([task_0], multiprocess=args['num_pipelines'])
    lrc = flushqueue(job_rcs)
    if len(lrc) == len(filter(lambda x: x == 99, lrc)):
        print 'pipeline successfully stopped by breakpoints.'
        rc = 99
    elif not all(rc == 0 for rc in lrc):
        rc = 98

except:
    rc = -1
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print >> sys.stderr, '{0} pipeline failed due to error: {1}, {2}'.format(pipeline_name, exc_type, exc_obj)
    kill_jobs(job_ids)

finally:
    pl.log_pipeline_footer(l)
    pl.log_info(l, '{0} pipeline finished with exit code {1}. Please check the logs.'.format(pipeline_name, rc))
    sys.exit(rc)

