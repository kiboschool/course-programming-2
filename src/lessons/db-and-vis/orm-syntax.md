
## ORM Syntax

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

### How to set up SQLAlchemy

Telling SQLAlchemy about a table is done by creating a class called a *SqlAlchemy model*. Notice that the class isn't a normal standalone class, it is a class that inherits from *Base*.

Don't worry if the model class is hard to understand, you won't really be asked to create a model class like this from scratch. When learning very new lines of code like this, the best strategy is to copy from an existing example and modify it to fit the new situation.

The code for creating an engine also looks unusual, the lines with `create_engine`. Again, you can think of this as boilerplate, and copy it to each of your projects. (SQLAlchemy has laid out the code like this to allow people to create different types of connections and different types of sessions, but the defaults work fine for us).

### Bonus: More about SQLAlchemy

SQLAlchemy is a good example of object-oriented programming for another reason. Remember in the midterm when we made subclasses that could run in different modes. The calling code remained the same, but the child class would have slightly different behavior, like measuring statistics. In a similar way, SQLAlchemy internally has different implementations that connect to different database systems. So if your Python program interacts with a database through SQLAlchemy, it would only take a few lines of code changed to make it interact with a SQLite system, a Postgres system, a MySQL system, and so on. This is great because your program can easily adapt - you make only a minor change to your code running on your computer vs running in the cloud, running with a small amount of data vs running with large data sets.

(You can read in-depth information about SQLAlchemy here, https://leportella.com/sqlalchemy-tutorial/).

