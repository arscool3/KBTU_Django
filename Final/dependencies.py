# app/dependencies.py

from fastapi import Depends
from tortoise.contrib.fastapi import HTTPNotFoundError

from .models import Seed


async def get_seed(seed_id: int) -> Seed:
    return await Seed.get_or_none(id=seed_id)


def get_seed_or_404(seed: Seed = Depends(get_seed)) -> Seed:
    if seed is None:
        raise HTTPNotFoundError(detail="Seed not found")
    return seed


# Define other dependencies here
