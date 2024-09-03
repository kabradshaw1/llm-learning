```bash
ipython
run ./file_name
```
## Things I've Learned
help(function) will return the docstring for that function in ipython.  My current version opens in what looks like vim
funtion? will give signature and some other useful information.  That's also possible for methods and veriables

```python
def square(a):
    """Return the sqaure root of a."""
    return a ** 2
```
tab completion in ipython is interesting.  It pulls up lists of imports, if you put import.  you can do wildcards in order to find autocomplete options at the end such as:
```ipython
*Warning?
str.*find*?
```
Ctrl-a: move cursor to beginning of line
Ctrl-e: move cursor to end of the line
Ctrl-b: move cursor back one character
Ctrl-f: move cursor forward one character
Ctrl-d: delete next character in line
Ctrl-k: cut test from cursor to end of line
Ctrl-u: Cut text from beginning of line to cursor
Ctrl-p: Access previous command in history
Ctrl-n: Access next command in history
Ctrl-r Reverse-search through command history
