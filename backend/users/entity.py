from sqlalchemy.orm import mapped_column,Mapped
from backend.config.db import Base
from backend.common.entity import TimestampMixin

class User(Base,TimestampMixin):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False,autoincrement=True)
    name:Mapped[str] = mapped_column(nullable=False)
    is_admin:Mapped[bool] = mapped_column(nullable=False,server_default="false")
    is_active:Mapped[bool] = mapped_column(nullable=False,server_default="true")
    is_notice:Mapped[bool] = mapped_column(nullable=False,server_default="false")
    

