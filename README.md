# Pipeline Components

This repository contains components developed by the Morin lab for the Pipeline Factory. 

## Installation

For installing these components, clone this repository and append your `PYTHONPATH` environment variable with the repository directory. 

```bash
git clone https://github.com/morinlab/pipeline-components.git
export PYTHONPATH="$PYTHONPATH:/path/to/pipeline-components"
```

Tags
----

Tags are used to track specific releases/versions of this repository. This allows for reproducibility when using these scripts for projects. This repository adopts the format X.Y (_e.g._ 1.0), where X is the major version and Y is the minor version. When updates are made to existing scripts, increment the minor version number (_e.g._ 1.1). When new scripts are added to the repository, increment the major version (_e.g._ 2.0). 

Here's how to tag commits and push them to GitHub. 

```bash
git tag 1.1
git push --tags
```

And then on another machine, you can checkout that tag as follows. 

```bash
git clone git@github.com:morinlab/pipeline-components.git
cd pipeline-components
git checkout -b tags/1.1 tags/1.1
```
