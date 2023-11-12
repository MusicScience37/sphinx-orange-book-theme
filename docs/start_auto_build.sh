#!/bin/bash

set -e

cd $(dirname $0)

sphinx-autobuild source build --port 2765
