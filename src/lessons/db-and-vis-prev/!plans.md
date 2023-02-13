


------------------Page 1 "Database of songs", section 1----------------------
(not songlength)

First show a data set on songs.
with a json data set backing it.

schema:
song, artist, number_of_times_played
    (good thing about number_of_times_played = makes sense for it to be frequently incremented,
    for the perf test. otherwise less realistic to be repeatedly setting a value)
and can add the african ones to this one

initial methods:
show-number-of-plays
increment-number-of-plays
show-titles-by-artist
change-title
    intentional bug with a typo-but it saves to the db just fine, how to stop this?
    
show some example code using it

this is very similar to the persistedlist example we saw last week

challenge can you spot the bug?


------------------Page 1 "Database of songs", section 2 ----------------------

note - there is a bug but it saves without showing any error=bad

let's look at a database implementation. (don't convert the whole program, just create def functions)

one using sqlite, not with sqlalchemy yet

you will recognize sql from the webapp course.

    all you need is a few examples
    to show how to execute sqlite
    don't need to fully convert the json songs example, only do a couple queries


read the replit code and try running it.

talk a little bit about databases. sqlite runs on a simple file on your machine and it is built into python.

remember that commit commits it

bonus self.session.query(Song).filter(Song.song.ilike("%title%"))

------------------Page 2 "Advantages of databases" ----------------------

try calling the change-title- it shows an error right away!
this would catch the problem with the title typo, it would show an error right away
this is one benefit of db

why do the work to do this? one nice thing about the json version is that you can open it in a text file and see it.
in sqlite you'd have to use a program like 'db browser for sqlite' to do that.

(another example is that you don't need a bunch of loops to find the right row, code is simpler)

let's also try running this a lot of times (not on replit, which isn't a fair comparison)
and it's slow!
speed doesn't always matter but sometimes it does.

so it's about choosing the right approach for what you need

-faster(can benchmark it, why not!)
-and not restrained by limits in memory
-and has constraints on types that can be useful

as web foundaations alluded too, there are other advantages
- fast lookup with indexes
- multiple users connecting

Databases aren't magical - you could create one yourself if you had enough time


--------------------Page 3 ORM --------------------------------

We've been working on object oriented software... is there a way to work with databases
and objects?

What if we thought of a database row as an object. The internal data would be the columns. The behavior would be modifying the data and saving it back to the database.
This would be convenient because it puts the row state together on one object.
The syntax would look really pythonic - look similar to working with other objects - not having to construct sql strings.


Can also kind of think of the database table as an object too. The internal data is the rows, and it has behavior which is the queries, inserts, and deletes.

If you squint your eyes, it looks like this:
class SongsTable():
    def init():
        self.rows = []
    def insert(songsRow):
        self.rows.append(songsRow)
    def query():
    
class SongsRow():
    def init():
        self.title = ''
        self.artist = ''
        self.number_of_plays = 0
    def settitle
    def setartist
    def setnumberofplays

This feels a lot more pythonic.

But why write this code -- for each table it is the same --
and what if you already had a lot of tables- it is doing similar stuff
could this code be generated automatically?

This is what an ORM is!

It makes objects for the tables and rows.
Can look at models.py and see the classes.

Show in replit a version that uses an ORM

Tell them that the models.py file is complicated-don't worry, you 
won't really be expected to write a models.py from scratch.

We get the benefits of a database- but we don't need to build a string,
which doesn't really feel right with Python
And then when working with it they are objects which is nice.
And avoids chance of sql injection which is really bad. (bonus showing that)

show replit of sqlalchemy


Google docs slideshow showing the syntax, you click through it and it highlights the lines
showing how behind the scenes it becomes a SELECT


note that sqlalchemy runs on sqloite, postgres etc very similarly
it;s the great thoing about oop and abstravgfion - we are using sqlachlemy and don't have to eorru
about a l;otop f the db diffreences - abstracton laur!!!

--------------------Page 4 Querying data in sqlalchemy --------------------------------

show songs database from south african charts

have a challenge -- what do you think this code does?
answer: it finds the song that has been on the charts the longest

use order by to answer questions about the data
	Which one has biggest % increase
	Which one has biggest % decrease
Which one has been on the charts the longest (weeks on chart)

typeform to make a multiple choice quiz -----



--------------------Page 5 data visualization --------------------------------

explain correlation

installing matplotlib (like we installed sqlalchemy earlier)

Matplot lib a scatter plot -- 
    basic array example, shows a correlation
    
    basic array example, does not show a correlation


for the songs database plot total views vs num likes
plot 'total_views': 2250623, 'num_likes': 30866
it is correlated, usually the # of likes is related to # of views.
(one interpretation is that the songs that people like are popular and ppl watch them more
but just because they are correlated you can't completely draw a conclusion.
maybe the number of likes means that youtube's algorithm shows it to ppl more so it gets more views.
combination of factors.
)

Bonus: look up what a histogram is. here is the syntax for creating a histogram. draw one.


--------------------Page 6 football example --------------------------------

scatter plot with caps vs goals for forwards
note that there isn't a correlation really for all players
so that's part of data visualization - sometimes there isn't a strong correlation.

remember in web app talked about splitting a table into different tables.
could have a b a b a b
but split out the countries table. uses less space too which is nice.
link to there to talk about normalization.




EXCERSIZES:

What song has largest % increase in views? write a method to detremine it and run it to find out.
Make a plot of some data on either songs or football, and see if there is a correlation or not. Is there a correlation between length of song and number of likes?
Add an orm method for change artist like the change title one.








