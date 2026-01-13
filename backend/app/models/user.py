from typing import List, TYPE_CHECKING
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from .account import Account
    from .transaction import Transaction
    from .category import Category
    from .counterparty import Counterparty


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    password_hash: Mapped[str] = mapped_column(String)

    accounts: Mapped[List["Account"]] = relationship(back_populates="user")
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="user")
    categories: Mapped[List["Category"]] = relationship(back_populates="user")
    counterparties: Mapped[List["Counterparty"]] = relationship(back_populates="user")
