from DataBase import DataBase
from m import Model
from Field import *

Model.db = DataBase('database.sqlite')
Model.connection = Model.db.connect()


class Post(Model):
    title = CharField()
    body = TextField()
    created_at = DateTimeField()
    published = BooleanField()


class User(Model):
    first_name = CharField()
    last_name = CharField(max_length=250)
    age = IntegerField()


if __name__ == '__main__':
    # post = Post()
    print(Post.get(1))
