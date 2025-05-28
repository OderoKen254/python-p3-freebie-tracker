from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    founding_year = Column(Integer(), nullable=True)

    #Relationship to freebies
    freebies = relationship("Freebie", backref="company")
    devs = relationship("Dev", secondary="freebies", back_populates="companies", overlaps="company,freebies")

    #new freebies instance
    def give_freebie(self, dev, item_name, value):
        """Creates and returns a new Freebie instance."""
        freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        return freebie
    
    @classmethod
    def oldest_company(cls):
        """Returns the Company with the earliest founding year."""
        return cls.query.order_by(cls.founding_year).first()

    def __repr__(self):
        return f'<Company (name ={self.name}, founding_year={self.founding_year})>'
        #return session.query(cls).order_by(cls.founding_year.asc()).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String(), nullable=False)

    # Relationship
    freebies = relationship("Freebie", backref="dev")
    companies = relationship("Company", secondary="freebies", back_populates="devs", overlaps="dev,freebies")


    #new dev instances
    def received_one(self, item_name):
        """Returns True if dev has a freebie with item_name, else False."""
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def give_away(self, dev, freebie):
        """Transfers freebie to another dev if owned by this dev."""
        if freebie.dev == self:
            freebie.dev = dev

    def __repr__(self):
        return f'<Dev {self.name}>'


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer, nullable=False)
    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)

    created_at = Column(String, server_default='CURRENT_TIMESTAMP', nullable=False)
    updated_at = Column(String, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP', nullable=False)

    #Relationships
    dev = relationship( "Dev", backref=backref("freebies", overlaps="devs"),  overlaps="devs")
    company = relationship("Company", backref=backref("freebies", overlaps="company"))

    #instance to format freebies
    def print_details(self):
        """Returns formatted string with freebie details."""
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

    def __repr__(self):
        return f'<Freebie {self.item_name} valued at {self.value}>'