from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    TIMESTAMP,
    ForeignKey,
    Text,
    Time,
)
from sqlalchemy.sql.expression import text
from app.database import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, nullable=False)
    image_cover = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    tag = Column(String, nullable=False)
    address = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    open_time = Column(Time)
    close_time = Column(Time)
    # registration_date = Column(TIMESTAMP(timezone=True), nullable=False)
