import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from flask_login import UserMixin
from models import Base
f


# URL de la base de données
url = 'postgresql://zasnrhbz:c_2dQQfWMWhCHkuxpP9l5ZB0cVZ4Ed5K@horton.db.elephantsql.com/zasnrhbz'
# Création du moteur de base de données
engine = sqla.create_engine(url)

# Base de modèle SQLAlchemy
Base = declarative_base()

# Classe de session SQLAlchemy
Session = sessionmaker(bind=engine)

# Objet de session
SESSION = Session()

from sqlalchemy import Column, Integer, String
from models import Base

class IncomeExpenses(Base):
    __tablename__ = 'api_sold'

    id = Column(Integer, primary_key=True)
    type = Column(String(30), default='income')
    description = Column(String(255))
    amount = Column(Integer)
    date = Column(DateTime)

    def __repr__(self):
        return f"IncomeExpenses(id={self.id}, type='{self.type}', description='{self.description}', amount={self.amount})"



class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, email='{self.email}', name='{self.name}')"

