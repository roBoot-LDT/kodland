from sqlalchemy.sql.expression import table
from .db import sess
from . import tables


class TableWrapper:
    def __init__(self, table):
        self.table = table

    @property
    def keys(self):
        return [str(item).split('.')[-1] for item in self.table.__table__.columns]

    def _print_row(self, row):
        for key in self.keys:
            print(getattr(row, key), end=' | ')
        print()

    def show(self, key=None, val=None):
        # Вывод на консоль 1 строки из БД
        if val is not None and key is not None:
            row = self.get(key, val)
            if row:
                print(' | '.join(self.keys))
                self._print_row(row)
            else:
                print(f'Такого значения {val} в столбце {key} нет')
            return

        data = self.get_all()
        # Вывод столбца на консоль
        if key is not None:
            print(key)
            for row in data:
                print(getattr(row, key))
            return 

        # Вывод всей таблицы
        print(' | '.join(self.keys))
        for row in data:
            self._print_row(row)

    def put(self, data):
        sess.add(self.table(**data))
        sess.commit()

    def delete(self, key, val):
        sess.query(self.table).filter(getattr(self.table, key) == val).delete()
        sess.commit()

    def update(self, key, old_val, new_val):
        sess.query(self.table).filter(getattr(self.table, key) == old_val).\
            update({key: new_val})
        sess.commit()

    def get(self, key, val):
        return sess.query(self.table).filter(getattr(self.table, key) == val).first()

    def get_all(self):
        return sess.query(self.table).all()


class DataBase:
    t = {}

    def __init__(self):
        for attr_desc in dir(tables):
            attr = getattr(tables, attr_desc)
            if hasattr(attr, '__tablename__'):
                self.t[attr.__tablename__] = attr

    def __getattr__(self, attr):
        if attr in self.t:
            return TableWrapper(self.t[attr])
        else:
            raise AttributeError(f'Таблицы {attr} в базе данных не существует')

    @property
    def tables(self):
        return list(self.t.keys())

   