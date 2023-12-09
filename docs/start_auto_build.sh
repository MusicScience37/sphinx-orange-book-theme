#!/bin/bash

set -e

cd $(dirname $0)

./cpp_example/generate_doxygen_xml.sh

# prevent warning.
export PYDEVD_DISABLE_FILE_VALIDATION=1

sphinx-autobuild source build --port 2765
