import contextlib
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
sys.path.append('c:\2020ly\pythontest\database001\venv\lib\site-packages ')

engine = create_engine('sqlite:///foo.db?check_same_thread=False', echo=True)
Base = declarative_base()

from sqlalchemy.schema import Column


# 定义映射类User，其继承上一步创建的Base
class User(Base):
    # 指定本类映射到users表
    __tablename__ = 'users'
    # 如果有多个类指向同一张表，那么在后边的类需要把extend_existing设为True，表示在已有列基础上进行扩展
    # 或者换句话说，sqlalchemy允许类是表的字集
    # __table_args__ = {'extend_existing': True}
    # 如果表在同一个数据库服务（datebase）的不同数据库中（schema），可使用schema参数进一步指定数据库
    # __table_args__ = {'schema': 'test_database'}

    # 各变量名一定要与表的各字段名一样，因为相同的名字是他们之间的唯一关联关系
    # 从语法上说，各变量类型和表的类型可以不完全一致，如表字段是String(64)，但我就定义成String(32)
    # 但为了避免造成不必要的错误，变量的类型和其对应的表的字段的类型还是要相一致
    # sqlalchemy强制要求必须要有主键字段不然会报错，如果要映射一张已存在且没有主键的表，那么可行的做法是将所有字段都设为primary_key=True
    # 不要看随便将一个非主键字段设为primary_key，然后似乎就没报错就能使用了，sqlalchemy在接收到查询结果后还会自己根据主键进行一次去重
    # 指定id映射到id字段; id字段为整型，为主键，自动增长（其实整型主键默认就自动增长）
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    name = Column(String(20))
    fullname = Column(String(32))
    password = Column(String(32))

    # __repr__方法用于输出该类的对象被print()时输出的字符串，如果不想写可以不写
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


def get_dynamic_table_name_class(table_name):
    # 定义一个内部类
    class TestModel(Base):
        # 给表名赋值
        __tablename__ = table_name
        __table_args__ = {'extend_existing': True}

        username = Column(String(32), primary_key=True)
        password = Column(String(32))

    # 把动态设置表名的类返回去
    return TestModel

    # 查看映射对应的表
    User.__table__

    # 创建数据表。一方面通过engine来连接数据库，另一方面根据哪些类继承了Base来决定创建哪些表
    # checkfirst=True，表示创建表前先检查该表是否存在，如同名表已存在则不再创建。其实默认就是True
    Base.metadata.create_all(engine, checkfirst=True)

    # 上边的写法会在engine对应的数据库中创建所有继承Base的类对应的表，但很多时候很多只是用来则试的或是其他库的
    # 此时可以通过tables参数指定方式，指示仅创建哪些表
    # Base.metadata.create_all(engine,tables=[Base.metadata.tables['users']],checkfirst=True)
    # 在项目中由于model经常在别的文件定义，没主动加载时上边的写法可能写导致报错，可使用下边这种更明确的写法
    # User.__table__.create(engine, checkfirst=True)

    # 另外我们说这一步的作用是创建表，当我们已经确定表已经在数据库中存在时，我完可以跳过这一步
    # 针对已存放有关键数据的表，或大家共用的表，直接不写这创建代码更让人心里踏实


from sqlalchemy.orm import sessionmaker

# engine是2.2中创建的连接
Session = sessionmaker(bind=engine)

# 创建Session类实例
session = Session()
