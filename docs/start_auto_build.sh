#!/bin/bash

set -e

cd $(dirname $0)

./cpp_example/generate_doxygen_xml.sh

sphinx-autobuild source build --port 2765
