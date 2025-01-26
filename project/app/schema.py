from pydantic import BaseModel
from datetime import date
from typing import Optional



class ProductCreateModel(BaseModel):
    id: Optional[int] = None
    product_name: str
    price: float
    date_added: Optional[date] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'product_name': 'book',
                'price': '5.32'
            }
        }


class ProjectUpdateModel(BaseModel):
    id: Optional[int] = None
    product_name: Optional[str] = None
    price: Optional[float] = None
    date_added: Optional[date] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'product_name': 'book',
                'price': '5.32'
            }
        }
