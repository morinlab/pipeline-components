"""
component_test.py

@author: bgrande
"""

import unittest
import shlex
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
                                 "component_reqs: {}".format(var))


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
            cmd_args_split.append(shlex.split(arg))
        all_args = cmd_split + cmd_args_split
        returncode = subprocess.call(all_args)
        self.assertEqual(returncode, 0, "Unsucessful command: {}".format(" ".join(all_args)))

    def test_with_one_fastq_file(self):
        """
        Run bwa_mem with one input FASTQ file.
        """
        args = Arguments(fastq_1="/sample/path/to/fastq_1",
                         reference="/sample/path/to/reference",
                         output_bam="/sample/path/to/output_bam",
                         num_threads="2")
        comp = self.setup_component(args)
        cmd, cmd_args = comp.make_cmd()

    def test_with_two_fastq_files(self):
        """
        Run bwa_mem with two input FASTQ files.
        """
        args = Arguments(fastq_1="/sample/path/to/fastq_1",
                         fastq_2="/sample/path/to/fastq_2",
                         reference="/sample/path/to/reference",
                         output_bam="/sample/path/to/output_bam",
                         num_threads="2")
        comp = self.setup_component(args)
        cmd, cmd_args = comp.make_cmd()
