# Krypto- Price Alert WebApp

## About Myself-
 Hola! I am Prachi Dixit aka 18BCY10064 at VIT😜.
 This assessment is given by Krypto Company.
 
## Instructions:
**IMPORTANT: Must use a Gmail account! as I have used yagmail**
<br> NOTE: In case of invalid email credentials, an email will not sent.
<br> EXTRA FEATURE: We can also alert as I have used winsounds.

## What I have done-
I have divided the project in two parts-
1. Krypto- Real Time Price Updater WebApp: 
      <br> In this part I have created an webapp which detects real time price of cryptos in USD. This webapp is made for scraping the crypto details so that we can use it in Krypto- Real Time PRice Alert Webapp. 
      You can even search the crypto by using the search tab.
      
      ![Demo1](https://user-images.githubusercontent.com/53315283/132959970-ca027f76-d3cd-43c1-a786-3af5e7ebd153.PNG)
      
2. Krypto- Real Time Price Alert WebApp: 
      <br> After scraping stuffs from Krypto- Real Time Price Updater Webapp we will use it to make our Alert WebApp.
      App will open up with a front home page having setting and history tab. How the app will going to run-
      
      ##### Step 1- Click on the settings tab for setting up the cypto.
      
      ![Demo2](https://user-images.githubusercontent.com/53315283/132959972-48b0daf4-f9e5-4464-aec4-f8295d768946.PNG)
      
      ##### Step 2- You have to click on update button so that the app can scrape the whole thing. {This will take around 3-4 minutes}
      
      ![Demo 7](https://user-images.githubusercontent.com/53315283/132960525-4777ed96-7f3f-4549-985c-09b8d177cd3f.PNG)
      
      ![Demo6](https://user-images.githubusercontent.com/53315283/132960528-73a4990e-372a-46b0-86ac-297a0c0d0ff4.PNG)
      
      ##### Step 3- After updating select your crypto for which you need to get the alert.
       
      ##### Step 4- Select crypto amount at which you need the update. {Options can be in percentage or the simple amount}
      
      ##### Step 5- Select how you want to get the update like by alerting on Email or playing a sound or both.{Alerting a user by playing a sound is an extra feature}.
      
      ![Demo3](https://user-images.githubusercontent.com/53315283/132959974-ef642ee2-9fb4-47ae-ae37-b08cbc626d87.PNG)
      
      ![Demo8](https://user-images.githubusercontent.com/53315283/132960626-4c2938d2-855b-4775-8814-5c1e5c53af7e.PNG)
      
      ##### Step 6- After confirming your email you will get back to the front page where you can see the current price of that crypto.
      
      ##### Step 7- Now, go and chill this app will alert on your mail or play a alert tone when your crypto amount is less than or greater than what you have been updated in settings.
      
      ![Demo9](https://user-images.githubusercontent.com/53315283/132960689-5ef0aece-b5e9-444f-8c46-fefc013c22e8.PNG)

      ##### Step 8- You can also check the history of alerts using history tab.
      
      ![Demo5](https://user-images.githubusercontent.com/53315283/132959988-9d27d079-34da-4fd4-a086-48cfafddade8.PNG)
      
 ## How you are going to run the App-
 As I don't have much time to combine the both project as like one WebApp. so, you have to run it seprately. 
 
#### Prequistes:
 
   - Python
   - React Js
   - Visual Studio Code.

#### Steps:

   1. Clone the repository.
   2. First open the Krypto- Real Time Price Updater WebApp Folder. Type the following commands in your terminals.
       
       Commands:
        - 'npm install axios'
        - 'npm start'
       
       It will open up the http://localhost:3000 to view it in the browser. You will get real time update because of using the API given by you (https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_d esc&per_page=100&page=1&sparkline=false) which gives USD amount of each crypto.
   3. Open the Second folder named Krypto- Real Time Price Alert WebApp in Visual studio code. Type the following commands to run the file.
       
       Commands:
        - pip install time
        - pip install bs4
        - pip install requests
        - pip install re
        - pip install random
        - pip install json
        - pip install yagmail
        - pip install winsounds
        - pip install tkinter
        - pip install ttwidgets
        - python crypto_alert.py
       
       It will also open up in http://localhost:3000 bydefault so you need to stop the first app before running the second one or just change the port number. Then both the WebApp can run smoothly.
       
 Hurray you are done!! 
 Feel Free to comment for any issues.
       

       
       
       
       
       
 
        
      
      
