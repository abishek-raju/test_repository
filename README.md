<!--Heading-->
#E.P.A.I Session 2

<!--Motivation-->
##E.P.A.I Session 2 Assignment

<!--Titles-->
- [Functions](#functions)
	- [Something](#something)
	- [SomethingNew](#somethingnew)
	- [add_something](#add_something)
	- [clear_memory](#clear_memory)
	- [critical_function](#critical_function)
	- [compare_strings_old](#compare_strings_old)
	- [compare_strings_new](#compare_strings_new)
	- [sleep](#sleep)
	- [char_list](#char_list)
	- [collection](#collection)
	- [\_\_init__](#init)
- [What is Happening?](#what-is-happening)
- [References](#references)

###Something
```python
class Something(object):
    def __init__(self):
        super().__init__()
        self.something_new = None
```
###SomethingNew
```python
class SomethingNew(object):
    def __init__(self, i: int = 0, something: Something = None):
        super().__init__()
        self.i = i
        self.something = something
```
###add_something
```python
def add_something(collection: List[Something], i: int):
    something = Something()
    something.something_new = SomethingNew(i, something)
    collection.append(something)
```
Cyclic Referencing.
###clear_memory
```python
def clear_memory(collection: List[Something]):
    # you probably need to add some comment here
    collection.clear()
    gc.collect()
```
Used to clear the memory  of any cyclic references.
###critical_function
```python
def critical_function():
    collection = list()
    for i in range(1, 1024 * 128):
        add_something(collection, i)
    clear_memory(collection)
```
This function will create cyclic references **1024*128** times.
###compare_strings_old
```python
def compare_strings_old(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass
    char_list = list(a)
    for i in range(n):
        if 'd' in char_list:
            pass

```
Compares each character of one string with another, also "list" of a string to check if a character is present in the entire string which is slower.
###compare_strings_new
```python
def compare_strings_new(n):
    a = sys.intern('a long string that is not intered' * 200)
    b = sys.intern('a long string that is not intered' * 200)
    for i in range(n):
        if a is b:
            pass
    char_list = frozenset(a)
    for i in range(n):
        if 'd' in char_list:
            pass
```
Here checking if the memory id of both strings are same or not, also using **frozenset** of a string which is Faster and Efficient.
###sleep
```python
time.sleep(6)
```
Introducing delay of 6 sec's.
###char_list
```python
char_list = list(a)
```
Converting the **string** object  to a **list** object of character's.
###collection
```python

```
###init
```python
def __init__(self):
	super().__init__()
	self.something_new = None
```
Constructor which allow's the class to initialize the attributes of the class.



###What is happening?

The first function that is executed is **critical_function** which executes **add_something** 1024 * 128 times and then call's **clear_memory** which is responsible for removing all the cyclic reference's created by the add_something function.Inside clear_memory **gc.collect()** removes all the cyclic reference's which is why we see a dramatic reduction in the memory use.



The second function that is executed is **compare_strings_old**  and **compare_strings_new**.While both have identical use we are interested in the performance metric.In the "compare_strings_old" function the two strings **a** and **b**  although identical have not been interned,because of which when the equality test is conducted it internally checks it at a character level.Also for the membership test the string is converted to a list of characters which again is slower compared to its immutable cousin's.In the "compare_strings_new" function the strings have been interned and the equality test has been replaced with the **is** operator which checks if both the variables point to the same memory location.Also for the membership test the string is converted to a **frozenset** which is much more efficient.



###References
- https://www.journaldev.com/22460/python-str-repr-functions
- https://stackoverflow.com/questions/37075939/python-experiment-with-gc-and-memory-profiler
- https://www.w3schools.com/python/ref_func_frozenset.asp


[Back to top](#)