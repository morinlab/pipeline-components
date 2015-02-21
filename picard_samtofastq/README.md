#picard_samtofastq

```
Development information

Date created	: Feb 18 2015
Last update	: Feb 18 2015
Developer	: Jasleen Grewal (jkg21@sfu.ca)
Input		: bam file
Output		: Fastq
Parameters	: input.file, fastq.output.file1 
		  (for additional optional parameters refer to component_params.py)
Seed used	: picardtools
```
###Dependencies
-picardtools (Tested using v1.71)
-java

###Known issues
- Picard SamToFastq doesnt work if there are unpaired reads in the bam file.
- Need to update component_test.fq to compare output file(s) against expected file(s).
###Last updates


