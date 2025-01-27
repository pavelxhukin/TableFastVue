from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from enum import Enum as PyEnum
from typing import Optional

class WeekdayEnum(PyEnum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"


class User(Base):
    __tablename__ = 'users'

    token: Mapped[Optional[str]] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] 
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))  

    group: Mapped["Group"] = relationship(
        "Group",
        back_populates="users"
    )


class Group(Base):
    __tablename__ = 'groups'

    description: Mapped[str]

    users: Mapped[list["User"]] = relationship(
        "User",
        back_populates="group",
    )
    
    schedules: Mapped[list["Schedule"]] = relationship(
        "Schedule",
        back_populates="group",
        cascade="all, delete-orphan"  # Удаляет посты при удалении пользователя
    )


class Schedule(Base):
    __tablename__ = 'schedules'

    time: Mapped[str]
    title: Mapped[str]  
    cabinet: Mapped[str] 
    weekday: Mapped[WeekdayEnum] = mapped_column(
        default=WeekdayEnum.monday,
    )


    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))
    
    group: Mapped["Group"] = relationship(
        "Group",
        back_populates="schedules"
    )

