# Username Changes

A company has released a new internal system, and each employee has been assigned a username. Employees are allowed to change their usernames but only in a limited way. More specifically, they can choose letters at two different positions and swap them. For example, the username “bigfish” can be changed to “gibfish” (swapping ‘b’ and ‘g’) or “bighisf” (swapping ‘f’ and ‘h’). The manager would like to know which employees can update their usernames so that the new username is smaller in alphabetical order than the original username.

CodeWars - Kata not found

## Example

import `is_changable()` function and pass `str` value to it
the output will be _YES_ or _NO_ according to username

``` python
from UsernameChanges import is_changable

is_changable("bigfish") # YES
is_changable("ace") # NO
```
