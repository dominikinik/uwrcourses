import sys
from datetime import datetime
from sqlalchemy.orm import sessionmaker, validates
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  DateTime


baza = declarative_base()


class filmy(baza):
    __tablename__ = 'filmy'
    id = Column(Integer, primary_key=True)

    tytul = Column(String, unique=False, nullable=False)

    rok = Column(Integer, unique=False, nullable=False)

    rezyser = Column(String, unique=False, nullable=False)

    operator = Column(String, unique=False, nullable=False)

    producent = Column(String, unique=False, nullable=False)

    data_dodania = Column(DateTime, default=datetime.now())

    @validates("rok")
    def validate_wykonawca(self, key, rok):
        if int(rok) > 1850:
            return rok

    def __repr__(self):
        return f'<tytul: {self.tytul}, rok: {self.rok}>'


class muzyka(baza):
    __tablename__ = 'muzyka'
    id = Column(Integer, primary_key=True)

    tytul = Column(String, unique=False, nullable=False)

    rok = Column(Integer, unique=False, nullable=False)

    wykonawca = Column(String, unique=False, nullable=False)

    wytwornia = Column(String, unique=False, nullable=False)

    klip = Column(String, unique=False, nullable=False)

    data_dodania = Column(DateTime, default=datetime.now())

    @validates("wykonawca")
    def validate_wykonawca(self, key, wykonawca):
        if "Ariana" in wykonawca:
            return wykonawca

    def __repr__(self):
        return f'<tytul: {self.tytul}, rok: {self.rok}>'


class obrazy(baza):
    __tablename__ = 'obrazy'
    id = Column(Integer, primary_key=True)

    tytul = Column(String, unique=False, nullable=False)

    rok = Column(Integer, unique=False, nullable=False)

    autor = Column(String, unique=False, nullable=False)

    kraj = Column(String, unique=False, nullable=False)

    rodzaj = Column(String, unique=False, nullable=False)

    data_dodania = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f'<tytul: {self.tytul}, rok: {self.rok}>'

    @validates("kraj")
    def validate_kraj(self, key, kraj):
        if "Francja" in kraj:
            return kraj


def query(**kwargs):
    tabla = kwargs['co']
    engine = create_engine('sqlite:///database.db', echo=False)
    baza.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    if kwargs['flag'] == '--dodaj':
        if tabla == "obrazy":
            nowecos = obrazy(tytul=kwargs['tytul'], rok=kwargs['rok'],
                             autor=kwargs['info1'], kraj=kwargs['info2'], rodzaj=kwargs['info3'])
        elif tabla == "filmy":
            nowecos = filmy(tytul=kwargs['tytul'], rok=kwargs['rok'], rezyser=kwargs['info1'],
                            operator=kwargs['info2'], producent=kwargs['info3'])
        elif tabla == "muzyka":
            nowecos = muzyka(tytul=kwargs['tytul'], rok=kwargs['rok'],
                             wykonawca=kwargs['info1'], wytwornia=kwargs['info2'], klip=kwargs['info3'])
        session.add(nowecos)
        session.commit()
        print('data_dodania : ', nowecos)

    elif kwargs['flag'] == '--usun':
        if tabla == "filmy":
            filmyy = session.query(filmy)
            pom = [filmy.tytul, filmy.rok, filmy.rezyser,
                   filmy.operator, filmy.producent]
        elif tabla == "obrazy":
            filmyy = session.query(muzyka)
            pom = [muzyka.tytul, muzyka.rok, muzyka.wykonawca,
                   muzyka.wytwornia, muzyka.klip]
        elif tabla == "muzyka":
            filmyy = session.query(obrazy)
            pom = [obrazy.tytul, obrazy.rok,
                   obrazy.autor, obrazy.kraj, obrazy.rodzaj]

        for i, j in enumerate(kwargs['params']):
            filmyy = filmyy.filter(pom[i] == j)

        filmyy = filmyy.all()

        for j in filmyy:
            session.delete(j)
        session.commit()

    elif kwargs['flag'] == '--wypisz':
        if tabla == "filmy":
            print(' filmy:')
            cos = session.query(filmy).all()
            for i in cos:
                print(
                    f'<tytul: {i.tytul}, rok: {i.rok}, 'f'rezyser: {i.rezyser},'f'operator: {i.operator}, producent: {i.producent}>')
        if tabla == "obrazy":
            print(' obrazy:')
            cos = session.query(obrazy).all()
            for i in cos:
                print(
                    f'<tytul: {i.tytul}, rok: {i.rok}, 'f'autor: {i.autor},'f'kraj: {i.kraj}, rodzaj: {i.rodzaj}>')
        if tabla == "muzyka":
            print(' muzyka:')
            cos = session.query(muzyka).all()
            for i in cos:
                print(
                    f'<tytul: {i.tytul}, rok: {i.rok}, 'f'wykonawca: {i.wykonawca},'f'wytwornia: {i.wytwornia}, klip: {i.klip}>')
    elif kwargs['flag'] == '--znajdz':
        if tabla == "filmy":
            filmyy = session.query(filmy)
            pom = [filmy.tytul, filmy.rok, filmy.rezyser,
                   filmy.operator, filmy.producent]
        elif tabla == "obrazy":
            filmyy = session.query(muzyka)
            pom = [muzyka.tytul, muzyka.rok, muzyka.wykonawca,
                   muzyka.wytwornia, muzyka.klip]
        elif tabla == "muzyka":
            filmyy = session.query(obrazy)
            pom = [obrazy.tytul, obrazy.rok,
                   obrazy.autor, obrazy.kraj, obrazy.rodzaj]

        for i, j in enumerate(kwargs['params']):
            filmyy = filmyy.filter(pom[i] == j)

        filmyy = filmyy.all()

        for i, j in enumerate(filmyy):
            print(f'{i + 1}. {j}')
    else:
        print('blad :c: ', kwargs)
        exit()

    session.close()


def info():
    print('--dodaj kategoria(obrazy,filmy,muzyka) tytul rok info1  info2  info3')
    print('--usun kategoria informacja')
    print('--znajdz kategoria  arg')
    print('--wypisz kategoria')


def bladkomendy():
    args = ' '.join(sys.argv[1:])
    print(f'idk: "{args}"')
    info()


if __name__ == '__main__':

    if sys.argv[1] == '--dodaj':
        query(flag='--dodaj', co=sys.argv[2], tytul=sys.argv[3], rok=sys.argv[4],
              info1=sys.argv[5], info2=sys.argv[6], info3=sys.argv[7])

    elif sys.argv[1] == '--usun':
        query(flag='--usun', co=sys.argv[2], params=sys.argv[3:])

    elif sys.argv[1] == '--znajdz':
        query(flag='--znajdz', co=sys.argv[2], params=sys.argv[3:])

    elif sys.argv[1] == '--wypisz':
        query(flag='--wypisz', co=sys.argv[2])

    elif sys.argv[1] == '--help':
        info()

    else:
        bladkomendy()
