import numpy as np
import math
import random
import itertools
import sys
import pylab
import os
import csv

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")


fileDir = os.path.dirname(os.path.realpath(__file__))
dataDir = os.path.join(fileDir, "dataset")