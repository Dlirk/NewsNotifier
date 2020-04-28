from sense_emu import SenseHat
from time import sleep
from bs4 import BeautifulSoup
import requests
import schedule

page = requests.get("https://www.thesun.co.uk/tech/")
tech_news = page.content

sense = SenseHat()
soup = BeautifulSoup(tech_news, 'html5lib')

counter = 0
tech_news_headlines = soup.find_all('a', class_='teaser-anchor')

def update():
    page = requests.get("https://www.thesun.co.uk/tech/")
    tech_news = page.content
    tech_news_headlines = soup.find_all('a', class_='teaser-anchor')
    
    return tech_news_headlines

schedule.every().hour.do(update)

while True:
    schedule.run_pending()
    event = sense.stick.wait_for_event()
    
    if event.direction == "left":
        counter = counter - 1

    elif event.direction == "right":
        counter = counter + 1

    elif event.direction == "up":
        sense.show_message(tech_news_headlines[counter-1]['data-headline'], scroll_speed=0.05)
        sense.clear()
    elif event.direction == "down":
        sense.clear()

    print(event)
    print(counter)
    sleep(1)