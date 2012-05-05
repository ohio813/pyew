#!/usr/bin/env python

import os

CODE_ANALYSIS=True
DEEP_CODE_ANALYSIS=False
CONFIG_ANALYSIS_TIMEOUT=0
PLUGINS_PATH=os.path.dirname(__file__) + os.sep + "plugins"
DATABASE_PATH=os.path.dirname(__file__) + os.sep + "files.sqlite"

# Experimental: when DEEP_CODE_ANALYSIS is True, this experimental feature
# can be enabled. It tries to find new functions starting at the end address
# of currently known functions
ANALYSIS_FUNCTIONS_AT_END=True
