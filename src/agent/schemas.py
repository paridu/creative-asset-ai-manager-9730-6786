from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class SearchFilters(BaseModel):
    """Structured filters extracted from natural language."""
    color_palette: Optional[List[str]] = Field(None, description="List of dominant colors mentioned")
    file_types: Optional[List[str]] = Field(None, description="File extensions like .psd, .jpg, .pdf")
    date_after: Optional[datetime] = Field(None, description="Start date for range search")
    date_before: Optional[datetime] = Field(None, description="End date for range search")
    project_name: Optional[str] = Field(None, description="Specific project the user is referring to")
    min_width: Optional[int] = Field(None, description="Minimum image width")

class QueryPlan(BaseModel):
    """The execution plan for the search engine."""
    semantic_query: str = Field(..., description="The core visual/contextual concept to search via Vector DB")
    filters: SearchFilters
    reasoning: str = Field(..., description="Brief explanation of how the agent interpreted the request")