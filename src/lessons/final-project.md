# Final Project

FINAL PROJECT: OBJECT-ORIENTED TIC TAC TOE 

This builds off one of the final-projects from programming-1

* Students start with a full solution to that project
* We provide a stub TicTacToeDrawer, student implements it to draw to console, and refactor code to call into that
* We provide a stub TicTacToeGame, student implements it to run the game
* First improve it to be able to save the game state to json on disk and restore at any point
    * Implement the save() and restore() methods, they should work independently (meaning that if we need to change how they persist in the future it shouldn’t necessitate other big changes)
* Extensibility
    * By writing something in an object-oriented way, it’s easy for people to make future changes, all they need to do is implement the interface
    * We’ll show extensibility by doing this - your program must ask you which mode you want to run in - console or image, and it will create a different TicTacToe drawer instance and use that throughout
    * This is a good way to show the benefit of OOP, and how the calling code is simpler
    * If there is enough time to cover PIL
        * Students will make a TicTacToeDrawer implementation that uses PIL. (create a png file, run process to show and wait for user to click X, then resumes)
    * If there is not enough time to cover PIL
        * Students will make a TicTacToeDrawer implementation that uses unicode characters for more-fun graphics, like “✕” and “◯”, or have fun looking for other unicode markers.
* Fun Challenge
    * Make another separate TicTacToeDraw implementation that does something creative.


