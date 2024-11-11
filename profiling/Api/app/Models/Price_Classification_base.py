from pydantic import BaseModel

class Price_Classification_base(BaseModel):
    premium_median :float
    coverage_limit_median :float
    Pricing_Method :int
    price_ratio_median : float
    