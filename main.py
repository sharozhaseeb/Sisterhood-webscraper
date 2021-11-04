from bs4 import BeautifulSoup
import requests
import time
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDKYH5Na1kHnZEHdZzw0X8dMWQYLn6pbC8",
    'authDomain': "maps-project-bb7b0.firebaseapp.com",
    'databaseURL': "https://maps-project-bb7b0-default-rtdb.firebaseio.com",
    'projectId': "maps-project-bb7b0",
    'storageBucket': "maps-project-bb7b0.appspot.com",
    'messagingSenderId': "162460674604",
    'appId': "1:162460674604:web:181c1ad06bf19b610d7f89",
    'measurementId': "G-TST1FD76FY"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()

email = 'pythonbackend@python.com'
password = 'python1234'

auth.sign_in_with_email_and_password(email, password)


def find_news():
    new_html = requests.get('https://www.geo.tv/latest-news').text
    soup = BeautifulSoup(new_html, 'lxml')
    news = soup.find_all('li', class_='border-box')

    num = ['women', 'abuse', 'rape', 'harassment', 'Women', 'Abuse', 'Rape', 'Harassment', 'Pakistan', 'Domestic violence',
           'Mike', 'Lahore'
           ]
    list_temp = []
    for new in news:
        title = new.find('h2').text
        for word in num:
            if word in title:
                last_update = new.find('span', class_='date').text
                data = {'title': title, 'last updated': last_update, 'link': new.a['href']}
                list_temp.append(data)
                print(data)
                db.child("news").child(title).push(data)


find_news()

'''if __name__ == '__main__':
    while True:
        find_news()
        print("Waiting 3 hours....")
        time.sleep(10800)
'''
