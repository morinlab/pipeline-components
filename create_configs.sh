#!/bin/bash

# This script creates single-component pipelines for each component
# in the repository. This way, the YAML configuration is easily
# accessible. 
# 
# Run this script in the repository directory. 
# It assumes that the Pipeline Factory dependencies are already installed.
# Usage: 
# bash create_configs.sh /path/to/python /path/to/factory.py

# Set CWD
CWD=$(pwd)

# Add CWD to PYTHONPATH
export PYTHONPATH="$CWD:$PYTHONPATH"

# Iterate over components
for COMP in $(ls -d */ | grep -v template)
do
	COMP=$(basename $COMP "/")
	cd "$COMP"
	$1 $2 -w . make_config -c component_config $COMP
	cd "$CWD"
done

# Cleanup *.pyc files
find "$CWD" -name "*.pyc" -delete
