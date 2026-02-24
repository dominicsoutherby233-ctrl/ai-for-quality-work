my definition of good code is well abstracted, clear variable and function names. No function should be longer than 20 lines and should make use of abstractions. 

Type hints should be used wherever possible and docstrings should be fully descriptive.

Avoid nesting of codes - NEVER have more than 2 nested loops or conditionals.

Bias against using try except loops, only use them for errors that are anomolous and not easily handled with if statements.

use lists comprehension where possible as long as the list comprehension isn't longer then 40 characters