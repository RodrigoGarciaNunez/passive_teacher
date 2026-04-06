import os
import re
import numpy as np
from random import choice
import sys
import json
import requests




class file_selector():
    def __init__(self):
        self.topics =['bash','c++','docker', 'git', 'linux', 'python']

    # def select_cheat_sheet(self):

     
    #     path = ""

    #     dir = os.scandir(path)
    #     dir = np.array([x.path for x in dir])


    #     pattern_to_exclude= re.compile(r'^.*/\.[^/]+/?$') #excluye directorios con formato '.loquesea' y/o archivos

    #     dir = self.exclude_files_dirs(dir, pattern_to_exclude)

    #     #print(dir)


        

        
    #     while True:
    #         selected_dir = choice(dir)
    #         #print(selected_dir)
    #         scanned_dir = os.scandir(selected_dir)
    #         scanned_dir = np.array([x.path for x in scanned_dir])
    #         #print(len(scanned_dir))
    #         if len(scanned_dir)>0:
    #             break

 
    #     CHEATS_in_dir = np.array([x.path for x in os.scandir(selected_dir)])
        
    #     pattern_to_exclude = re.compile(r'^(?!.*\.pdf$).+$')

    #     CHEATS_in_dir = self.exclude_files_dirs(CHEATS_in_dir, pattern_to_exclude) 

    #     #print(CHEATS_in_dir)

    #     return choice(CHEATS_in_dir)
    

    def select_cheatsheet_http(self):
        random_topic = choice(self.topics)

        r = requests.get(f"http://storage/CHEATSHEETS/{random_topic}/directorio.txt")
        dir = r.text()

        dir_listed = dir.split(',')

        file_choiced = choice(dir_listed)


    def exclude_files_dirs(self, dir ,pattern_to_exclude):
        return dir[~np.array([bool(pattern_to_exclude.match(s)) for s in dir])]

if __name__ == "__main__":
    fs = file_selector()
    selected_dir = fs.select_cheatsheet_http()
    selected_dir = selected_dir.tolist()
    json.dump(selected_dir, sys.stdout)
