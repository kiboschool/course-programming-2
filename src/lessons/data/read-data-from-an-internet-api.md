# Read Data From An Internet API

## Reading From the Internet

Let's talk about reading data from the internet.

The technical term for the string that identifies a webpage is called the **URL**. You have seen URLs often, for example when we see google.com, this refers to the URL `https://google.com`. When you are in your web browser (Chrome, Safari, or Firefox) and you click on the address bar at the top, you will see the URL for the current page. (An internet URL always starts with `http://` or `https://`, but sometimes the browser doesn't show that part). The URL for the Kibo website is `https://programming-2.vercel.app/programming-2.html`.

The technical term for retrieving a web page is sending a **request**. Behind the scenes, your web browser program (Chrome, Safari, or Firefox) is constantly sending out **requests** to get the webpages you are looking at.

Remember that websites are built with **HTML**. Your browser sends a request for a certain URL of the page you are on. The internet server then responds to the request by sending over html code. The browser then interprets this **HTML** code and shows it on the screen.

A Python script can send requests to retrieve a webpage from the internet. This is one of the reasons Python is a powerful and useful language. As you can see in the example, the name for the library to do this is called `urllib`. By running this code, you can retrieve the main Kibo website,

```
import urllib.request
def main():
    url = 'https://programming-2.vercel.app/programming-2.html'
    results = urllib.request.urlopen(url)
    html_content = results.read().decode('utf-8')
    with open('output.html', 'w') as f:
        f.write(html_content)

main()

```

You can try running this example! It will create a file named `output.html`. Try opening `output.html` and see the HTML code inside.

Some webpages remain the same over time. Every time I get the contents of "https://programming-2.vercel.app/programming-2.html" I get the same HTML code back. The webpage has not changed.

Other webpages can change each time a request comes in. For example when I check my email I always go to the same URL, `https://mail.google.com/mail/u/0/#inbox`. But even though each time I am going to the same URL, I will see different items on the page. The server sends back a response with different information.

Or, if I am not logged into my email account, the results will come back with an error saying "unauthorized". The same error will happen if I try to read from mail.google.com in Python. It's trickier to use Python to send requests to webpages where you need to log in; we won't cover how to do that yet.

Exercises:
* Run the example code above and look at the `output.html` file.
* Modify the example code so that it gets the Wikipedia page for the country you live in. (You can get the url from your web browser - click on the address bar at the top of your brower to see the url and copy it).
* Try entering a non-existing url and running the program. What happens?

## What is an API

Let's imagine, as an example, that I am growing a tomato plant. From my experience growing plants, I know that tomato plants shouldn't be left in cold weather outside, because this can hurt the plant. I'm living in an area where the weather gets cold sometimes.

Every day I open my laptop, go to Google, and search for the weather forecast. I'll see if the forecast will get below 12 degrees celsius in the next few days and make plans to bring the plant inside if I need to.

This is a repetitive task, to open the web browser, search for the forecast, and look for the days with a temperature below a certain amount. Because I can write programs in Python, maybe there is a way I can write a program to check the weather automatically for me!

I could try using the example code earlier on this page. I'd find the right url to call, for example a url that looks like this, `https://weather.com/en-KE/weather/tenday/l/Nairobi+Nairobi?placeId=e1d0bb735632de2df082e02f88493ef295908714761728c5c7d5d6c76cb2f83e`.

Theoretically, this would work. This is what the web browser is doing behind the scenes to get the data. There are some problems, though.

* First, when we look at output.html, we see a bunch of junk! It's all html that is designed for a browser to draw on the screen. There is so much extra information involved, it will take us a while to write a program to filter down to what we want.
* Second, once we've written all of that filtering code, the website might make some changes and cause the filtering to not work anymore - fairly often, the website will add a new feature or update the site, and then our code will get errors until we update it to make the filtering work again.
* And third, many websites don't really want programs to automatically look at their data, and so they try to block Python from getting the website. (Programs looking at their data might send many requests, which would slow down the website.) Even many Google pages block access.

The process of using the html that was designed for a browser is called scraping, and we try to avoid having to do it whenever possible.

Fortunately, some websites are set up to intentionally let programs connect to them, which eliminates these problems. This is called an **API**. A company will create a **web API** by setting up a server that listens for special URLs. If a program sends a request to one of these URLs, they get pure data back in response.

Why APIs are better than scraping:
* APIs do not send html back, or anything intended to be shown by the browser, they send only the pure data that you need. For example, instead of sending text and graphics back, they could send just a list of numbers.
* APIs keep their output structure the same. The company providing an API will be careful not to make changes that would cause your program to stop working. For example, if the API documentation says that the API will respond with a dictionary, it won't change a few weeks later to respond with a list instead.
* An API can monitor how often it is being called, and block anything that is requesting it too often. (An API can restrict access to by requiring anyone connecting to it to provide a type of password called a token).

You can type an API url into the address bar for your browser and see the results there. But you'll just see raw data, so it isn't very useful. The intention an API is for programs, not people, to see it.

Fortunately for my tomato plant project, there is a free API that any program can send requests to, that will respond with the weather forecast. I can write a program to automatically look at the weather forecast! And the data will be in json format, which we already know how to work with.

Watch the video in the next section, to see how I update the weather program we've been working on to get real weather information from the internet.

