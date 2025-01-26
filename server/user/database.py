from sqlalchemy import create_engine, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declared_attr, Mapped, mapped_column

URL_DATABASE='postgresql://db_user:123456@postgres:5432/postgres'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)