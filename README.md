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

```ipython
%timeit L = [n ** 2 for n in range(1000)]
```

```ipython
%%timeit
L = []
for n in range(1000):
  L.append(n ** 2)
```

We are going over a varity of uses for ipython's In and Out objects.  We are learning that _ can retreive the last output and __ will go back 2.

```bash
%history -n 1-3
```
This will print your inputs for In[n] where n is the range, in this example 1-3

The ipython shell can add ! to a command such as !pwd to do the zsh commands.

ls works without !ls, but it does require ! in order to do contents = !ls or directory = !pwd.  These are 
of type IPython.utils.text.SList.  You can see this by print(directory).  This is a lot like a python list, but it has some additonal functionality, such as grep and fields method and the s, nm p properties that allow you to search, filter, and display the results in convenent ways.  You can read about this in IPython's build-in help features.

You can also pass variables from the IPython to the zsh by using {}.  

```IPython
message = "hello from python"
!echo {message}
```
You can change the amount of information displayed in errors with these commands:
```IPython
%xmode Verbose
%xmode Plain
```

The debugger for ipython lets you step through the function 