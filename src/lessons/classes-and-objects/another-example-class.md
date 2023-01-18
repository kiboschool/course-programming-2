# Another Example Class

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/kPkqyoTSdks?rel=0" title="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

If you'd like to follow along, you can see the starting code <a href="https://github.com/kibo-programming-2-jan-23/walkthroughs/tree/main/classes-weather-data/beginning" target="_blank">here</a> and the end result <a href="https://github.com/kibo-programming-2-jan-23/walkthroughs/tree/main/classes-weather-data/end" target="_blank">here</a>.

Some of what we learned in the video:

* If we use a class, we will know what attributes are there on the instance.
  * For example, we know that an instance of the `Point` class will always have an `x` attribute and a `y` attribute, but no other attributes.
  * If we saw `point_instance.w` it would look wrong.
  * This means that we can catch bugs earlier, before even running the program.
  * A dictionary, on the other hand, doesn't describe what is there. There could potentially be a valid `data['w']`.
  * We would need to read the code or look at documentation that someone wrote, which takes time.
* If we use a class, our VSCode editor can also know what attributes are there.
  * I recommend installing the VSCode extension called "Pylance".
  * Typing `point_instance.` will pop up a window showing `x` and `y`.
  * We can make changes to the program faster, even if we don't remember what methods or attributes are there, because we can use this autocomplete window that pops up.  
* The video also shows some possibilities:
  * We can create a helper function that creates an instance of a class.
  * Methods in a class can call other methods.
  * If a long method is split into smaller methods, the code is often easier to read.

