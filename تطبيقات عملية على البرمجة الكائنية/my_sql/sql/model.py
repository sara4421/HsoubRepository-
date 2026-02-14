# model.py

class Model:
    db = None
    connection = None

    def __init__(self):
        self._create_table()
        self._saved = False

    @classmethod
    def get_table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def get_columns(cls):
        columns = {}
        for key, value in cls.__dict__.items():
            if str(key).startswith('_'):
                continue
            columns[str(key)] = str(value)
        return columns

    def _create_table(self):
        if not self.connection:
            raise ValueError("No database connection")
        columns = ', '.join([f"{key} {value}" for key, value in self.get_columns().items()])
        sql = f"CREATE TABLE IF NOT EXISTS {self.get_table_name()} (ID INTEGER PRIMARY KEY AUTOINCREMENT, {columns})"
        cursor = self.connection.cursor()
        result = cursor.execute(sql)
        return result

