import ca_gui
from ca_gui import *
import ca_scraping
from ca_scraping import *
import ca_settings
from ca_settings import *
import time


def crypto_alert():
    settings_file = "settings.txt"
    settings = ca_settings(settings_file)

    #GUI init
    root = tkinter.Tk()
    gui = ca_gui(root, settings)

    current_price = ""
    last_price = ""
    initial = ""
    counter = 0

    test_url = "http://www.google.com"
    test_timeout = 5

    try:
        test_request = requests.get(test_url, timeout = test_timeout)

        if settings.get_coin() != "":
            current_price = get_price(settings.get_url())
            last_price = current_price
    except:
        gui.set_crypto('No internet connection!')


    def update():
        nonlocal settings, current_price, last_price, initial, counter
        counter = counter + 1

        #check for internet connection
        connected = False
        test_url = "http://www.google.com"
        test_timeout = 5

        try:
            test_request = requests.get(test_url, timeout = test_timeout)
            connected = True
        except:
            gui.set_crypto('No internet connection!')

        if connected:

            if settings.get_coin() != "" :
                if settings.get_is_new():
                    current_price = get_price(settings.get_url())
                    set_ticker(root, settings, gui, current_price)
                    set_alert_info(settings, gui)
                    initial = current_price
                    settings.set_is_new(False)
                    counter = 61
                
                else:
                    gui.set_crypto(settings.get_symbol() + " - " + settings.get_coin())
                    if counter > 60:
                        counter = 0

                        if current_price != "" and last_price != current_price:
                            last_price = current_price

                        current_price = get_price(settings.get_url())

                        if alert_check(settings, initial, current_price):
                            to_history('history.txt', '{month}/{day}/{year},{time},{symbol},${price},{email_sent}'.format(month = date.today().month, day = date.today().day,
                                year = date.today().year, time = strftime("%H:%M:%S", localtime()), symbol = settings.get_symbol(), 
                                price = current_price.replace(",",""), email_sent = settings.get_email_status()))

                            if settings.get_email_status() == "True":
                                send_email(settings, current_price, initial)

                            gui.show_alert_screen(root, settings, initial)
                            
                            settings.blank_settings()
                            delete_file(settings_file)
                            gui.default_display()

                        elif current_price != "":
                            if float(current_price.replace(",","")) > float(last_price.replace(",","")):
                                gui.set_price_color("lime green")
                            elif float(current_price.replace(",","")) < float(last_price.replace(",","")):
                                gui.set_price_color("red")
                            
                            gui.set_price("$" + current_price)

            else:
                gui.set_crypto("No Coin Selected")
        root.after(500, update)


    update()
    root.mainloop()

crypto_alert()
