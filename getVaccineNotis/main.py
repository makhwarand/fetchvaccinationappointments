#from twilio.rest import Client
import smtplib
from urllib.request import Request, urlopen
from time import sleep
import json
from email.mime.text import MIMEText
import webbrowser
import sys
import time



def get_appointments(cities):
    req = Request('https://www.vaccinespotter.org/api/v0/states/MA.json', headers={'User-Agent': 'Mozilla/5.0'})
    locations = json.loads(urlopen(req).read())['features']
    success = False
    for location in locations:
        place = location['properties']
        #if place['city'] not in cities:
            #continue
        if place['appointments_available']:
            print(place)
            address = place['address']  #get address
            city = place['city'] #get city
            appointments = place['appointments'] #get appointments
            url = place['url']#get url
            message = 'Appointment Found at ' + address +', ' + city + ', MA \nAppointment Times: ' + appointments + '\nLink: ' + url
            # ^^ create message ^^
            send_message(message)
            success = True
    return success

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cities = ['Weymouth', 'Hingham', 'Hull', 'Dedham', 'Boston', 'Quincy', 'Braintree', 'Needham', 'West Roxbury', 'Hyde Park'
            'Westwood', 'South Weymouth', 'Randolph', 'Holbrook', 'Norwell', 'Rockland', 'Cohasset', 'Hanover']
    while not get_appointments(cities):
        sleep(5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
