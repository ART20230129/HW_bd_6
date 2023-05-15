import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()

##модели классов SQLAlchemy

class Publisher(Base):
    __tablename__ = "publisher"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50))

    def __str__(self):
        return f'Publisher {self.id}: {self.name}'



class Book(Base):
    __tablename__ = "book"
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'Book {self.id}: ({self.title}, {self.id_publisher})'


class Shop(Base):
    __tablename__ = "shop"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50))

    def __str__(self):
        return f'Shop {self.id}: {self.name}'


class Stock(Base):
    __tablename__ = "stok"
    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    book = relationship(Book, backref="stok")
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    shop = relationship(Shop, backref="stok")

    def __str__(self):
        return f'Stock {self.id}: ({self.count}, {self.id_book}, {self.id_shop})'


class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    data_sale =sq.Column(sq.String(50))
    count = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stok.id"), nullable=False)
    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f'Sale {self.id}: ({self.price}, {self.data_sale}, {self.id_stoc})'


## функция открытия таблиц (предварительно унчтожаются ранее созданные)
def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


DSN = 'postgresql://postgres:AdelaidA@localhost:5432/test8'
engine = sqlalchemy.create_engine(DSN)

## ВЫЗЫВАЕМ ФУНКЦИЮ СОЗДАНИЯ ТАБЛИЦ
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Заполняет таблицу publisher
publisher_1 = Publisher(name="Сергей Лукьяненко")
publisher_2 = Publisher(name="Йен Макдональд")
publisher_3 = Publisher(name="Джеймс Кори")
publisher_4 = Publisher(name="Пол Макоули")
publisher_5 = Publisher(name="Александp Беляев")

session.add(publisher_1)
session.add(publisher_2)
session.add(publisher_3)
session.add(publisher_4)
session.add(publisher_5)
session.commit()

# Заполняем таблицу book
book_1 = Book(title="Спектр", id_publisher=1)
book_2 = Book(title="Осенние визиты", id_publisher=1)
book_3 = Book(title="Дорога запустения", id_publisher=2)
book_4 = Book(title="Новая Луна", id_publisher=2)
book_5 = Book(title="Волчья Луна", id_publisher=2)
book_6 = Book(title="Восставшая Луна", id_publisher=2)
book_7 = Book(title="Пробуждение Левиафана", id_publisher=3)
book_8 = Book(title="Война Калибана", id_publisher=3)
book_9 = Book(title="Тихая война", id_publisher=4)
book_10 = Book(title="Сады Солнца", id_publisher=4)
book_11 = Book(title="Звезда КЭЦ", id_publisher=5)
book_12 = Book(title="Человек-амфибия", id_publisher=5)
book_13 = Book(title="Продавец воздуха", id_publisher=5)
book_14 = Book(title="Дозоры", id_publisher=1)

session.add_all([book_1, book_2, book_3, book_4, book_5, book_6, book_7])
session.add_all([book_8, book_9, book_10, book_11, book_12, book_13, book_14])
session.commit()

# Заполняем таблицу shop
shop_1 = Shop(name="Магазин № 1")
shop_2 = Shop(name="Магазин № 2")
shop_3 = Shop(name="Магазин № 2")

session.add_all([shop_1, shop_2, shop_3])
session.commit()

# Заполняем таблицу stock
stock_1 = Stock(count=100, id_book=1, id_shop=1)
stock_2 = Stock(count=200, id_book=2, id_shop=1)
stock_3 = Stock(count=150, id_book=11, id_shop=3)
stock_4 = Stock(count=300, id_book=8, id_shop=2)
stock_5 = Stock(count=200, id_book=6, id_shop=3)
stock_6 = Stock(count=500, id_book=5, id_shop=1)
stock_7 = Stock(count=600, id_book=12, id_shop=3)
stock_8 = Stock(count=700, id_book=4, id_shop=2)
stock_9 = Stock(count=300, id_book=14, id_shop=2)
stock_10 = Stock(count=500, id_book=7, id_shop=2)

session.add_all([stock_1, stock_2, stock_3, stock_4, stock_5, stock_6, stock_7])
session.add_all([stock_8, stock_9, stock_10])
session.commit()

# Заполняем таблицу sale
sale_1 = Sale(price=50, data_sale="10-05-2023", count=100, id_stock=1)
sale_2 = Sale(price=100, data_sale="10-05-2023", count=200, id_stock=2)
sale_3 = Sale(price=50, data_sale="11-05-2023", count=150, id_stock=3)
sale_4 = Sale(price=150, data_sale="12-05-2023", count=300, id_stock=4)
sale_5 = Sale(price=100, data_sale="10-05-2023", count=200, id_stock=5)
sale_6 = Sale(price=100, data_sale="09-05-2023", count=500, id_stock=6)
sale_7 = Sale(price=200, data_sale="12-05-2023", count=600, id_stock=7)
sale_8 = Sale(price=350, data_sale="12-05-2023", count=700, id_stock=8)
sale_9 = Sale(price=150, data_sale="08-05-2023", count=300, id_stock=9)
sale_10 = Sale(price=100, data_sale="12-05-2023", count=500, id_stock=10)

session.add_all([sale_1, sale_2, sale_3, sale_4, sale_5, sale_6, sale_7])
session.add_all([sale_8, sale_9, sale_10])
session.commit()


publisher_name = input("Введите имя и фамилию писателя или его id\n")
print()
quer_pub = session.query(Book.title, Shop.name, Sale.count, Sale.data_sale).join(Publisher).join(Stock).join(Shop).join(Sale)
if publisher_name.isdigit():
    quer_pub2 = quer_pub.filter(Publisher.id == publisher_name).all()
else:
    quer_pub2 = quer_pub.filter(Publisher.name == publisher_name).all()


for title, name, count, date_sale in quer_pub2:
    print(f"{title:<30} | {name:<10} | {count:<5} | {date_sale}")

session.close()



