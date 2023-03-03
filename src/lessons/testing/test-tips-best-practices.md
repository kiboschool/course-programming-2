
# Test Tips: Best Practices

### Test Coverage

cover the branches


### Detecting Exceptions

use with catch errors


### What makes a good unit test?

(These are ideally what a good unit test looks like. In the real world, we sometimes have to make tests that are more like component tests (they don't perfectly mock out all dependencies) and won't always be like this.)

* Imagine 
* If you discover a bug in your program, and there isn't a test case that would have caught it, add test(s) that would have caught the problem.
   * This will help prevent similar problems from happening in the future.
* If a method has side effects, test those too





