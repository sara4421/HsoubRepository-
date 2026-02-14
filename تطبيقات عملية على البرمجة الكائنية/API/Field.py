from abc import ABC

class Field(ABC):
    field_type = None

    def __init__(self, max_length=225, unique=None):
        if unique is True:
            self.unique = 'UNIQUE'
        else:
            self.unique = ''

        if max_length:
            self.max_length = max_length

    def __repr__(self):
        column = []
        if self.field_type == 'VARCHAR':
            column.append(f'VARCHAR ({self.max_length})')
            # التابع هنا لا يقوم بإرجاع قيمة

        else:
            column.append(self.field_type)
            column.append(self.unique)
            return ''.join(column).strip() # الخلل موجود في هذا السطر
        return ''.join(column).strip() # يجب أن يكون هكذا

class CharField(Field):
    field_type = 'VARCHAR'

    def __init__(self, max_length=225, unique=None):
        self.max_length = max_length
        self.unique = unique
        super().__init__(max_length=max_length, unique=unique)

class TextField(Field):
    field_type = 'TEXT'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)

class IntegerField(Field):
    field_type = 'INTEGER'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)

class FloatField(Field):
    field_type = 'REAL'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)

class BooleanField(Field):
    field_type = 'INTEGER'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)

class DateTimeField(Field):
    field_type = 'INTEGER'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)