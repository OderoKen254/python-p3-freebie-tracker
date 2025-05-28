#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db') 
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


#Clearing existing data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()


#Create companies
companies = [
    Company(name="KenTechnologies", founding_year=2021),
    Company(name="TechTrend", founding_year=1999),
    Company(name="CodeZap", founding_year=2000),
    Company(name="Innovatech", founding_year=2015),
    Company(name="SoftPeak", founding_year=2019),
    Company(name="HackWave", founding_year=2023)
]
session.add_all(companies)


#Create devs
devs = [
    Dev(name="Kennedy Odero"),
    Dev(name="Bob Johnson"),
    Dev(name="Erickson Smith"),
    Dev(name="Diana Lee"),
    Dev(name="Evan Patel"),
    Dev(name="Fiona Clark"),
    Dev(name="George Washington"),
    Dev(name="Hannah Davis"),
    Dev(name="Ian Wilson"),
    Dev(name="Julia Martinez")
]
session.add_all(devs)


#Create freebies
freebies = [
    Freebie(item_name="T-Shirt", value=20, dev=devs[0], company=companies[0]),   # Kennedy from KenTechnologies
    Freebie(item_name="Mug", value=15, dev=devs[0], company=companies[1]),       # Kennedy from TechTrend
    Freebie(item_name="Sticker", value=5, dev=devs[1], company=companies[0]),    # Bob from KenTechnologies
    Freebie(item_name="Notebook", value=10, dev=devs[2], company=companies[2]),  # Erickson from CodeZap
    Freebie(item_name="Pen", value=3, dev=devs[3], company=companies[3]),        # Diana from Innovatech
    Freebie(item_name="Lanyard", value=8, dev=devs[4], company=companies[4]),    # Evan from SoftPeak
    Freebie(item_name="Hat", value=25, dev=devs[5], company=companies[5]),       # Fiona from HackWave
    Freebie(item_name="Water Bottle", value=12, dev=devs[6], company=companies[1]), # George from TechTrend
    Freebie(item_name="Backpack", value=30, dev=devs[7], company=companies[2]),     # Hannah from CodeZap
    Freebie(item_name="USB Drive", value=10, dev=devs[8], company=companies[3]),    # Ian from Innovatech
    Freebie(item_name="Mouse Pad", value=7, dev=devs[9], company=companies[4])      # Julia from SoftPeak
]
session.add_all(freebies)


# Committing the session to save all changes and closing the session
session.commit()
session.close()