from sense_emu import SenseHat
from time import sleep
from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.thesun.co.uk/tech/")
tech_news = page.content

sense = SenseHat()
soup = BeautifulSoup(tech_news, 'html5lib')

counter = 0
tech_news_headlines = soup.find_all('a', class_='teaser-anchor')


while True:
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