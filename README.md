**Process Killer Program**

This program displays in a scrollable window the result of "ps -ef".

        The Display looks as Follows;

```                   Search Box
            .-----------------------.
            |   < search value >    |
            '-----------------------'  
    .---------.  .--------------.  .--------.
    |  Find   |  | Kill Process |  |  Quit  |
    '---------'  '--------------'  '--------'

.-----------------------------------------------------.
|                      Display Window                 |
:                                                     :

:                                                     :
|                                                     |
'-----------------------------------------------------'
```

The user enters a search value in the Search Box and 
entering a Carriage Return OR Clicking Find Button 
starts the search function.

If the Search Value is found the line is highlighted.

Clicking the Find Button will continue the search on the
line after the selected line. And this will continue until
the last line matching the Search Value is Found. The search
if continued, starts at line 1.

Clicking the Kill Process Button will is a "kill -9 <pid>".
Where <pid> is the pid on the selected line, and reload
a fresh "ps -ef" list.

Obviously, clicking on the Quit Button causes the program 
to exit.

**Files:**
  * .gitignore
  * pkill.py
  * README.txt
