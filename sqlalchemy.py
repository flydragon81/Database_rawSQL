import contextlib
import datetime
from sqlalchemy import create_engine, declarative_base,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,Column
from sqlalchemy import  (
    create_engine,
    Column,
    Integer,
    DateTime,
    String,
)
from config import config  # config模块里有自己写的配置，我们可以换成别的，注意下面用到config的地方也要一起换

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,  # SQLAlchemy 数据库连接串，格式见下面
    echo=bool(config.SQLALCHEMY_ECHO),  # 是不是要把所执行的SQL打印出来，一般用于调试
    pool_size=int(config.SQLALCHEMY_POOL_SIZE),  # 连接池大小
    max_overflow=int(config.SQLALCHEMY_POOL_MAX_SIZE),  # 连接池最大的大小
    pool_recycle=int(config.SQLALCHEMY_POOL_RECYCLE),  # 多久时间主动回收连接，见下注释
)
Session = sessionmaker(bind=engine)
Base = declarative_base(engine)


class BaseMixin:
    """model的基类,所有model都必须继承"""
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now,
                        index=True)
    deleted_at = Column(DateTime)  # 可以为空, 如果非空, 则为软删


@contextlib.contextmanager
def get_session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()


class User(Base, BaseMixin):
    __tablename__ = "user"

    Name = Column(String(36), nullable=False)
    Phone = Column(String(36), nullable=False, unique=True)

