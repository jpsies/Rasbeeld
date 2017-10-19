import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session  # type: ignore
from sqlalchemy.dialects.postgresql import (
    UUID as _UUID,
)


Base = declarative_base()
DBSession = scoped_session(sessionmaker())


class UUID(_UUID):
    default = uuid.uuid4

    # pylint: disable=useless-super-delegation
    def __init__(self, as_uuid=True):
        super().__init__(as_uuid)
