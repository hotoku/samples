from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    prefecture = Column(String(10))
    latitude = Column(Float)
    longitude = Column(Float)
    cnt = Column(Integer)

    def __repr__(self):
        return "<Station('%s', '%s', '%s', '%s', '%s')>" % (
            self.name, self.prefecture, self.latitude, self.longitude, self.cnt
        )


def _create_session():
    db_url = "mysql://root@localhost/pomap"
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()


session = _create_session()
ret = session.query(Station).filter(Station.name.like("%新宿%")).all()
print(ret)
