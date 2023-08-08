# Reading data from an internet API

Let's talk about reading data from the internet.

## Review: URLs and HTTP

A **URL** identifies a resource on the internet. 

You have seen URLs often, like `https://google.com`. In your web browser, when 
you click on the address bar at the top, you see the URL for the current page. An internet 
URL always starts with `http://` or `https://`, but sometimes the browser 
doesn't show that part. 

The URL for this course website is `https://programming-2.vercel.app/programming-2.html`.

To retrieve a web page, a program sends a **request**. Behind the scenes, your 
web browser is constantly sending out requests to get pages to display.

As you learned in Web Foundations, websites are built with **HTML**. The browser 
sends a request for a URL, and the server, sends back a page of HTML. The browser
interprets this HTML code and shows it on the screen.

A Python script can send requests to retrieve a webpage from the internet, just 
like your browser can. As you can see in the example, one library you can use to 
make requests is `urllib`. 

This code retrieves the homepage of the course website, and writes it to a file:

```python
import urllib.request
def main():
  url = 'https://programming-2.vercel.app/programming-2.html'
  results = urllib.request.urlopen(url)
  html_content = results.read().decode('utf-8')
  with open('output.html', 'w') as f:
    f.write(html_content)

main()
```

Try running this example! 

It will create a file named `output.html`. Open `output.html` in your editor to 
see the HTML code, or open it in your browser to see the rendered webpage.

In this situation, our Python program is acting as the "client" that sends a 
request to the server. The server sends the response back.

<image src="../../images/w1/server-combined.png" height="50%" width="50%" style="border:none, border-width: 0, border: 0; box-shadow: 0px 0px;" />

## Static and Dynamic pages

Some webpages remain the same over time. Every time I get the contents of "https://programming-2.vercel.app/programming-2.html" I get the same HTML code back. The webpage has not changed.

Other webpages can change each time a request comes in. For example when I check my email I always go to the same URL, "https://mail.google.com/mail/u/0/#inbox". But even though each time I am going to the same URL, I will see different items on the page. The server sends back a response with different information.

Or, if I am not logged into my email account, the results will come back with an error saying "unauthorized". The same error will happen if I try to read from mail.google.com in Python. It's trickier to use Python to send requests to webpages where you need to log in; we won't cover how to do that yet.

### Practice: Making Requests From Python

* Run the example code above and look at the `output.html` file.
* Modify the example code so that it gets the Wikipedia page for the country you live in. (You can get the url from your web browser - click on the address bar at the top of your brower to see the url and copy it).
* Modify the code so that it fetches a non-existing url, and run the program. What happens?

## Scraping Web Data

<img src="../../images/w1/tomato.png" height="50%" width="50%" style="border:none, border-width: 0, border: 0; box-shadow: 0px 0px;" />

Let's imagine that I am growing a tomato plant in a big pot. From my experience 
growing plants, I know that tomato plants shouldn't be left in cold weather 
outside, because this can hurt the plant. I'm living in an area where the weather 
gets cold sometimes.

Every day I open my laptop, go to Google, and search for the weather forecast. 
I'll see if the forecast will get below 12 degrees celsius in the next few days 
and make plans to bring the plant inside if I need to.

This is a repetitive task, to open the web browser, search for the forecast, and 
look for the days with a temperature below a certain amount. Because I can write 
programs in Python, maybe there is a way I can write a program to check the 
weather automatically for me!

I could try using the example code earlier on this page. First, I'd find the 
right url to call. This url might work:
`https://weather.com/en-KE/weather/tenday/l/Nairobi+Nairobi?placeId=e1d0bb735632de2df082e02f88493ef295908714761728c5c7d5d6c76cb2f83e`.
Then, I'd have my program request this url. When I get the HTML back, I'd set my 
program to look through the HTML to find the temperature information I need.

Theoretically, this plan would work. After all, this is what the web browser is 
doing behind the scenes to get the data. 

There are some problems, though.

* First, when we look at output.html, we see a bunch of junk! It's all html that is designed for a browser to draw on the screen. There is so much extra information involved, it will take us a while to write a program to filter down to what we want.
* Second, once we've written all of that filtering code, the website might make some changes and cause the filtering to not work anymore. Often, websites add a new feature or update the site, and our code will break, until we update it to make the filtering work again.
* Third, many websites don't want programs to automatically look at their data. They try to block Python from getting the website. Programs looking at their data might send many requests, which would slow down the website. Even many Google pages block programmatic access.

Finding data in html that was designed for a browser is called **scraping**. Since it's so annoying, programmers try to avoid having to do it whenever possible.

<image src="../../images/w1/puttyknife.png" height="25%" width="25%" style="border:none, border-width: 0, border: 0; box-shadow: 0px 0px;" />

## Using APIs

Fortunately, some servers are designed for programs connect to them, which 
eliminates these problems. 

This is called an Application Programming Interface: an **API**. An organization 
will create a web API by setting up a server that listens for requests to 
particular URLs. If a program sends a request to one of these URLs, the server 
sends back data in response.

Many APIs send back data in JSON format, which is perfect for us!

Why this is better than scraping:

* APIs do not send html back, or anything intended to be shown by the browser. They send only the data that you need. For example, instead of sending text and graphics back, they could send just a list of numbers.
* APIs keep their output structure the same. The organization providing an API will be careful not to make changes that would cause your program to stop working. For example, if the API documentation says that the API will respond with a dictionary, it won't change a few weeks later to respond with a list instead.
* An API can monitor how often it is being called, and block anything that is requesting it too often. An API can also restrict access to only authorized users, but we won't need need to worry about that in this project.

You can type an API url into the address bar for your browser and see the results there. But you'll just see raw data, so it isn't very useful. The intention an API is for programs, not people, to see it.

Fortunately for my tomato plant project, there is a free API that any program can send requests to, that will respond with the weather forecast. I can write a program to automatically look at the weather forecast! And the data will be in json format, which we already know how to work with.

Watch the video in the next section, to see how to update the weather program 
we've been working on to get real weather information from the internet.
