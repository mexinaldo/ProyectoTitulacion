import sqlalchemy as db
from Chess import persistence as mod

engine = db.create_engine('sqlite:///db/login.sqlite', echo=True, future=True)
mod.Base.metadata.create_all(engine)
