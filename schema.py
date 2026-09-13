from pydantic import BaseModel, Field
from typing import Optional

class TargetLead(BaseModel):
    company_name: str = Field(..., description="Legal or operating name of the company")
    website: str = Field(..., description="Official URL or root domain of the company")
    description: str = Field(..., description="Brief 1-2 sentence description of what the platform does")
    industry_or_orbit: str = Field(..., description="Sector e.g., AI, Cybersecurity, Fintech, Healthcare, Digital Twin")
    funding_or_revenue: str = Field(..., description="Funding or revenue in USD/EUR/GBP (strictly between $1M and $5M USD equivalent)")
    hq_country: str = Field(..., description="Country where the company is headquartered")
    us_presence: str = Field(..., description="Description of US presence (must be minimal or none)")
    founder_name: Optional[str] = Field(None, description="Name of the CEO or Co-founder")
    founder_role: Optional[str] = Field(None, description="CEO or Co-founder title")
    verified_email: Optional[str] = Field(None, description="Verified business email of the founder. Blank if unverified.")
    is_qualified: bool = Field(..., description="True ONLY if funding is $1M-$5M, is tech platform, and minimal/no US presence")