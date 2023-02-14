
## ORM Syntax

You will first need to install SQLAlchemy if it is not already installed.

In a terminal, run `py -m pip install sqlalchemy`, `python3 -m pip install sqlalchemy`, `python -m pip install sqlalchemy`, or use the way you have usually installed Python modules. (This is the way you have installed other modules like Requests).

Here is our songs program, updated to use the ORM called SQLAlchemy:

```python
from sqlalchemy import String, Integer, Column
from sqlalchemy import select, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Song(Base):
    # these lines look unusual, they're just telling sqlalchemy what the table name and columns are
    __tablename__ = "Songs"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    artist = Column(String())
    times_listened_to = Column(Integer)
    
    # from now on we can have rows that are an instance of the Song class.
    # we can think of a row as being an instance of Song, and the attributes are the columns.

class SongListUsingOrm:
    def __init__(self, filename):
        self.engine = create_engine(f'sqlite:///{filename}', echo=False)
        Session = sessionmaker(self.engine)
        self.session = Session()
    
    def save(self):
        self.session.commit()
            
    def get_song_id(self, song_name):
        result = self.session.query(Song).filter_by(name=song_name).first()
        if result:
            return result.id
        else:
            print('Song not found')
            return None
        
        
    def show_times_listened_to(self, song_id):
        result = self.session.query(Song).filter_by(id=song_id).first()
        if result:
            return result.times_listened_to
        else:
            print('Song not found')
            return None
        
        
    def increase_times_listened_to(self, song_id):
        result = self.session.query(Song).filter_by(id=song_id).first()
        if result:
            result.times_listened_to += 1
            self.save()
        else:
            print('Song not found')
            return None
```

### SQLAlchemy Schema

After installing and configuring SQLAlchemy, you need to tell the ORM about the tables and columns in the database.

To tell SQLAlchemy about a table, you create a class called a *SqlAlchemy model*. Models aren't standalone classes; they inherit from the SQLAlchemy *Base*.

```python
class Song(Base):
    __tablename__ = "Songs"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    artist = Column(String())
    times_listened_to = Column(Integer)
```

This would correspond to a table like this in SQL:

```sql
CREATE TABLE Songs (
  id INTEGER PRIMARY KEY,
  name TEXT,
  artist TEXT,
  times_listened_to INTEGER
);
```
 
Don't worry if the model class is hard to understand. You won't be asked to create a model class like this from scratch. When learning to use libraries, one strategy is to copy from an existing example and modify it to fit your new situation.

The code for creating an engine also looks unusual. Again, you can think of this as boilerplate, and copy it to each of your projects. SQLAlchemy has laid out the code like this to allow people to create different types of connections and different types of sessions, but the defaults work fine for us.

```python
self.engine = create_engine(f'sqlite:///{filename}', echo=False)
Session = sessionmaker(self.engine)
self.session = Session()
```

This is similar what you had to do with the SQLite library, dealing with connections and cursors.

### Bonus: More about SQLAlchemy

SQLAlchemy is a good example of object-oriented programming for another reason: it abstracts over the underlying database.

In the midterm, you made subclasses that could run in different modes. The calling code remained the same, but the child class would have slightly different behavior, like measuring statistics. 

In a similar way, SQLAlchemy internally has different implementations that connect to different database systems. If your Python program interacts with a database through SQLAlchemy, it would only take a few lines of changes to change the database from SQLite to Postgres or MySQL or another system. 

This is great! Your program can easily adapt. A common use case is to use SQLite when developing locally, then Postgres in the deployed application. You only need a minor change to which code runs on your computer vs running in the cloud to use an entirely different database.

## Further Reading: SQLAlchemy

You can follow an in-depth SQLAlchemy tutorial here: [https://leportella.com/sqlalchemy-tutorial/](https://leportella.com/sqlalchemy-tutorial/)
