# Exploring Data

You've seen how to connect to a database and use an ORM to model tables and rows. In this lesson, you'll see a bit more about how to use an ORM to explore data and answer questions.

There are two explorations here: one for pop music data and one for football statistics.

> **Follow along** with the examples below. Download the files, run the code, and make changes to experiment with the data and the program.

## Pop Charts

The Pop Charts are a list of the top 100 songs, ranked in order of popularity, which in this case is measured by the number of YouTube views.

This is based on real data from YouTube, ranking the currently most-popular music.

Download these files, and place them in a folder on your computer: 
- [pop_charts_exploration.db](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/pop-charts/pop_charts_exploration.db)
- [pop_charts_exploration.py](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/pop-charts/pop_charts_exploration.py).

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


As the `PopCharts` class shows, there table has columns for each song, like the song's name and artist. 

* `time_on_chart` is the number of days the song has been ranked in the top 100. 
* `change` is the percentage increase or decrease in the number of views since last week.
* `total_views` is the total number number of YouTube views
* `views_this_week` is the number of weekly YouTube views
* `duration` is the length of the song in seconds
* `num_likes` is the number of Likes on the YouTube video

We can use our Python program to answer questions about the data. It can be fun to measure and look for trends in the data!

In a statistics course, we could perform measurements on the different values to answer questions like variance and average. For now, we'll just look at basic properties like highest and lowest values.

If we want to find the longest song, we can sort by duration in **descending** order and retrieve the first result. The `.desc()` method specifies sorting in this order, from largest value to smallest.

Similarly, if we want to find the shortest song, we can sort by duration in **ascending** order and retrieve the first result. You can use `.asc()` to specify sorting in this order, from smallest value to largest.

Notice that SQLAlchemy is giving us access to many useful database features, without having to write the SQL by hand.

Tables in a relational database usually have an `id` column that serves as the *primary key*. SQLAlchemy expects at least one of the columns to be marked with `primary_key=True`, or it will throw an error when your program runs.

### Try it yourself: Pop Charts 

Practice working with the Pop Charts data.

If you hadn't already done so, download [pop_charts_exploration.db](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/pop-charts/pop_charts_exploration.db) and [pop_charts_exploration.py](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/pop-charts/pop_charts_exploration.py).

Use the SQLAlchemy ORM to generate queries to answer the following questions:

* How many songs are in the pop charts database?
* What is the most liked song?
* What is the most viewed song?
* What are the 10 top trending songs? (Hint: Find the songs with the largest percentage increase in views this week.)
* What song that has been ranked in the top 100 for the shortest amount of time?

### Football Players

This is real data, scraped from Wikipedia. It contains player information for World Cup football matches. There are many players who aren't included in this data set.

Download these files, and place them in a folder on your computer: 
- [football_players_exploration.db](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/football/football_players_exploration.db)
- [football_players_exploration.py](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/football/football_players_exploration.py).

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

If we want to find the player who scored the most goals, we can sort by goal scored in descending order and retrieve the first result.

Run the script, and see the answer. 

This database has two tables, one for Players and one for Countries. Programmers often create databases this way, splitting the data into different tables. You might remember that this is called [normalization](https://web-app-development.vercel.app/lessons/data-modeling/relations-and-normalization.html).

## Try it yourself: Football Players

Practice working with the Football Players data.

If you hadn't already done so, download [football_players_exploration.db](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/football/football_players_exploration.db) and [football_players_exploration.py](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/football/football_players_exploration.py).

Use the SQLAlchemy ORM to generate queries to answer the following questions:

* What country did the player with the most goals play for? After finding the player with the most goals in `get_most_goals`, write another query to find that player's country (you can use a query by country id, or add a [SQLAlchemy relationship](https://docs.sqlalchemy.org/en/14/tutorial/orm_related_objects.html#tutorial-orm-related-objects))
* What 10 players have the most caps?
* What country has the most goals scored by its players? (This will require [grouping and aggregating](https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#aggregate-functions-with-group-by-having)).
