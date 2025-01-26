from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from .model import Product
from .schema import ProductCreateModel,ProjectUpdateModel
from project.settings.database import engine, SessionLocal

session = SessionLocal(bind=engine)

images_bbox_router = APIRouter(prefix='/product')

product_router = APIRouter(
    prefix='/product'
)


# Create a new product
@product_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreateModel):
    db_product = Product(
        product_name=product.product_name,
        price=product.price,
        date_added=product.date_added or None  # Automatically set to None or current date if not provided
    )
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    session.close()
    data = {
        'id': db_product.id,
        'product_name': db_product.product_name,
        'price': db_product.price,
        'date_added': db_product.date_added
    }
    response = {
        'success': True,
        'code': status.HTTP_201_CREATED,
        'message': 'Product is created successfully'
    }

    return JSONResponse(status_code=201, content=response)


# Update an existing product
@product_router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_product(id: int, product: ProjectUpdateModel):
    db_product = session.query(Product).filter(Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Update fields
    db_product.product_name = product.product_name
    db_product.price = product.price
    db_product.date_added = product.date_added or db_product.date_added

    session.commit()
    session.refresh(db_product)
    session.close()
    data = {
        'success': True,
        'code': 200,
        'message': f'Product with {id} ID has been updated',
        'data': {
            'id': product.id,
            'product_name': product.product_name,
            'product_price': product.price
        }
    }
    return JSONResponse(status_code=200, content=data)



# Delete a product
@product_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id: int):
    db_product = session.query(Product).filter(Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    session.delete(db_product)
    session.commit()
    data = {
        'success': True,
        'code': 200,
        'message': f'Product with {id} ID has been deleted',
        'data': None
    }
    session.close()
    return JSONResponse(data)