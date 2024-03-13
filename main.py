from datetime import datetime
import json
import os


"""
Instructions:

  Get all the files on initialize computer
  Check their existence time
  Remove from server if existence time > 37 days (a month and a week) 
  
  Check if there are new files 
  Add to server
  Repeat same process
  
"""

class Name:
    path : str = "Z:\\"
    server = "Professores"
    profs : list[str] = [
        'Aline', 
        'Anderson', 
        'Edmeire',
        'Michele',
        'Reinaldo V',
        'Ricardo',
        'Tais',
        'Tati',
        'Wellington'
        ]
    
    def __init__(self):
        for prof in self.profs:
            prof_json = self.get_all_files(prof)
            with open(f"{self.server}\\{prof}.json", "w") as file:
                json.dump(prof_json, file, ensure_ascii= False)
    
    def get_all_files(self, prof : str) -> dict:
        prof_json : dict = {}
        
        for root, folders, files in os.walk(f"{self.path}Prof {prof}"):
           
          for folder in folders:
                prof_json[folder] = {folder: dict()}
                
          for file in files:
              
              file = os.path.join(root, file)
              folder = file.split("\\")[-2]
              prof_json[folder][file] = self.get_existence_time(file)
                
        return prof_json
    
    def get_existence_time(file : str) -> int:
        return (datetime.now() - datetime.fromtimestamp(os.path.getmtime(file))).days

    def add_new_file_server(self, file : str):          
        with open(self.server) as file:
            files_in_server : dict = json.load(self.server)
        
            if file not in files_in_server.keys(): {}
                
                # Faça a lógica de colocar o arquivo em si na próprio server
                # json.dump(all_files, file, ensure_ascii= False)