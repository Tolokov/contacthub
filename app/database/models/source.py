from app.database.core.base import BaseModel


class Source(BaseModel):
    __tablename__ = 'sources'
    __doc__ = 'The source of the information about the company'

    # TODO image to zip
    name: str
    link: str
    icon: str
    format_icon: str
    description: str

