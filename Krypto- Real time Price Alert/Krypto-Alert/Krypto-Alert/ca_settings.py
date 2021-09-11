from os import path

class ca_settings:
    def __init__(self, file):
     
        self.blank_settings()

        if path.exists(file) and path.isfile(file):
            with open(file) as f:
                settings_list = f.read().splitlines()
                self.coin = settings_list[0]
                self.symbol = settings_list[1]
                self.url = settings_list[2]
                self.alert_type = settings_list[3]
                self.alert_sign = settings_list[4]
                self.alert_number = settings_list[5]
                self.sound_status = settings_list[6]
                self.email_status = settings_list[7]
                self.email = settings_list[8]
    
    def get_coin(self):
        return self.coin
    
    def get_symbol(self):
        return self.symbol

    def get_url(self):
        return self.url
    
    def get_alert_type(self):
        return self.alert_type

    def get_alert_sign(self):
        return self.alert_sign

    def get_alert_number(self):
        return self.alert_number
 
    def get_sound_status(self):
        return self.sound_status

    def get_email_status(self):
        return self.email_status

    def get_email(self):
        return self.email

    def get_is_new(self):
        return self.is_new

    def set_is_new(self, status: bool):
        self.is_new = status

    def blank_settings(self):
        self.coin = ""
        self.symbol = ""
        self.url = ""
        self.alert_type = ""
        self.alert_sign = ""
        self.alert_number = 0
        self.sound_status = "False"
        self.email_status = "False"
        self.email = ""
        self.is_new = True

    def new_settings(self, new_coin, new_symbol, new_url, new_alert, new_sign, new_number, new_sstatus, new_estatus, new_email):
        self.coin = new_coin
        self.symbol = new_symbol
        self.url = new_url
        self.alert_type = new_alert
        self.alert_sign = new_sign
        self.alert_number = new_number
        self.sound_status = new_sstatus
        self.email_status = new_estatus
        self.email = new_email
        self.is_new = True
    
    def print_settings(self):
        print(self.coin)
        print(self.symbol)
        print(self.url)
        print(self.alert_type)
        print(self.alert_sign)
        print(self.alert_number)
        print(self.sound_status)
        print(self.email_status)
        print(self.email)