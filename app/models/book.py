from sqlalchemy import orm, Column, String, Integer

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    # 类变量和实例变量的关系
    # 类变量是公用的
    # 实例变量是私有的

    # sqlachemy ORM
    # 元类 并不会调用构造方法
    # 参考 https://docs.sqlalchemy.org/en/latest/orm/constructors.html
    @orm.reconstructor
    def init_on_load(self):
        self.fields = [
            'id', 'title', 'author', 'binding', 'publisher',
            'price', 'pages', 'pubdate', 'isbn', 'summary', 'image'
        ]

    def keys(self):
        return self.fields

