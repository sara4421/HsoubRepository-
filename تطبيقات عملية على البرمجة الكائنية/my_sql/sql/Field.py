from abc import ABC

class Field(ABC):
    filetype = None

    def __init__(self, max_length=255, unique=None):
        self.unique = 'UNIQUE' if unique else ''
        if max_length:
            self.max_length = max_length

    def __repr__(self):
        column = []
        if self.filetype == 'VARCHAR':
            column.append(f'VARCHAR({self.max_length})')
        else:
            column.append(self.filetype)
        column.append(self.unique)
        return ' '.join(column).strip()


class Char(Field):
    filetype = 'VARCHAR'
    def __init__(self, max_length=255, unique=None):
        super().__init__(max_length=max_length, unique=unique)


class Text(Field):
    filetype = 'TEXT'
    def __init__(self, unique=None):
        super().__init__(unique=unique)


class Integer(Field):
    filetype = 'INTEGER'
    def __init__(self, unique=None):
        super().__init__(unique=unique)

