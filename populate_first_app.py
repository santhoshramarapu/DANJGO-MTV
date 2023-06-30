import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

#FAKE POPULATE SCRIPT
import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen = Faker()
topics = ['search','social','marketplace','news','country','address','bank','color','barcode','currency']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t 

def populate(N=10):
    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        #create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        Webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=Webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(35)
    print("populating complete!!")

    




