from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import sys
from random import choice
from json import JSONDecodeError, loads
import pandas as pd

class sender():

    def __init__(self, directory:dict, message:str, file:str):

        self.dir = directory
        self.mensaje = message

        options = Options()
        options.binary_location = "/usr/bin/brave-browser"
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="143.0.7499.110").install()), options=options)

        

        # self.file = os.path.abspath(
        #     os.path.join(os.path.dirname(__file__), "../test_resourses", "mc.jpg"))

        #print(self.file)


        def send_Message(self):
            pass
            
       



class WA_sender(sender):

    def __init__(self, directory:dict, message:str, file:str):
        super().__init__(directory, message, file)

        self.driver.get("https://web.whatsapp.com")

        try:
            WebDriverWait(self.driver, 300).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='grid']")))
            print("✅ Sesión iniciada correctamente.")
        except:
            print("⏰ Tiempo de espera agotado. No se detectó el inicio de sesión.")
            self.driver.quit()
            exit()


    def send_Message(self):
        #mensaje = "Hola!"
        
        for contacto in self.dir:
            self.find_contact(contacto)
            self.add_message(contacto)
            self.add_file()
        
        # cierra sesión
        self.driver.quit()


    
    def find_contact(self, contacto):
        try:
            print(contacto)
            search_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='3']")))
                
            search_box.click()
            search_box.send_keys(self.dir[contacto][1])
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)
        except Exception as e:
            print("algo salio mal buscando el contacto")



    def add_message(self, contacto):

        if self.mensaje == "":
            return
        
        msg_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10'][role='textbox']")))
            
        msg_box.click()
        msg_box.send_keys(self.mensaje)
        msg_box.send_keys(Keys.ENTER)

        print(f"✅ Mensaje enviado a {contacto}: {dir[contacto][1]}.")
        time.sleep(3)

    def add_file(self):
        
        if self.file == "":
            return

            # 1️⃣ Abrir el botón del clip
        clip_btn = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='plus-rounded']" )))
    
        clip_btn.click()

            # 2️⃣ Localizar el input file

        file_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

            # file_input = wait.until(EC.presence_of_element_located(
            #     (By.CSS_SELECTOR, "input[type='file']")
            # ))

            # 3️⃣ Enviar la ruta del archivo (ABSOLUTA)
        file_input.send_keys(self.file)

            # 4️⃣ Esperar botón de enviar y hacer click

        send_btn = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='wds-ic-send-filled']" )))

            # send_btn = wait.until(EC.element_to_be_clickable(
            #     (By.CSS_SELECTOR, "span[data-icon='send']")
            # ))
        send_btn.click()




if __name__ =="__main__":
    print('---------ENVIANDO MENSAJE ---------')
    random_cheatsheet =loads(sys.argv[1])
    random_cheatsheet = choice(random_cheatsheet)
    print('file' ,type(random_cheatsheet), random_cheatsheet)
    
    contact = sys.argv[2]
    #contact = cleans_json(contact)
    print('directorio',contact)

    if type(contact) is int():
        print('soy int')
    
    try: 
        contact = loads(contact)
        print('contacto parseado', type(contact), contact)
    except JSONDecodeError as e:
        print(e, "Error al parsear directorio")


    snd = WA_sender(contact, "Esto es una prueba", random_cheatsheet)
    snd.send_Message()


    


  


