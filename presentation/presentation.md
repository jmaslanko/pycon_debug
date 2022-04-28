---
marp: true
theme: gaia
paginate: false
backgroundColor: '#eae8db'
color: '#392020'
---
<!-- _class: lead -->

# LEARNING FROM ERRORS: UNDERSTANDING AND DEBUGGING PYTHON ERRORS


### Dorota Jarecka
McGovern Institute for Brain Research, MIT (Cambridge, MA)

---
# Main theme of the presentation


-  errors / bugs
-  debugging

## Why?

- because most tutorials shows you how to write code that works
- in real life you spend more time dealing with bugs than  writting a new code...


---

# What is debugging?

- investigating why the program is not working properly
- fixing the issues

---

### When does the program not work properly?

- returns an error
- returns results that differ from what you expected
- keep running and doesn't return anything

---
# Errors in Python

- Syntax Errors

- Exception Errors

    - FileNotFoundError
    - AssertionError
    - ZeroDivisionError

---
# Syntax Errors
```
  File ~/teaching/pycon_debugging/part1/syntax.py:1
    a = 3 * (4 + 6
                  ^
SyntaxError: incomplete input
```

```
  File "/Users/dorota/teaching/pycon_debugging/part1/syntax_2.py", line 1
    for i in range(2)
                     ^
SyntaxError: expected ':'
```

---
# Exception Errors

```
Traceback (most recent call last):
  File "/Users/dorota/teaching/pycon_debugging/part1/division.py", line 1, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

```
Traceback (most recent call last):
  File "/Users/dorota/teaching/pycon_debugging/part1/assert.py", line 1, in <module>
    assert 1 + 2 < 3
AssertionError
```

---
# Python Traceback 
TODO

```
Traceback (most recent call last):
  File "/Users/dorota/teaching/pycon_debugging/part1/division_traceback.py", line 18, in <module>
    main()
  File "/Users/dorota/teaching/pycon_debugging/part1/division_traceback.py", line 15, in main
    return mean(my_list)
  File "/Users/dorota/teaching/pycon_debugging/part1/division_traceback.py", line 8, in mean
    list_mean = list_sum / list_len
ZeroDivisionError: division by zero
```
- show a Python call stack at the point the exception was raised 

---
TODO
# Python call stack

![width:800px](stack.001.jpeg)
 
 ---
# pdb - the Python debugger

-  interactive source code debugger

- part of the Python's standard library

- allows to stop and exammin running code

- two main ways of using `pdb`:

    - start the program with the debugger: 
    `python -m pdb code.py`

    - stop the program and invoke the debugger:
    `import pdb; pdb.set_trace` or `breakpoint()` (in Python 3.7+)
---
# using the interactive debugger

after inoking the debugger using `breakpoint()` in the code:
- `p <expression>` - evaluate the expression in the current context and print its value
- `pp` - the same as `p` but uses pretty-print 
- `l` - ist source code for the current file (without arguments, list 11 lines around the current line)
- `ll` - ist all source code for the current function or frame
- `a` - print the argument list of the current function.