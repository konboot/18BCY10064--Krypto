#Haiden Gembinski
#GUI class for Krypto

import os
import tkinter
from tkinter import *
from tkinter import font
import tkinter.font
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from time import localtime, strftime
from datetime import date

import ca_helpers
from ca_helpers import *
import ca_scraping
from ca_scraping import *

class ca_gui:
    def __init__(self, master, settings):
        #GUI setup
        self.master = master
        master.title('Krypto')
        master.geometry('700x750')
        master.resizable(False, False)
        master.config(bg = 'white', highlightbackground = '#000F46', highlightcolor = '#000F46', highlightthickness = 10)

        self.title = Label(master, text = 'Krypto', bg = '#000F46', fg = 'white', width = 12,
                    font = (None, 40)).place(x = 350, y = 50, anchor = 's')
        self.crypto_name = Label(master, text = 'No Coin Selected', bg = 'white', fg = '#000F46', font = (None, 35, 'bold'))
        self.crypto_name.place(x = 350, y = 115, anchor = 'center')

        #price ticker
        self.priceframe = Frame(master, bg = 'grey9', highlightbackground = '#004ac2', highlightcolor = '#004ac2',
                    highlightthickness = 15, relief = 'flat', height = 200, width = 500).place(x = 350, y = 275, anchor = 'center')
        self.price_font = font.Font(size = 5)
        self.price = Label(master, text = '$0000.00', bg = 'grey9', fg = 'grey9', font = self.price_font)
        self.price.place(x = 350, y = 275, anchor = 'center')
        master.update()

        #alert display
        self.alert_display = Label(master, bg = 'white', fg = '#000F46',font = (None, 25))
        self.alert_display.place(x = 350, y = 425, anchor = 'center')
                    
        self.sound_display = Label(master, bg = 'white', fg = '#000F46',font = (None, 25))
        self.sound_display.place(x = 350, y = 475, anchor = 'center')

        self.email_display = Label(master, bg = 'white', fg = '#000F46', font = (None, 25))
        self.email_display.place(x = 350, y = 525, anchor = 'center')

        self.email_address_display = Label(master, bg = 'white', fg = '#000F46',font = (None, 20))
        self.email_address_display.place(x = 350, y = 565, anchor = 'center')

        #buttons
        self.settings_button = Button(self.master, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', 
                    activeforeground = 'antiquewhite1', text = 'Settings', relief = 'raised', width = 10, font = (None, 30, 'bold'), 
                    command = lambda: self.show_settings_screen(master, settings))
        self.settings_button.place(x = 500, y = 650, anchor = 'center')

        self.history_button = Button(self.master, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', 
                    activeforeground = 'antiquewhite1', text = 'History', relief = 'raised', width = 10, font = (None, 30, 'bold'),
                    command = lambda: self.show_history_screen(master))
        self.history_button.place(x = 200, y = 650, anchor = 'center')

        self.default_display()

    def set_crypto(self, new_name):
        self.crypto_name.config(text = new_name)

    def set_price(self, new_price):
        self.price.config(text = new_price)

    def set_price_color(self, color):
        self.price.config(fg = color)
        
    def set_alert_text(self, new_text):
        self.alert_display.config(text = new_text)

    def set_sound_alert_text(self, new_text):
        self.sound_display.config(text = new_text)

    def set_email_alert_text(self, new_text):
        self.email_display.config(text = new_text)

    def set_email_text(self, new_text):
        self.email_address_display.config(text = new_text)

    def get_font(self):
        return self.price_font

    def set_font_size(self, new_size):
        self.price_font.config(size = new_size)

    def get_price_label(self):
        return self.price

    def default_display(self):
        self.set_crypto('No Coin Selected')
        self.set_price('')
        self.set_alert_text('No alert set!')
        self.set_sound_alert_text('')
        self.set_email_alert_text('')
        self.set_email_text('')    

    def show_settings_screen(self, master, settings):
        #construct dict of coins
        csv_file = 'cryptos.csv'
        coin_dict = csv_to_dict(csv_file)
        coin_list = []
        for key in coin_dict.keys():
            coin_list.append(coin_dict[key][0] + ' - ' + key)
        
        if list(coin_dict.keys())[0] == 'Update to load list of coins!':
            coin_name = 'Update to load list of coins!'

        elif settings.get_coin() != '': #for displaying coin in combobox entry field
            coin_name = settings.get_symbol() + ' - ' + settings.get_coin()
            
        else:
            coin_name = ''

        #GUI
        settings_gui = tkinter.Toplevel(master)
        settings_gui.title('Krypto Settings')
        settings_gui.resizable(False, False)
        settings_gui.grab_set()

        x = master.winfo_x()
        y = master.winfo_y()
        h = master.winfo_height()
        w = master.winfo_width()
        settings_gui.geometry('%dx%d+%d+%d' % (w, h, x, y))
        settings_gui.config(bg = 'white', highlightbackground = '#000F46', highlightcolor = '#000F46', highlightthickness = 10)

        #title
        title = Label(settings_gui, text = 'Settings', bg = '#000F46', fg = 'white', width = 12,
                    font = (None, 40)).place(x = 350, y = 50, anchor = 's')

        #drop down list
        list_title = Label(settings_gui, text = 'Select Coin To Track ', bg = 'white', fg = '#000F46',
                    font = (None, 25)).place(x = 350, y = 75, anchor = 'center')
        list_font = font.Font(None, 25)
        settings_gui.option_add('*TCombobox*Listbox*Font', list_font)
        cryptos = AutocompleteCombobox(settings_gui, width = 30, font = (None, 15), completevalues = coin_list)
        cryptos.place(x = 350, y = 125, anchor = 'center')
        cryptos.set(coin_name)

        #update button
        update = Button(settings_gui, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                    text = 'Update', relief = 'raised', width = 6, font = (None, 15, 'bold'), command = lambda: self.update_screen(master, cryptos))
        update.place(x = 600, y = 125, anchor = 'center')

        #alert options
        alert_price_text = Label(settings_gui, text = 'When the price...', bg = 'white', fg = '#000F46',
                    font = (None, 30, 'italic')).place(x = 150, y = 160)
        changes_text = Label(settings_gui, text = 'Changes by ', bg = 'white', fg = '#000F46',
                    font = (None, 22)).place(x = 250, y = 225)
        changes_percent = Label(settings_gui, text = '%', bg = 'white', fg = '#000F46',
                    font = (None, 22)).place(x = 490, y = 225)
        changes_number = Entry(settings_gui, font = (None, 20), width = 4, relief = 'sunken')
        changes_number.place(x = 425, y = 227)
        if settings.get_alert_type() == 'Percent':
            changes_number.insert(0, settings.get_alert_number())

        is_text = Label(settings_gui, text = 'Is ', bg = 'white', fg = '#000F46',
                font = (None, 22)).place(x = 250, y = 292)
        is_choices = ['<', '>']
        is_choice_dropdown = AutocompleteCombobox(settings_gui, width = 2, font = (None, 20), justify = 'center',
                    completevalues = is_choices, state = 'readonly')
        is_choice_dropdown.place(x = 300, y = 294)
        if settings.get_alert_sign() != 'N/A':
            is_choice_dropdown.set(settings.get_alert_sign())
        than_text = Label(settings_gui, text = 'than', bg = 'white', fg = '#000F46',
                justify = 'center', font = (None, 22))
        than_text.place(x = 375, y = 292)

        is_sign = Label(settings_gui, text = '$', bg = 'white', fg = '#000F46',
                font = (None, 22)).place(x = 450, y = 292)
        is_number = Entry(settings_gui, font = (None, 20), width = 8, relief = 'sunken')
        is_number.place(x = 475, y = 294)
        if settings.get_alert_type() == 'Flat':
            is_number.insert(0, settings.get_alert_number())

        #alert type configurations
        alert_config_text = Label(settings_gui, text = 'Alert me by...', bg = 'white', fg = '#000F46',
                font = (None, 30, 'italic')).place(x = 150, y = 365)
        sound_alert_text = Label(settings_gui, text = 'Playing a sound!', bg = 'white', fg = '#000F46',
                    font = (None, 22)).place(x = 250, y = 425)

        email_alert_text = Label(settings_gui, text = 'Sending me an email!', bg = 'white', fg = '#000F46',
                    font = (None, 22)).place(x = 250, y = 490)
        email_address = Entry(settings_gui, font = (None, 20), relief = 'sunken')
        email_address.place(x = 250, y = 530)
        if settings.get_email() != 'N/A':
            email_address.insert(0, settings.get_email())

        #toggles
        #price 'changes by' toggle
        price_changes_by = Canvas(settings_gui, bg = 'light grey', borderwidth = 0, 
                    highlightthickness = 5, highlightbackground = 'light grey', width = 25, height = 25) #default on display
        price_changes_by.place(x = 200, y = 225)
        if settings.get_alert_type() == 'Percent':
            price_changes_by.config(bg = '#000F46')


        #price 'is' toggle
        price_is = Canvas(settings_gui, bg = 'light grey', borderwidth = 0, 
                    highlightthickness = 5, highlightbackground = 'light grey', width = 25, height = 25)
        price_is.place(x = 200, y = 292)
        if settings.get_alert_type() == 'Flat':
            price_is.config(bg = '#000F46')

        #alert 'play sound' toggle
        play_sound = Canvas(settings_gui, bg = 'light grey', borderwidth = 0, 
                    highlightthickness = 5, highlightbackground = 'light grey', width = 25, height = 25)
        play_sound.place(x = 200, y = 425)
        if settings.get_sound_status() == 'True':
            play_sound.config(bg = '#000F46')

        #'send email' toggle
        send_email = Canvas(settings_gui, bg = 'light grey', borderwidth = 0, 
                    highlightthickness = 5, highlightbackground = 'light grey', width = 25, height = 25)
        send_email.place(x = 200, y = 490)
        if settings.get_email_status() == 'True':
            send_email.config(bg = '#000F46')

        #toggle events
        def changes_by_toggle(event):
            if price_changes_by['background'] == 'light grey':
                price_changes_by.config(bg = '#000F46')
                price_is.config(bg = 'light grey')
            else:
                price_changes_by.config(bg = 'light grey')
        price_changes_by.bind('<Button-1>', changes_by_toggle)

        def is_toggle(event):
            if price_is['background'] == 'light grey':
                price_is.config(bg = '#000F46')
                price_changes_by.config(bg = 'light grey')
            else:
                price_is.config(bg = 'light grey')
        price_is.bind('<Button-1>', is_toggle)

        def sound_alert_toggle(event):
            if play_sound['background'] == 'light grey':
                play_sound.config(bg = '#000F46')
            else:
                play_sound.config(bg = 'light grey')
        play_sound.bind('<Button-1>', sound_alert_toggle)

        def email_alert_toggle(event):
            if send_email['background'] == 'light grey':
                send_email.config(bg = '#000F46')
            else:
                send_email.config(bg = 'light grey')
        send_email.bind('<Button-1>', email_alert_toggle)

        #confirm button
        confirm = Button(settings_gui, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                text = 'Confirm', relief = 'raised', width = 10, font = (None, 30, 'bold'), 
                command = lambda: settings_confirm())
        confirm.place(x = 500, y = 650, anchor = 'center')

        #Settings confirm function
        def settings_confirm():
            settings_file = 'settings.txt'
            name = cryptos.get().split(' - ', 1) #split out the coin name, 2nd element is the 'spelled out' name of the coin
            if len(name) > 1 and name[1] in coin_dict.keys() and name[1]!= 'Update to load list of coins!':
                coin = name[1]
                symbol = coin_dict[name[1]][0]
                url = coin_dict[name[1]][1]
            else:
                message = 'Invalid coin, please try again.'
                show_error_screen(settings_gui, message)
                return

            if price_changes_by['background'] == '#000F46':
                alert_type = 'Percent'
                alert_sign = 'N/A'
                try:
                    check = float(changes_number.get())
                except ValueError:
                    message = '"Changes by" value must be a valid number between 0 and 1000, please try again.'
                    show_error_screen(settings_gui, message)
                    return
                if float(changes_number.get()) >= 0 and float(changes_number.get()) < 1000:
                    alert_number = changes_number.get()
                else:
                    message = ' "Changes by" value must be a valid number between 0 and 1000, please try again.'
                    show_error_screen(settings_gui, message)
                    return

            elif price_is['background'] == '#000F46':
                alert_type = 'Flat'
                alert_sign = is_choice_dropdown.get()
                if alert_sign != '<' and alert_sign != '>':
                    message = 'Please choose a value sign for the alert.'
                    show_error_screen(settings_gui, message)
                    return
                try:
                    check = float(is_number.get())
                    if check < 0:
                        message = 'Alert price must be a valid number greater than 0, please try again.'
                        show_error_screen(settings_gui, message)
                        return
                    alert_number = is_number.get()
                except ValueError:
                    message = 'Alert price must be a valid number greater than 0, please try again.'
                    show_error_screen(settings_gui, message)
                    return
            else:
                message = 'Please choose an alert type.'
                show_error_screen(settings_gui, message)
                return

            if play_sound['background'] == '#000F46':
                is_sound = 'True'
            else:
                is_sound = 'False'
            
            if send_email['background'] == '#000F46':
                is_email = 'True'
                test_email = email_address.get()
                if (check_email(test_email)):
                    email = email_address.get()
                else:
                    message = 'Please enter a valid email, such as "example@website.com"'
                    show_error_screen(settings_gui, message)
                    return
            else:
                is_email = 'False'
                email = 'N/A'

            #save to file   
            with open(settings_file, 'w') as f:
                f.write(str(coin) + '\n' + symbol + '\n' + url + '\n' + str(alert_type) + '\n' + str(alert_sign) 
                + '\n' + str(alert_number) + '\n' + str(is_sound) + '\n' + str(is_email) + '\n' + str(email))

            #set the settings object values accordingly
            settings.new_settings(coin, symbol, url, alert_type, alert_sign, alert_number, is_sound, is_email, email)

            settings_gui.destroy()

        #cancel button
        cancel = Button(settings_gui, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                    text = 'Cancel', relief = 'raised', width = 10, font = (None, 30, 'bold'), command = lambda: settings_cancel())
        cancel.place(x = 200, y = 650, anchor = 'center')

        #settings cancel button function
        def settings_cancel():
            settings_gui.destroy()
        
        #error screen popup
        def show_error_screen(settings_screen, message):
            #gui
            error_screen = tkinter.Toplevel(settings_screen)
            error_screen.title('Error!')
            error_screen.resizable(False, False)
            error_screen.grab_set()

            x = settings_screen.winfo_x()
            y = settings_screen.winfo_y()
            h = settings_screen.winfo_height()
            w = settings_screen.winfo_width()
            error_screen.geometry('%dx%d+%d+%d' % (w - 100, h - 150, x + 50, y + 75))
            error_screen.config(bg = 'white', highlightbackground = '#000F46', highlightcolor = '#000F46', highlightthickness = 10)

            #text elements
            error_title = Label(error_screen, text = 'Error', bg = '#000F46', fg = 'white', width = 12,
                        font = (None, 30)).place(x = 300, y = 40, anchor = 's')

            error_message = Message(error_screen, bg = 'white', fg = '#000F46', width = 500, justify = 'center', font = (None, 20))
            error_message.place(x = 300, y = 250, anchor = 'center')
            error_message.config(text = message)

            #buttons
            close_button = Button(error_screen, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                        text = 'Close', relief = 'raised', width = 10, font = (None, 25, 'bold'), command = lambda: error_close())
            close_button.place(x = 300, y = 500, anchor = 'center')

            def error_close():
                error_screen.destroy()

    def show_history_screen(self, master):
        history_file = 'history.txt' #file to read history data from

        #gui
        history_gui = tkinter.Toplevel(master)
        history_gui.title('Krypto History')
        history_gui.resizable(False, False)
        history_gui.grab_set()

        x = master.winfo_x()
        y = master.winfo_y()
        h = master.winfo_height()
        w = master.winfo_width()
        history_gui.geometry('%dx%d+%d+%d' % (w, h, x, y))
        history_gui.config(bg = 'white', highlightbackground = '#000F46', highlightcolor = '#000F46', highlightthickness = 10)

        #title
        title = Label(history_gui, text = 'History', bg = '#000F46', fg = 'white', width = 12,
                    font = (None, 40)).place(x = 350, y = 50, anchor = 's')

        #table
        table_frame = Frame(history_gui, highlightcolor = '#000F46', highlightbackground = '#000F46', highlightthickness = 8)
        table_frame.place(x = 9, y = 55)

        date_label = Label(table_frame, text = 'Date', font = (None, 20, 'bold'))
        date_label.grid(row = 0, column = 0, padx = 15)

        time_label = Label(table_frame, text = 'Time', font = (None, 20, 'bold'))
        time_label.grid(row = 0, column = 1, padx = 15)

        name_label = Label(table_frame, text = 'Coin', font = (None, 20, 'bold'))
        name_label.grid(row = 0, column = 2, padx = 30)

        price_label = Label(table_frame, text = 'Price', font = (None, 20, 'bold'))
        price_label.grid(row = 0, column = 3, padx = 25)

        email_sent_label = Label(table_frame, text = 'Email Sent?', font = (None, 20, 'bold'))
        email_sent_label.grid(row = 0, column = 4, padx = 15)


        def history_blank(): #fills history table with '-' for each value
            for i in range(13):
                for j in range(5):
                    info = Label(table_frame, height = 2, text = '-', font = (None, 11))
                    info.grid(row = 1 + i, column = j)
        
        table_data = {}

        if path.exists(history_file) and path.isfile(history_file):
            with open(history_file, 'r') as f:
                for i in range(13):
                    line = f.readline().strip().split(',')
                    for j in range(5):
                        info = Label(table_frame, height = 2, text = line[j], font = (None, 11))
                        info.grid(row = 1 + i, column = j)
                        table_data[(i, j)] = info
        else:
            history_blank()

        #buttons
        reset = Button(history_gui, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                text = 'Reset', relief = 'raised', width = 10, font = (None, 30, 'bold'), command = lambda: history_reset())
        reset.place(x = 500, y = 675, anchor = 'center')

        back = Button(history_gui, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                    text = 'Back', relief = 'raised', width = 10, font = (None, 30, 'bold'), command = lambda: history_back())
        back.place(x = 200, y = 675, anchor = 'center')

        def history_back():
            history_gui.destroy()

        def history_reset():
            delete_file(history_file)
            for i in range(13):
                for j in range(5):
                    table_data[i,j].config(text = '-')
            master.update()

    def show_alert_screen(self, master, settings, initial):
        alert_screen = tkinter.Toplevel(master)
        alert_screen.title('Alert Triggered!')
        alert_screen.resizable(False, False)
        alert_screen.grab_set()

        x = master.winfo_x()
        y = master.winfo_y()
        h = master.winfo_height()
        w= master.winfo_width()
        alert_screen.geometry('%dx%d+%d+%d' % (w - 100, h - 150, x + 50, y + 75))
        alert_screen.config(bg = 'white', highlightbackground = '#000F46', highlightcolor = '#000F46', highlightthickness = 10)

        #text elements
        alert_title = Label(alert_screen, text = 'Alert!', bg = '#000F46', fg = 'white', width = 12,
                    font = (None, 30)).place(x = 300, y = 40, anchor = 's')

        alert_info = Message(alert_screen, bg = 'white', fg = '#000F46', width = 500, justify = 'center', font = (None, 20))
        alert_info.place(x = 300, y = 120, anchor = 'center')
        alert_info.config(text = 'Alert triggered for \n' + settings.get_symbol() + ' - ' + settings.get_coin() +
                    '\nat ' + strftime('%H:%M:%S', localtime()))

        alert_price_info = Message(alert_screen, bg = 'white', fg = '#000F46', width = 500, justify = 'center', font = (None, 20))
        alert_price_info.place(x = 300, y = 225, anchor = 'center')

        if settings.get_alert_type() == 'Percent':
            alert_price_info.config(text = 'Price changed by ' + settings.get_alert_number() + '%' + '\nfrom $' + str(initial))
        elif settings.get_alert_type() == 'Flat':
            phrase = ''
            if settings.get_alert_sign() == '>':
                phrase = 'greater than $'
            elif settings.get_alert_sign() == '<':
                phrase = 'less than $'
            alert_price_info.config(text = 'Price was\n' + phrase + settings.get_alert_number())

        sound_info = Label(alert_screen, bg = 'white', fg = '#000F46', justify = 'center', font = (None, 20))
        sound_info.place(x = 300, y = 300, anchor = 'center')

        if settings.get_sound_status() == 'True':
            sound_info.config(text = 'A sound alert played.')
        else:
            sound_info.config(text = 'A sound alert was not played.')

        email_info = Label(alert_screen, bg = 'white', fg = '#000F46', justify = 'center', font = (None, 20))
        email_info.place(x = 300, y = 350, anchor = 'center')

        email_address = Label(alert_screen, bg = 'white', fg = '#000F46', justify = 'center', font = (None, 20))
        email_address.place(x = 300, y = 390, anchor = 'center')

        if settings.get_email_status() == 'True':
            email_info.config(text = 'An email was sent to:')
            email_address.config(text = str(settings.get_email()))
        else:
            email_info.config(text = 'An email was not sent.')

        close_button = Button(alert_screen, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                    text = 'Close', relief = 'raised', width = 10, font = (None, 25, 'bold'), command = lambda: alert_close())
        close_button.place(x = 300, y = 500, anchor = 'center')

        master.update()
        if settings.get_sound_status() == 'True':
            play_sound()

        def alert_close():
            alert_screen.destroy()

    def update_screen(self, settings_screen, cryptos):
        #gui
        update_screen = tkinter.Toplevel(settings_screen)
        update_screen.title('Update')
        update_screen.resizable(False, False)
        update_screen.grab_set()

        x = settings_screen.winfo_x()
        y = settings_screen.winfo_y()
        h = settings_screen.winfo_height()
        w = settings_screen.winfo_width()
        update_screen.geometry('%dx%d+%d+%d' % (w - 100, h - 150, x + 50, y + 75))
        update_screen.config(bg = 'white', highlightbackground = '#000F46', highlightcolor = '#000F46', highlightthickness = 10)

        #text elements
        update_title = Label(update_screen, text = 'Update Coin List', bg = '#000F46', fg = 'white', width = 15,
                        font = (None, 30)).place(x = 300, y = 40, anchor = 's')

        update_status = Label(update_screen, bg = 'white', fg = '#000F46', justify = 'center', 
                        font = (None, 25, "bold"), text = "Idle")
        update_status.place(x = 300, y = 150, anchor = 'center')

        update_message = Message(update_screen, bg = 'white', fg = '#000F46', width = 500, justify = 'center', 
                        font = (None, 20), text = "Click Go to begin updating the list of available coins!")
        update_message.place(x = 300, y = 250, anchor = 'center')

        update_warning = Message(update_screen, bg = 'white', fg = '#000F46', width = 350, justify = 'center', 
                        font = (None, 20, "italic"), text = "Note: The process cannot be interrupted once begun.")
        update_warning.place(x = 300, y = 400, anchor = 'center')

        #buttons
        go_button = Button(update_screen, bg = 'green', activebackground = 'green', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                        text = 'Go', relief = 'raised', width = 10, font = (None, 25, 'bold'), command = lambda: update_button(cryptos))
        go_button.place(x = 425, y = 500, anchor = 'center')

        close_button = Button(update_screen, bg = '#004ac2', activebackground = 'dodgerblue2', fg = 'antiquewhite1', activeforeground = 'antiquewhite1',
                        text = 'Close', relief = 'raised', width = 10, font = (None, 25, 'bold'), command = lambda: close_update())
        close_button.place(x = 175, y = 500, anchor = 'center')

        #go button function
        def update_button(cryptos):
            scrape_crypto_names(update_screen, update_status, update_message, go_button, close_button)

            #refresh the dropdown list
            csv_file = 'cryptos.csv'
            coin_dict = csv_to_dict(csv_file)
            coin_list = []
            for key in coin_dict.keys():
                coin_list.append(coin_dict[key][0] + ' - ' + key)

            cryptos.config(completevalues = coin_list)
        #cancel button function
        def close_update():
            update_screen.destroy()


def set_alert_info(settings, gui):
        if settings.get_alert_type() == 'Percent':
            gui.set_alert_text('When the price changes by ' + str(settings.get_alert_number()) + '%:')
        elif settings.get_alert_type() == 'Flat':
            if settings.get_alert_sign() == '<':
                phrase = 'is less than $'
            elif settings.get_alert_sign() == '>':
                phrase = 'is greater than $'
            gui.set_alert_text('When the price ' + phrase + str(settings.get_alert_number()) + ':')

        if settings.get_sound_status() == 'True':
            gui.set_sound_alert_text('I will play a sound!')
        elif settings.get_sound_status() == 'False':
            gui.set_sound_alert_text('I will not play a sound!')

        if settings.get_email_status() == 'True':
            gui.set_email_alert_text('I will send an email to:')
            gui.set_email_text(settings.get_email())
        elif settings.get_email_status() == 'False':
            gui.set_email_alert_text('I will not send an email!')
            gui.set_email_text('')

def set_ticker(root, settings, gui, current_price):
    gui.set_crypto(settings.get_symbol() + ' - ' + settings.get_coin())
    gui.set_font_size(5)

    if current_price != '':
        gui.set_price('$' + current_price)
        root.update()
        resize_font(root, gui.get_font(), gui.get_price_label())
    
    else:
        gui.set_price('No price data')
        gui.set_font_size(50)
        gui.set_price_color('antiquewhite1')

        