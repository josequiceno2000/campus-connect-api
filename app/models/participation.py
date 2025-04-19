from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

participation_table = Table(
    "participations",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("event_id", Integer, ForeignKey("events.id"), primary_key=True),
)

class Participation(Base):
    __tablename__ = "participations"

    user_id = Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
    event_id = Column("event_id", Integer, ForeignKey("events.id"), primary_key=True)

    user = relationship("User", back_populates="events")
    event = relationship("Event", back_populates="participants")