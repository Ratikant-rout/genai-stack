from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from genai_stack.genai_server.models.component_models import StackComponentResponseModel
from genai_stack.genai_server.models.constants import STR_FIELD_MAX_LENGTH


class StackRequestModel(BaseModel):
    """Data Model for Stack Request."""

    name:str = Field(
        title="The name of the stack.", max_length=STR_FIELD_MAX_LENGTH
    )
    description:str = Field(
        title="The description of the stack",
        max_length=STR_FIELD_MAX_LENGTH,
    )


class StackResponseModel(BaseModel):
    """Data Model for Stack Response."""

    id:int
    name:str
    description:str
    components: List[StackComponentResponseModel]
    created_at: datetime
    modified_at: Optional[datetime] 


class StackFilterModel(BaseModel):
    """Data Model for Stack Filter."""

    id:int
