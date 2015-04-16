# file_eater

```
Development Information
=======================

Date Created : Apr 02 2015
Last Update  : Apr 09 2015
Developer    : Jasleen Grewal (jkg21@sfu.ca)
Input Params : input_filenames, out_files
Optional Input: out_dir, in_dir (default './')
Output       : out_dir/results/in_FIRST_FILE_IN_out_FIRST_FILE_OUT_sumin.txt,
               out_dir/results/in_FIRST_FILE_IN_out_FIRST_FILE_OUT_sumout.txt 
Parameters   : filetype_in, filetype_out, delete_input (default 'True')
Seed Used    : count_comparefiles.py, compare_deleteinput.py
```

### Dependencies

- count_comparefiles.py
- compare_deleteinput.py
- samtools (for filetype == bam)

### Known Issues

- None

### Last Updates

- No new updates

### Parameter definitions
input_filenames: List of files (alternatively, a regex - currently identified if including '*' in input_filenames) which were input to a component (or to multiple components)
out_files      : List of files output by a component (or output by multiple components)
It is assumed that by passing in the input_filenames and out_files, the user wishes to compare the total number of reads in the input versus the output.

in_dir         : Define if the input_filenames are located in a different location than the current working directory. 
out_dir        : Define if the out_files are located in a different location than the current working directory.
If in_dir or out_dir are passed, any pathnames in input_filenames or out_files (respectively) are discarded and the file basename retained from the input_filenames, out_files (respectively)

filetype_in    : Either of 'bam' or 'fastq'. Filetype of input_filenames.
filetype_out   : Either of 'bam' or 'fastq'. Filetype of out_files.
 
delete_input   : Either of 'True' or 'False'. Default is 'True'. Deletes the input files if the number of reads in the input = number of reads in the output.
