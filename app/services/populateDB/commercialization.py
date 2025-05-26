from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError

from app.services.extractions.commercialization import CommercializationExtractor
from db.models import Commercialization
from db.database import AsyncSessionLocal


async def populate_commercializations(data: list[dict[str, str]], year: int):
    async with AsyncSessionLocal() as session:
        extractor = CommercializationExtractor()
        data = extractor.fetch_data(year)
        try:
            for item in data:
                product=item['product'],
                quantity=item['quantity'],
                product_type=item['product_type']
                year=year

                record = Commercialization(
                    product_name=product,
                    quantity=quantity,
                    product_type=product_type,
                    year=year
                )
                session.add(record)

            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
