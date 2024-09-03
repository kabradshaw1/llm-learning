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
