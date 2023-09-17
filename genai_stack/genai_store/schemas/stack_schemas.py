from sqlalchemy import Column, Integer, String

from genai_stack.genai_store.schemas.base_schemas import TimeStampedSchema
from genai_stack.genai_server.models.constants import STR_FIELD_MAX_LENGTH

class StackSchema(TimeStampedSchema):
    """
    SQL Schema for Stacks.

    Args:
        name : String
        description : String
    """
    
    __tablename__ = "stacks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(STR_FIELD_MAX_LENGTH), nullable=False)
    description = Column(String(STR_FIELD_MAX_LENGTH), nullable=False)