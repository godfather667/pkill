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

When the user enters a search value in the Search Box and
then entering a Carriage Return OR Clicking Find Button 
will start the search function.

If the Search Value is found the line is highlighted.

Clicking on the Find Button will continue the search on the
line after the selected line. This will continue until
the last line matching the Search Value is found. If the search
if continued, by clicking Find Button, the search restarts at line 1.

Clicking on the Kill Process Button will issue a "kill -9 &ltpid&gt" 
OS Command where &ltpid&gt is the actual pid on the selected line 
and reload a fresh "ps -ef" list.

Obviously, clicking on the Quit Button causes the program to exit.

**Files:**
  * .gitignore
  * pkill.py
  * README.txt
