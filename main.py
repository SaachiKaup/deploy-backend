from enum import Enum
from typing import Any, List
from fastapi import FastAPI
from pydantic import BaseModel, Json, ValidationError
Fresh Hyena

from ranking_model import Ranking 

import generate_scores as gs 

app = FastAPI()

@app.post("/users/{user_id}/tests/{test_id}")
async def global_scores(user_id: int, test_id: int, rankings: Ranking):
    return {"global_scores": gs.global_scores(rankings)}
