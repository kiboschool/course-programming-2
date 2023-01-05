# Tips For Print Debugging



<!--

------------------------------- in progress -------------------------------



    • Outline
        ◦ Theme for this week is “how to explore code”, 1) investigate a bug, 2) investigate another body of code to learn how it works 3) readability considerations
        ◦ Show print debugging
            ▪ Tips like pretty-print, dump all local vars, dump object’s __dict__, repr to see whitespace chars
        ◦ Show stop-the-world debugging
            ▪ PythonTutor helps show this
            ▪ Useful for duck typing scenarios when you don’t know the object
        ◦ Discuss ways to organize code that make it harder vs easier to read
        ◦ Discuss ways to explore large codebases, even those in a different language
            ▪ Search for strings and work backwards
            ▪ print-trace-debugging to see what is getting executed. Or log to a file for ui programs.
            ▪ Find-in-files is useful, limit file types e.g. to not include docs/css
            ▪ Drill down using VsCode F12. And go higher by using callers with ‘find references’.
            ▪ Large projects are often lots of puzzle pieces fitting together.
            ▪ Thoroughly learn something by porting it to a new platform
            ▪ Sometimes looking for main() at the top works, sometimes it doesn’t
            ▪ Some languages have braces. Some languages need a compilation step.
            ▪ Changing strings is a way to ensure your changes are working
            ▪ Write a little script to call into one low-level part of the program to see if it can be run independently

    • Code Examples (some provided by us, some left to be written by students)
        ◦ Lab: fix a bug in a provided nontrivial codebase
        ◦ Possibly: take the midterm project from another student, and add a feature to it, while keeping it running and preserving the style
        ◦ Split into separate functions and files
        ◦ Write documentation - docstrings, comments, improve variable names
-->
