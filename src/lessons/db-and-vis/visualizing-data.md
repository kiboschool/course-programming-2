
## Visualizing Data

Please <a href="https://careerfoundry.com/en/blog/data-analytics/what-is-data-visualization/">read this page</a> for a good introduction to Data Visualization:

<a href="https://careerfoundry.com/en/blog/data-analytics/what-is-data-visualization/"><img align="center"  width="75%" height="75%" src="../../images/w6/datavis.png"></a>

In Python, there are a few tools that can be used to visualize data. This week we'll use a library called `matplotlib`.

In a terminal, run `py -m pip install matplotlib`, `python3 -m pip install matplotlib`, `python -m pip install matplotlib`, or use the way you have usually installed Python modules. (This is the way you have installed other modules like Requests).


### Histograms

A histogram depicts trends in data. It shows how frequently values fall into certain ranges. For example, let's say you want to know the most common song length for popular music. Are most popular songs about 4 minutes long?

We can answer the question by drawing a histogram.

Histograms are explained on the page [here](https://www.tibco.com/reference-center/what-is-a-histogram-chart).

We can add a script alongside our previous exploration scripts, that use matplotlib and the existing scripts to draw a histogram.

You can run this code to see a histogram of song lengths:

```python
import matplotlib.pyplot as pyplot
from pop_charts_exploration import *

def getDurations():
    durations = []
    exploration = PopChartsExploration('pop_charts_exploration.db')
    rows = exploration.session.query(PopCharts).all()
    for row in rows:
        durations.append(row.duration)
    
    return durations

def go():
    number_of_bins = 20
    durations = getDurations()

    pyplot.hist(durations, bins=number_of_bins)
    pyplot.show()
        
if __name__ == '__main__':
    go()

```

The `getDurations` function will use sqlalchemy to get a list of numbers, where each number is the length in seconds of a song. This list of numbers is passed to matplotlib's `pyplot.hist`, which automatically comes up with bins and draws the picture.

How long are most songs in the data set?

<!-- another possibility, histogram of goals-->


### Scatter Plots

Scatter plots can show the **correlation** between data. This means that there is a connection between the two types of statistical event.

For example, there is a correlation between a number of shots on goal, and how often a football team wins. They aren't 100% correlated, sometimes a team could take a lot of wild shots and not win the game. But in general, it's a sign of a good team that they take a lot of shots.

Sometimes, there isn't a correlation between events. For example, one could try to find a correlation between the color of the team uniform and how often a football team wins. There probably wouldn't be a very strong correlation.

It's very interesting to ask questions about correlation. It can help us, for example, determine how much home teams have an advantage.

The page [here](https://docs.tibco.com/pub/sfire-analyst/latest/doc/html/en-US/TIB_sfire-analyst_UsersGuide/scat/scat_what_is_a_scatter_plot.htm#:~:text=Scatter%20plots%20are%20used%20to,the%20X%20and%20Y%20axes.) describes what a **scatter plot** is.

Let's run scatter plots on the Football Player database.

```python

import matplotlib.pyplot as pyplot
from football_players_exploration import *

def iteratePlayers():
    caps = []
    goals = []
    exploration = FootballPlayersExploration('football_players_exploration.db')
    rows = exploration.session.query(Player).all()
    for row in rows:
        caps.append(row.caps)
        goals.append(row.goals)
    
    return caps, goals
    
def go():
    caps, goals = iteratePlayers()
    pyplot.scatter(caps, goals)
    pyplot.show()
    
if __name__ == '__main__':
    go()

```

This plot is with caps (appearences) on the x axis and goals on the y axis. There is kind of a relationship, but a strong correlation would show a straight line, and this is more of a cloud - it's not a strong correlation. This means that scoring more goals is linked to appearing more, but it's not a very strong link

<img align="center"  width="75%" height="75%" src="../../images/w6/plot1.png">

But if we filter to only looking at Forwards,

```python

import matplotlib.pyplot as pyplot
from football_players_exploration import *

def iteratePlayers(position):
    caps = []
    goals = []
    exploration = FootballPlayersExploration('football_players_exploration.db')
    rows = exploration.session.query(Player).filter(Player.position==position).all()
    for row in rows:
        caps.append(row.caps)
        goals.append(row.goals)
    
    return caps, goals
    
def go(position):
    caps, goals = iteratePlayers(position)
    pyplot.scatter(caps, goals)
    pyplot.show()
    
if __name__ == '__main__':
    go(position='FW')

```

<img align="center"  width="75%" height="75%" src="../../images/w6/plot2.png">

There is a stronger correlation. The data appears to be shaped in more of a line than a cloud. This makes sense, because forwards are expected to be scoring goals.


> Exercise:
> * Look inside the database and get the codes for different positions, such as `FW` for forward or `GK` for goalkeeper.
> * You can do this by opening the `.db` file in a tool like `DB Browser for Sqlite`, or by writing a script to loop through player rows and print out the `.position`.
> * Modify the script above, to make plots for each position.
> * Which appears to have the strongest correlation?
> * Which appears to have the weakest correlation?


