from model.file_selector import file_selector
from model.sender import sender
from datetime import datetime

import gc


class passive_teacher():

    def __init__(self):
        gc.enable()
        self.clock = datetime.now()
        self.reminder_sent_flag = False
        


    def checking_time(self):
        while self.reminder_sent_flag == False:
            if self.clock.hour > 17:
                self.reminder_sent_flag = True
                print("mensaje enviado")
                return
            
            self.clock = datetime.now()


        