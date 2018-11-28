# git_clone_script

Clone all repos related to a user or clone single user repo.

Requirements
Python 3.x, pip

How to run?
Move to <project-dir>, create virtual environment and then activate it as

$ cd <project-dir>

$ virtualenv .environment

$ source .environment/bin/activate
Add project to PYTHONPATH as

$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)
Under <project-dir> install requirements/dependencies as

$ pip install -r requirements.txt
Then run sync.py as

$ python3 script.py -u "git username"

or 
for single directory clone

$ python3 script.py -u "git username" -r "git user repo name"