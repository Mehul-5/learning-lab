from pydantic import BaseModel, ValidationError, Field
from datetime import datetime, UTC

class User(BaseModel):
    uid: int
    username: str
    email: str
    bio: str = ""
    verified_at: datetime | None = None
    is_active: bool = True
    full_name: str | None = None

class BlogPost(BaseModel):
    title: str
    content: str
    view_count: int = 0
    is_published: bool = False
    tags: list[str] = Field(default_facrory=list)
    create_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
