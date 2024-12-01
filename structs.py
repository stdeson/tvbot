from pydantic import BaseModel


class CallBackMsg(BaseModel):
    key: str