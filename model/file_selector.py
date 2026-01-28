import subprocess
import os
import re
import numpy as np
from random import choice
import sys

class file_selector():
    def __init__(self):
        pass

    def select_cheat_sheet(self):

        path = "/home/rodrigo/Documents/CHEATSHEETS"
        dir = os.listdir(path)
        #print(dir)
        dir = np.array(dir)
        #print(type(dir),  dir)

        pattern_to_exclude= re.compile(r'^[A-Za-z]*\.[A-Za-z]+$')

        dir = self.exclude_files_dirs(dir, pattern_to_exclude)

        #print(dir)


        selected_dir = choice(dir) 
        selected_dir = selected_dir if len(selected_dir) >0 else choice(dir)
        
        #print(selected_dir)

        CHEATS_in_dir = np.array(os.listdir(path+f"/{selected_dir}"))
        #print(CHEATS_in_dir)
        pattern_to_exclude = re.compile(r'^(?!.*\.pdf$).+$')

        CHEATS_in_dir = self.exclude_files_dirs(CHEATS_in_dir, pattern_to_exclude) 

        #print(CHEATS_in_dir)

        return CHEATS_in_dir


    def exclude_files_dirs(self, dir ,pattern_to_exclude):
        return dir[~np.array([bool(pattern_to_exclude.match(s)) for s in dir])]

if __name__ == "__main__":
    fs = file_selector()
    sys.exit(fs.select_cheat_sheet())
