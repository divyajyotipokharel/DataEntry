import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DataEntry.settings')

import django
django.setup()

# fake pop script
import random
from operator_form.models import Post
from faker import Faker
from django.db import models
from django.contrib.auth.models import User

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def populate(N=5):
    for entry in range(N):
        fake_random_int = fakegen.random_int()
        fake_date = fakegen.date()
        fake_name = fakegen.name()
        fake_ssn = fakegen.ssn()
        fake_date_time = fakegen.date_time()
        fake_email = fakegen.email()
        fake_address = fakegen.address()
        fake_city = fakegen.city()
        fake_state = fakegen.state()
        fake_postcode = fakegen.postcode()
        fake_phone_number = fakegen.phone_number()
        fake_card = fakegen.credit_card_provider()
        fake_credit_card_number = fakegen.credit_card_number()

        post = Post.objects.get_or_create(created_date=fake_date_time,published_date=fake_date_time,file_no=fake_name,record_no=fake_random_int,entry_date=fake_date_time,ref_no=fake_random_int,invoice_no=fake_random_int,courier_name=fake_name,con_no=fake_ssn,dispatch_date=fake_date_time,dispatch_by=fake_name,sales_date=fake_date,sales_time=fake_date_time,customer_name=fake_name,mail_address=fake_email,agent_name=fake_name,address=fake_address,city=fake_city,state=fake_state,zip_code=fake_postcode,customer_phone=fake_phone_number,credit_card_type=fake_card,credit_card_number=fake_credit_card_number)
if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(50)
    print('Populating Complete')