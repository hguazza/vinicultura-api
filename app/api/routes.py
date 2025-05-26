from fastapi import APIRouter

from app.schemas.schema import CommercializationResponse, ProcessingResponse, ProductionResponse
from app.services.extractions.commercialization import CommercializationExtractor
from app.services.extractions.processing import ProcessingExtractor

commercialization_router = APIRouter()
processing_router = APIRouter()
production_router = APIRouter()

@commercialization_router.get("/commercialization/{year}", response_model=CommercializationResponse)
async def get_commercializations(year: int) -> CommercializationResponse:
    """
    Endpoint to get the comercializaciao data for a given year.
    """
    # Here you would call your extraction and normalization logic
    # here call logic to check year range
    extractor = CommercializationExtractor()
    response = extractor.fetch_data(year)

    return response

@processing_router.get("/processing/{year}", response_model=ProcessingResponse)
def get_processings(year: int) -> ProcessingResponse:
    """
    Endpoint to get the processing data for a given year.
    """

    # Here you would call your extraction and normalization logic
    # For now, we'll just return a placeholder response
    # return {"year": year, "data": "processing data"}
    extractor = ProcessingExtractor()
    response = extractor.fetch_data(year)

    return response

@production_router.get("/production/{year}", response_model=ProductionResponse)
def get_productions(year: int) -> ProductionResponse:
    """
    Endpoint to get the production data for a given year.
    """

    # Here you would call your extraction and normalization logic
    # For now, we'll just return a placeholder response
    return {"year": year, "data": "production data"}