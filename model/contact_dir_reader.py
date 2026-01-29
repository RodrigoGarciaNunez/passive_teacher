import pandas as pd
import sys 
import json


class directory_reader:
    
    def __init__(self, path_to_contact):
        self.path_to_contact = path_to_contact
        self.direcoty_format = ['ID', 'NAME', 'TELEFONO', 'EMAIL']

    def leer_directorio(self):

        self.contact_directory = pd.read_excel(self.path_to_contact)

        try:
            pass
            
        except Exception as e:
            print(e)
            print(f"[XLSX] No se pudo leer ")
            #self.output_text_2.insert(tk.END, f"[XLSX] No se pudo leer {ruta}")

        return "hola"


if __name__ == "__main__":
    path_to_contact = sys.argv[1]
    dr = directory_reader(path_to_contact)
    json.dump(dr.leer_directorio(), sys.stdout)