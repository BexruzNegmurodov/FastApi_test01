from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.sql import func
from project.settings.database import Base  # SQLAlchemy Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    price = Column(Float)
    date_added = Column(Date, default=func.current_date())  # Automatically sets to the current date
