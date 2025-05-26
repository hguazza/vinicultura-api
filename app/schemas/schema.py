# YearRangeValidation(year=year)
from typing import Optional
from pydantic import BaseModel, Field


class ValidateYear(BaseModel):
    """Validate Year model."""

    year: int = Field(..., ge=1970, le=2023)

class Commercialization(BaseModel):
    """Commercialization model."""

    product: str
    quantity: int
    type: Optional[str]

class CommercializationResponse(BaseModel):
    """Commercialization response model."""
    commercializations: list[Commercialization]

class Processing(BaseModel):
    """Commercialization model."""

    product: str
    quantity: int
    type: Optional[str]
    classification: str

class ProcessingResponse(BaseModel):
    """Commercialization response model."""
    commercializations: list[Processing]

class Production(BaseModel):
    """Production model."""

    product: str
    quantity: int
    type: Optional[str]

class ProductionResponse(BaseModel):
    """Production response model."""
    productions: list[Production]