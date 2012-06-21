#!/bin/bash
# Cut a release to PyPi and update Github with tag.

# Push to PyPi
./setup.py sdist upload

# Tag in Git
git push origin master
git push --tags