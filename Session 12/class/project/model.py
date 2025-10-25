from sqlalchemy import create_engine, text, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# 1| sakhte engine - rabete ma baraye etesal python be mysql be vasete sqlalchemy
# + connection string -> darvaqe be on str dakhele dastore create_engine migim
# ke be vaseteye on miaim va vasl mishim be mysql
engine = create_engine("mysql+mysqlconnector://root:root1234@localhost")

# 2| sakhte db agar ke nist ba engine ke az qabl darim
# + with -> estefade mikonim az in dastor python ke otomat bebande in connection ro
# + as conn -> natijeye dastor connect ro dakhelesh zakhire mikonim ta badan estefade konim
# + execute -> dastorat maro mibare dakhele db va ejra mikone
# + text -> chizi ke dakhelesh bedi ro mifahmone be alchemy ke ye dastor sql vaqeyi hast (raw sql)
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS student_db_test"))

# 3| hala ke db ro sakhtim miaim va be on db jadidemon vasl mishim va akhar on
# connection string ke dadim be dastor create_engine ezafash mikonim -> "/db_name"
engine = create_engine("mysql+mysqlconnector://root:root1234@localhost/student_db_test")

# 4| in ye class misaze ke kole model ha azash bayad ers bebaran va ba in kar
# class haye ma mitonan az qodrate orm estefade konan va intori on class ma mishe ye
# table toye db va attributes hari mizare soton haye jadavel va mohem tar az hame
# maid va toye metadata zakhire mikone class ro ke akhare kar betonim on jadavel ro
# besazim
Base = declarative_base()

# 5| Session -> darvaqe miaim va ba sessionmaker ye karkhoneye tolid kargare robati misazim
# va badesh az roye on miaim va ye robat baraye khodemon tolid mikonim be esm samad va azinja bebad
# on samad miad karhaye CRUD maro baramon anjam mide
# + session_maker() -> ye function hast ke miazare ma karkhoneye tolid robat besazim
# + bind=engine -> mige hameye in kargara badan bayad roye kodom db kar konan ba che moshakhasti
# + samad -> ye nemone robate karegare ke mitone baraye ma kar kone va be db vasl beshe va dastorat ro
# ejra kone baramon.
RobotFactory = sessionmaker(bind=engine)
samad = RobotFactory()


# 6| sakhte ye model be shekli ke alchemy on ro befahme va motevaje beshe
# + Base -> hamon classi hast ke aval sakhtim va ba ersbari az on alchemy in class ro
# be onvane ye table mishnase va attr haye ono ye soton dar nazar migire
# + __tablename__ -> ba in esm jadval ro moskhasa mikoni ke age nadi miad va esm
# khode calss ro barmidare va lower case mikone
# + Column -> miad va mige in attr ha harkdom ke soton toye jadval ma hast
# + __repr__ -> ye magic method hast ke age __str__ nabashe va print koni ye obj az
# in class ro miad va namayesh dade mishe ke syntax neveshtan matn toye on in sheklie:
# <Class name(--attrs--)>
# va in baraye programmer ha va developeras ke bebinan va motevaje beshan che khabare
# toye in calss va baraye didan ham age __str__ nveshte bodi
# mitoni biai obj haro bezari toye list ya dict
# bade print seda zade mishe va ya khodesho mostaqim roye obj seda bezani intori
# obj.__repr__
# va ya toye console khode obj ro seda bezani hame
class Student(Base):
    __tablename__ = "students"  # table name in MySQL

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    score = Column(Float, nullable=False)

    def __str__(self):
        return f"[{self.name}, {self.last_name}, {self.age}, {self.score}]"


    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, last_name={self.last_name}, age={self.age}, score={self.score})>"


# 7| dar akhar baraye save va zakhire tamame data ha va table ha va column ha
# miaim va metadata ro seda mizanim ta hamaro besaze
Base.metadata.create_all(engine)