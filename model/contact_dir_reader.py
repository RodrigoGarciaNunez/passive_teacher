import pandas as pd
import sys 
import json


class directory_reader:
    
    def __init__(self, path_to_contact):
        self.path_to_contact = path_to_contact
        self.direcoty_format = {'ID':False, 'NAME':False ,'TELEFONO':False, 'EMAIL':False}

    def leer_directorio(self):

        try:
            contact_directory = pd.read_excel(self.path_to_contact)
            #print(self.contact_directory.head())
            for key in self.direcoty_format.keys():
                self.direcoty_format[key] = True

            if False in self.direcoty_format.values():
                print('Formato de directorio NO válido', file=sys.stderr)
            
            #print('formato válido')
            #valid = False if False in x else True 
            return contact_directory.to_dict()
        
        except Exception as e:
            print(e)
            #print(f"[XLSX] No se pudo leer ")
            return None
        
            #self.output_text_2.insert(tk.END, f"[XLSX] No se pudo leer {ruta}"


if __name__ == "__main__":
    path_to_contact = sys.argv[1]
    dr = directory_reader(path_to_contact)
    direcotrio = dr.leer_directorio()
    json.dump(direcotrio, sys.stdout)