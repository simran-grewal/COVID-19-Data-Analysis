import subprocess
import os

import numpy as np
import pandas as pd


def get_johns_hopkins():
    git_pull = subprocess.Popen( "/usr/bin/git pull" , 
                     cwd = os.path.dirname( '../data/raw/COVID-19/' ), 
                     shell = True, 
                     stdout = subprocess.PIPE, 
                     stderr = subprocess.PIPE )
    (out, error) = git_pull.communicate()


    print("Error : " + str(error)) 
    print("out : " + str(out))

if __name__ == '__main__':
    get_johns_hopkins()
