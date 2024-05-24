from sqlalchemy.orm import Session

from .models import Activity


# get activity of a user by username


async def get_activities_by_username(
    db: Session, username: str, page: int = 1, limit: int = 10
) -> list[Activity]:
    offset = (page - 1) * limit

    return (
        db.query(Activity)
        .filter(Activity.username == username)
        .order_by(Activity.timestamp.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
