from django.core.management.base import BaseCommand

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

from scraping.models import Job

class Command(BaseCommand):
    help = 'collect jobs'
    
    # define logic of command
    def handle(self, *args, **kwargs):
        
        # collect_html
        html = urlopen('https://jobs.lever.co/opencare')
      
        # convert to soup
        soup = BeautifulSoup(html, 'html.parser')
        
        # grab all postings
        postings = soup.find_all("div", class_="posting")
        
        for p in postings:
            url = p.find('a', class_='posting-btn-submit')['href']
            title = p.find('h5').text
            if p.find('span', class_='sort-by-location'):
                location = p.find('span', class_='sort-by-location').text
            
            # check if url in db
            try:
                # save in db
                Job.objects.create(url=url,
                                   title=title,
                                   location=location
                                   )
                print(f"{title} added")
            except:
                print(f"{title} alredy exists")
        self.stdout.write('job complete')
            
        