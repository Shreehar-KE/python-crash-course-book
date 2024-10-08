# Chapter 1: Getting Started

* Setting Up Your Programming Environment
* Python on Different Operating Systems
* Troubleshooting
* Running Python Programs from a Terminal

#### Setting Up Your Programming Environment
* Python Interpreter
* Python prompt `>>>`

#### Python on Different Operating Systems
* `exit()`

#### Troubleshooting
* Traceback

#### Running Python Programs from a Terminal
* Terminal Commands
  * `cd`
  * `ls`
* `python3 file_name.py`

---

# Chapter 2: Variables and Simple Data Types

* What Really Happens When You Run hello_world.py
* Variables
* Strings
* Numbers
* Comments
* The Zen of Python

#### What Really Happens When You Run hello_world.py
* `.py` extension
* `print()` function
* Syntax Highlighting

#### Variables
* Variable & Value
* Varible naming guidelines
* name error
* Variables are labels rather than boxes

#### Strings
* Series of characters inside quotes
* Single or Double quotes
* `str.title()` method
* Dot (.) notation
* `str.upper()` method
* `str.lower()` method
* f-strings (f : format)
  * `f"Using a variable {var} inside a String"`
* Whitespace characters: space, `\n`, `\t`
* `str.strip()`, `str.lstrip()`, `str.rstrip()` methods
* `url.removeprefix('https://')` method
* Syntax Errors
* `filename.removesuffix('.txt')` method

#### Numbers
* Integers
* Arithmetic Operators: `+ - * / **` 
* Order of operations i.e. Operator Precedence, ()
* Float
  * `0.2 + 0.1 = 0.30000000000000004` - due to **precision**
  * `4 / 2 = 2.0` - Decimal division by default, 
* Underscores to group digits
  * `universe_age = 14_000_000_000`
  * `print(universe_age) # 14000000000`
* Multiple Assignment
* Constants (not included python)

#### Comments
* `#` hash mark
* Writing Meaningful comments

---

# Chapter 3: Introducing Lists

* What is a List?
* Modifying, Adding, and Removing Elements
* Organizing a List
* Avoiding Index Errors When Working with Lists

#### What is a List?
* Collection of items, [], separated by commas, can be unrelated
* Index, starts from 0
* Off-by-one Error
* `sample_list[-1]` to access the last element & other negative index values

#### Modifying, Adding, and Removing Elements
* Lists are dynamic(size)
* `sample_list.append(value)` method
* `sample_list.insert(pos, val)` method
* `del sample_list[pos]` method
  * permanently deletes the item at pos
* `removed_item = sample_list.pop()` method
  * return the last item and removes it from the list
* `some_item = sample_list.pop(pos)` method
  * return the item at pos and removes it from the list
* `sample_list.remove(value)` 
  * removes the item by its value
  * first appearance only

#### Organizing a list
* `list.sort()` method
  * changes the order permanently
* `list.sort(reverse=True)` method
* `sorted(list)` function
  * doesn't modify the list
  * also accepts `reverse=True` argument
* `list.reverse()` method
  * reverses the original order, permanently modifies the list
* `len(list)` function
  * returns the length of the list, i.e no. of items

#### Avoiding Index Errors When Working with Lists
* Index Error

---