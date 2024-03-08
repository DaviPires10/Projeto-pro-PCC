import os
from datetime import datetime
import json


"""
 Get all the files on initialize computer
 Check their existence time
 Remove from server if existence time > 37 days (a month and a week) 
 
 Check if there are new files 
 Add to server
 Repeat same process
 """


path : str = "C:\\Users\\davip\\Animes"
server : str = "./all_files.json"
all_files : dict[str, int] = {}

def get_all_files() -> None:
    for root, dirs, files in os.walk(path):
        for file in files:
            file = os.path.join(root, file)
            all_files[file] = get_existence_time(file)

def get_existence_time(file : str) -> int:
    return (datetime.now() - datetime.fromtimestamp(os.path.getmtime(file))).days


def add_new_file_server(file : str):          
    with open(server) as file:
        files_in_server : dict = json.load(server)
    
        if file not in files_in_server.keys():
            
            # Faça a lógica de colocar o arquivo em si na próprio server
            json.dump(all_files, file)
        

            
#  get_all_files()

  
 
 
  
