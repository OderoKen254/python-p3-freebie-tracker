#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


#testing relationships
Kennedy = session.query(Dev).filter_by(name="Kennedy").first()
print(Kennedy.freebies)
print(Kennedy.company)

TechTrend = session.query(Company).filter_by(name="TechTrend").first()
print(TechTrend.freebies) 
print(TechTrend.devs)  

freebie = Diana.freebies[0]
print(freebie.dev)  
print(freebie.company)  

# Test aggregate methods
print(freebie.print_details())  
print(Kennedy.received_one("T-shirt"))  
print(Kennedy.received_one("Laptop")) 

Julia = session.query(Dev).filter_by(name="Julia").first()
SoftPeak.give_freebie(Julia, "Pen", 3) 
session.commit()

print(Company.oldest_company())  

Fiona.give_away(bob, freebie)  
session.commit()
print(freebie.dev)   