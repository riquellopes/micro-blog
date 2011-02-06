import os
import sys


# add lib in PYTHONPATH

path_lib = os.getcwd().replace('/tests', '/lib')
sys.path.append(path_lib)

