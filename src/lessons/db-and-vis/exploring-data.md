
## Exploring Data

### Pop Charts

Please download these files, and place them in a folder on your computer, [pop_charts_exploration.db](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/pop-charts/pop_charts_exploration.db) and [pop_charts_exploration.py](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/pop-charts/pop_charts_exploration.py).

```python

from sqlalchemy import String, Integer, Column
from sqlalchemy import select, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class PopCharts(Base):
    __tablename__ = "PopCharts"
    id = Column(Integer, primary_key=True)
    youtube_link = Column(String())
    name = Column(String())
    artist = Column(String())
    time_on_chart = Column(Integer)
    change = Column(Integer)
    total_views = Column(Integer)
    num_likes = Column(Integer)
    duration = Column(Integer)
    views_this_week = Column(Integer)


class PopChartsExploration:
    def __init__(self, filename):
        self.engine = create_engine(f'sqlite:///{filename}', echo=False)
        Session = sessionmaker(self.engine)
        self.session = Session()
    
    def save(self):
        self.session.commit()
            
    def get_longest_song(self):
        result = (
            self.session.query(PopCharts)
            .order_by(PopCharts.duration.desc())
            .first())
            
        print(f'Found: {result.artist} - {result.name} {result.duration}')
        

if __name__ == '__main__':
    popChartsExploration = PopChartsExploration('pop_charts_exploration.db')
    popChartsExploration.get_longest_song()
    

```

This is based on real data from YouTube, ranking the currently most-popular music.

The Pop Charts are a list of the top 100 songs, ranked in order of popularity, which in this case is measured by the number of YouTube views.

As the `PopCharts` class shows, there are some columns like song name, artist, time_on_chart, and so on. 

* `time_on_chart` is the number of days the song has been ranked in the top 100. 
* `change` is the percentage increase or decrease in the number of views since last week.
* `total_views` is the total number number of YouTube views
* `views_this_week` is the number of weekly YouTube views
* `duration` is the length of the song in seconds
* `num_likes` is the number of Likes on the YouTube video

We can use our Python program to answer questions about the data. It can be fun to measure and look for trends in the data!

In a statistics course, we could perform measurements on the different values to answer questions like variance and average. For now, we'll just look at basic properties like highest and lowest values.

If we want to find the longest song, we can sort by duration in **descending** order and retrieve the first result. (The `.desc()` specifies sorting in this order, from largest value to smallest).

Similarly, if we want to find the longest song, we can sort by duration in **descending** order and retrieve the first result. (You could use `.asc()` to specify sorting in this order, from largest value to smallest).

Notice that SQLAlchemy is giving us many useful features, and we don't have to write any sql.

One caveat is to remember to indicate the primary key. Tables in a relational database usually have an `id` column. This id is also referred to as the *primary key*. SQLAlchemy expects at least one of the columns to be marked with `primary_key=True`, or it will throw an error when your program runs.

> Exercise:
> * modify the code so that it finds the song that has been ranked in the top 100 for the shortest amount of time. 
> * then run the program and get the artist and name of that song.

### Football Players

Please download these files, and place them in a folder on your computer, [football_players_exploration.db](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/football/football_players_exploration.db) and [football_players_exploration.py](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/football/football_players_exploration.py).

```python
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy import select, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Player(Base):
    __tablename__ = "Players"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    name_normalized = Column(String())
    caps = Column(Integer)
    goals = Column(Integer)
    most_recent_year_played = Column(Integer)
    position = Column(String())
    year_born = Column(Integer)
    club = Column(String())
    club_nationality = Column(String())
    played_in_latest = Column(String())
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    
class Country(Base):
    __tablename__ = "Countries"
    country_id = Column(Integer, primary_key=True)
    county_name = Column(String())


class FootballPlayersExploration:
    def __init__(self, filename):
        self.engine = create_engine(f'sqlite:///{filename}', echo=False)
        Session = sessionmaker(self.engine)
        self.session = Session()
    
    def save(self):
        self.session.commit()
            
    def get_most_goals(self):
        result = (
            self.session.query(Player)
            .order_by(Player.goals.desc())
            .first())
            
        print(f'Found: {result.name} - {result.goals}')
        

if __name__ == '__main__':
    footballPlayersExploration = FootballPlayersExploration('football_players_exploration.db')
    footballPlayersExploration.get_most_goals()
    

```

This is real data that was scraped from Wikipedia. It contains player information for world cup football matches.

If we want to find the player who scored the most goals, we can sort by goal scored in descending order and retrieve the first result.

(There are many players who aren't included in this data set).

Please run the script, and see the answer. 

Note that this database has two tables, one for Players and one for Countries. Programmers often create databases this way, splitting the data into different tables. You might remember that this is called [normalization](https://web-app-development.vercel.app/lessons/data-modeling/relations-and-normalization.html).

> Bonus challenge:
> * modify the code so that it does another query in `get_most_goals` to determine and display the country name.
> * remember that you can run queries by writing code that looks like this,
>   * `result = self.session.query(Table).filter_by(column_name=value).first()`

