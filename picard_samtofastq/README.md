#picard_samtofastq

```
Development information

Date created	: Feb 18 2015
Last update	: Mar 4 2015
Developer	: Jasleen Grewal (jkg21@sfu.ca)
Input		: Directory with bam files (.paired.bam, .unpaired.bam)
Output		: Fastq
Parameters	: input_dir, output_dir
		  (for additional optional parameters refer to component_params.py)
Seed used	: picardtools
```
###Dependencies
-picardtools (Tested using v1.71)
-java

###Known issues
- Picard SamToFastq doesnt work if there are unpaired reads in the bam file.
- Need to update component_test.fq to compare output file(s) against expected file(s).
- Currently not processing the .unpaired.bam (i.e. THERE IS NO CHUNK=2)
###Last updates
- Default chunk = 1 currently, which processes Paired reads bam file. 
- Note that the anticipated behaviour for processing unpaired.bam does not work, since the bam read metadata still indicates to SamToFastq that there is a mate around. Thus, currently, if using interval file, please only have 1 entry, namely '1'. If not using interval file, component_main.py is set by default to make_cmd with chunk=1. 
- Currently using input_dir and output_dir. We might wish to revisit this in the future, pass in the input files and output file names ourselves. Currently output for paired bam (infile.paired.bam) is {infile.R1.fq, infile.R2.fq}  
