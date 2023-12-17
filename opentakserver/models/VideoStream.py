from extensions import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class VideoStream(db.Model):
    __tablename__ = "video_streams"

    # These fields taken from MediaMTX's externalAuthenticationURL
    ip: Mapped[str] = mapped_column(String, primary_key=True)
    path: Mapped[str] = mapped_column(String, primary_key=True)
    id: Mapped[str] = mapped_column(String)  # This is a UUID that changes every time
    username: Mapped[str] = mapped_column(String, ForeignKey("user.username"))
    protocol: Mapped[str] = mapped_column(String)
    action: Mapped[str] = mapped_column(String)
    query: Mapped[str] = mapped_column(String, nullable=True)
    user = relationship("User", back_populates="video_streams")