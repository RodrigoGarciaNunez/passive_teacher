from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import sys
from random import choice
from json import JSONDecodeError, loads
import pandas as pd
from dataclasses import dataclass

import fitz # PyMuPDF
from PIL import Image
from image_manager import image_manager



@dataclass
class WA_selectors():
    session_init_selector = "div[role='grid']"
    contact_search_box_selector= "div[contenteditable='true'][data-tab='3']"
    msg_box_selector = "div[contenteditable='true'][data-tab='10'][role='textbox']"
    clip_btn_selector = "span[data-icon='plus-rounded']"
    file_input_selector = "input[type='file']"
    send__file_btn_selector = "span[data-icon='wds-ic-send-filled']" 




class sender():

    def __init__(self, directory:dict, message:str, file:str):

        self.dir = directory
        self.mensaje = message
        self.file = file

        options = Options()
        options.binary_location = "/usr/bin/brave-browser"
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="143.0.7499.110").install()), options=options)

        self.image_manager = image_manager()        

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
                EC.presence_of_element_located((By.CSS_SELECTOR, WA_selectors.session_init_selector)))
            print("✅ Sesión iniciada correctamente.")
            time.sleep(5)
        except:
            print("⏰ Tiempo de espera agotado. No se detectó el inicio de sesión.")
            self.driver.quit()
            exit()


    def send_Message(self):
        #mensaje = "Hola!"
        
        for contacto, num in zip(self.dir['ID'].values(),self.dir['TELEFONO'].values()):
            self.find_contact(num)
            self.add_message(contacto, num)
            self.add_file_copied()
        
        # cierra sesión
        self.driver.quit()


    
    def find_contact(self,num):
        try:
            #print(contacto)
            search_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WA_selectors.contact_search_box_selector)))
                
            search_box.click()
            #print(num)
            search_box.send_keys(num)
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)
        except Exception as e:
            print("algo salio mal buscando el contacto", e)



    def add_message(self, contacto, num):

        if self.mensaje == "":
            return

        try: 

            msg_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WA_selectors.msg_box_selector)))
                
            msg_box.click()
            msg_box.send_keys(self.mensaje)
            msg_box.send_keys(Keys.ENTER)

            print(f"\n✅ Mensaje enviado a {contacto}: {num}.")
        except Exception as e:
            print(e, "\n NO SE PUDO ENVIAR EL MENSAJE")
            exit()

        time.sleep(3)

    def add_file(self):
        
        if self.file == "":
            return
    
        try:

                # 1 Abrir el botón del clip
            clip_btn = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WA_selectors.clip_btn_selector)))
        
            clip_btn.click()

                # 2 Localizar el input file

            file_input = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WA_selectors.file_input_selector)))

            

                # 3 Enviar la ruta del archivo (ABSOLUTA)
            file_input.send_keys(self.file)

                # 4 Esperar botón de enviar y hacer click

            send_btn = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WA_selectors.send__file_btn_selector)))
            
            time.sleep(2)

            send_btn.click()

            print("✅ Archivo enviado!")
        
        except Exception as e:
            print(e, "NO SE PUDO ENVIAR EL ARCHIVO")
            exit()


    def add_file_copied(self):
        
        try:
            
            msg_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WA_selectors.msg_box_selector)))
                
            msg_box.click()

            image_2_copy = self.image_manager.converts_pdf2jpg(self.file)
            self.image_manager.copy_image_2_clipboard(image_2_copy)
            
            # ctrl + v 
            #ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

            msg_box.send_keys(Keys.CONTROL, 'v')


            send_btn = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WA_selectors.send__file_btn_selector)))
            
            time.sleep(2)

            send_btn.click()
            #msg_box.send_keys(Keys.ENTER)

            print(f"\n✅ Imágen enviada")


        except Exception as e:
            print(e, 'No se pudo copiar la imágen')



if __name__ =="__main__":
    print('---------ENVIANDO MENSAJE ---------')
    random_cheatsheet =loads(sys.argv[1])
    #random_cheatsheet = choice(random_cheatsheet)
    print('file' ,type(random_cheatsheet), random_cheatsheet)
    
    #mrg = image_manager(random_cheatsheet)
    #random_cheatsheet = converts_pdf2jpg(random_cheatsheet)

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

    #print(contact['TELEFONO']['1'])

    # for cont in contact['TELEFONO'].values():
    #     print(cont,'va una') 
    snd = WA_sender(contact, "Esto es una prueba", random_cheatsheet)
    snd.send_Message()


    


  


