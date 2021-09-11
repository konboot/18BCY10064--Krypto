# Krypto- Price Alert WebApp

### About Myself-
 Hola! I am Prachi Dixit aka 18BCY10064 at VIT😜.
 This assessment is given by Krypto Company.
 
### What we need to do-   
- Create a rest API endpoint for the user’s to create an alert alerts/create/ 
- Create a rest API endpoint for the user’s to delete an alert alerts/delete/ 
- Create a rest API endpoint to fetch all the alerts that the user has created. 
- The response should also include the status of the alerts (created/deleted/triggered/.. or any other status you feel needs to be included) - Paginate the response.
- Include filter options based on the status of the alerts. Eg: if the user wanted only the alerts that were triggered, then the endpoint should provide just that)
- Add user authentication to the endpoints. Use JWT tokens.
- There is no need to add tests.
- Write a script that monitors the price of the cryptocurrency
- You can use this endpoint to fetch the latest price of the cryptocurrency: https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_d esc&per_page=100&page=1&sparkline=false
- When the price of the coin reaches the price specified by the users, send an email to all the users that set the alert at that price. (send mail using Gmail SMTP, SendGrid, etc) 
- You should set up a background worker(eg: celery/python-script/go-script) to send the email. Use Rabbit MQ/Redis as a message broker.)

### What I have done-
I have divided the project in two parts-
1. Krypto- Real Time Price Updater WebApp: 
      In this part I have created an webapp which detects real time price of cryptos in USD. This webapp is made for scraping the crypto details so that we can use it in Krypto- Real Time PRice Alert Webapp. 
      You can even search the crypto by using the search tab.
      
2. Krypto- Real Time Price Alert WebApp: 
      After scraping stuffs from Krypto- Real Time Price Updater Webapp we will use it to make our Alert WebApp.
      App will open up with a front home page having setting and history tab. How the app will going to run-
      
      ##### Step 1- Click on the settings tab for setting up the cypto.
      ##### Step 2- You have to click on update button so that the app can scrape the whole thing. {This will take around 3-4 minutes}
      ##### Step 3- After updating select your crypto for which you need to get the alert.
      ##### Step 4- Select crypto amount at which you need the update. {Options can be in percentage or the simple amount}
      ##### Step 5- Select how you want to get the update like by alerting on Email or playing a sound or both.{Alerting a user by playing a sound is an extra feature}.
      ##### Step 6- After confirming your email you will get back to the front page where you can see the current price of that crypto.
      ##### Step 7- Now, go and chill this app will alert on your mail or play a alert tone when your crypto amount is less than or greater than what you have been updated in settings.
      ##### Step 8- You can also check the history of alerts using history tab.
      
 ### How you are going to run the App-
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
       
       
       
       
       
       
 
        
      
      
