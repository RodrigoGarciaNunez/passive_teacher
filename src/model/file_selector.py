from random import choice
import sys
import json
import requests




class file_selector():
    def __init__(self):
        pass
        #self.topics =['bash','c++','docker', 'git', 'linux', 'python']
    

    def select_cheatsheet_http(self):
        topics = requests.get("http://files_container/").json()
        #print(type(topics))

        topics= [topic["name"] for topic in topics 
                    if topic["type"] == "directory"]
            

        dir_name = choice(topics)
        
        dir_content = requests.get(f"http://files_container/{dir_name}").json()
        
        files = [file["name"] for file in dir_content 
                if file["type"] == "file" and file["name"].endswith(".pdf")]

        #print(files)
        #sys.stdout.flush()
        choosed_file = choice(files)
        choosed_file_request = requests.get(f"http://files_container/{dir_name}/{choosed_file}")
        
        with open(choosed_file, "wb") as f:
            f.write(choosed_file_request.content)        

        return choosed_file




if __name__ == "__main__":
    fs = file_selector()
    selected_file = fs.select_cheatsheet_http()
    #print(type(selected_file))
    #selected_file = selected_file.tolist()
    json.dump(selected_file, sys.stdout)
