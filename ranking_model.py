from pydantic import BaseModel

class Ranking(BaseModel):
    sc: dict #or JSON
    si: dict
    op: dict

