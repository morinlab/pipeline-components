"""
component_test.py

@author: bgrande
"""

import unittest
import shlex
import random
import os
import filecmp
import subprocess
import component_main
import component_reqs
import component_params


class TestComponentStructure(unittest.TestCase):
    """
    Test whether all the requirements are present.
    """

    def setUp(self):
        self.component = component_main.Component()

    def test_version(self):
        """Test that the versions are specified and consistent."""
        version_in_main = getattr(self.component, "version", None)
        self.assertIsNotNone(version_in_main, "Version not specified in component_main")
        version_in_reqs = getattr(component_reqs, "version", None)
        self.assertIsNotNone(version_in_main, "Version not specified in component_reqs")
        self.assertEqual(version_in_main, version_in_reqs, "Versions disagree between "
                         "component_main and components_reqs")

    def test_requirements(self):
        """Test that all the required variables in component_reqs are present."""
        min_vars = ["env_vars", "memory", "parallel", "requirements", "seed_version", "version"]
        for var in min_vars:
            var_value = getattr(component_reqs, var, None)
            self.assertIsNotNone(var_value, "Required variable not set in "
                                 "component_reqs: {}".format(var))

    def test_params(self):
        """Test that all the required variables in component_params are present."""
        min_vars = ["input_files", "output_files", "input_params", "return_value"]
        for var in min_vars:
            var_value = getattr(component_params, var, None)
            self.assertIsNotNone(var_value, "Required variable not set in "
                                 "component_params: {}".format(var))


class Arguments(object):
    """
    Creates namespace with provided keyword arguments.
    """

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class TestSeed(unittest.TestCase):
    """
    Test the seed by running it with some sample data
    and comparing the output with what's expected.
    The functions in component_main are tested as well.
    """

    def setUp(self):
        """
        Set a few common variables.
        """
        # Obtain component_test directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.test_dir = current_dir + "/component_test/"
        # Create a tmp directory
        comp = component_main.Component()
        random_num = int(random.random() * 1000)
        self.tmp_dir = "/tmp/test_{}_{}/".format(comp.component_name, random_num)
        os.mkdir(self.tmp_dir)

    def setup_component(self, args):
        """
        Create uniform Component instances.
        """
        component = component_main.Component()
        component.requirements = component_reqs.requirements
        component.args = args
        return component

    def run_cmd(self, cmd, cmd_args):
        """
        Build and run commands based on cmd and cmd_args.
        Also checks for status_code.
        """
        cmd_split = shlex.split(cmd)
        cmd_args_split = []
        for arg in cmd_args:
            cmd_args_split.extend(shlex.split(arg))
        all_args = cmd_split + cmd_args_split
        returncode = subprocess.call(subprocess.list2cmdline(all_args), shell=True,
                                     stderr=subprocess.PIPE)
        self.assertEqual(returncode, 0, "Unsucessful command: {}".format(" ".join(all_args)))

    def compare_files(self, comp, expectations={}):
        """
        Given a set of expectations, this method raises
        an exception when an actual output file doesn't
        match the expected output file.
        The expectations dictionary is a set of key-value
        pairs, where the key is the component argument of
        the output file and the value is the expected
        output file (such as one in component_test)
        """
        for arg, expected_filename in expectations.items():
            actual_filename = getattr(comp.args, arg)
            # Remove header line with BWA command
            # Because it prevents two files from being identical otherwise
            actual_filename_fixed = self.fix_bam_file(actual_filename)
            is_equal = filecmp.cmp(actual_filename_fixed, expected_filename)
            self.assertTrue(is_equal, "Actual output file differs from expected output file."
                            "\nActual: {}\nExpected: {}".format(actual_filename_fixed,
                                                                expected_filename))

    def fix_bam_file(self, bam_file):
        """
        Remove the @PG header line from BAM file
        and return resulting file.
        """
        prefix, ext = os.path.splitext(bam_file)
        output_bam = prefix + ".fixed." + ext
        with open(bam_file) as inbam, open(output_bam, "w") as outbam:
            for line in inbam:
                if line.startswith("@PG"):
                    continue
                outbam.write(line)
        return output_bam

    def test_with_one_fastq_file(self):
        """Run bwa_mem with one input FASTQ file."""
        args = Arguments(
            fastq_1="{}/phix_reads_R1.fastq.gz".format(self.test_dir),
            reference="{}/bwa_index/phix_genome.fasta".format(self.test_dir),
            output_bam="{}/phix_alignment_with_one_fastq_file.sam".format(self.tmp_dir),
            num_threads="2")
        comp = self.setup_component(args)
        cmd, cmd_args = comp.make_cmd()
        self.run_cmd(cmd, cmd_args)
        expectations = {
            "output_bam": "{}/phix_alignment_with_one_fastq_file.sam".format(self.test_dir)}
        self.compare_files(comp, expectations)

    def test_with_two_fastq_files(self):
        """Run bwa_mem with two input FASTQ files."""
        args = Arguments(
            fastq_1="{}/phix_reads_R1.fastq.gz".format(self.test_dir),
            fastq_2="{}/phix_reads_R2.fastq.gz".format(self.test_dir),
            reference="{}/bwa_index/phix_genome.fasta".format(self.test_dir),
            output_bam="{}/phix_alignment_with_two_fastq_files.sam".format(self.tmp_dir),
            num_threads="2")
        comp = self.setup_component(args)
        cmd, cmd_args = comp.make_cmd()
        self.run_cmd(cmd, cmd_args)
        expectations = {
            "output_bam": "{}/phix_alignment_with_two_fastq_files.sam".format(self.test_dir)}
        self.compare_files(comp, expectations)


def run_tests():
    """
    Run all tests.
    """
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestComponentStructure)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSeed)
    alltests_suite = unittest.TestSuite([suite1, suite2])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(alltests_suite)
