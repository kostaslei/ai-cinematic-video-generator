from pydantic import BaseModel

class BaseAgentOutput(BaseModel):
    class Config:
        str_strip_whitespace = True