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
* Variable naming guidelines
* name error
* Variables are labels rather than boxes

#### Strings
* Series of characters inside quotes
* Single or Double quotes
* `str.title()` method
* Dot (.) operator
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

# Chapter 4: Working with Lists

- Looping Through an Entire List
- Avoiding Indentation Errors
- Making Numerical Lists
- Working with Part of a List
- Tuples
- Styling Your Code

#### Looping Through an Entire List
- for loop
  - naming convention for the temporary variable

#### Avoiding Indentation Errors
- Indentation 
- Indentation Errors
- Logical Errors

#### Making Numerical Lists
- `range(start,end,step)` function
  - `range(1,5)` means 1 to 4
  - `range(5)` means 0 to 5
- `list()` function
  - `list(range(5))` : [0,1,2,3,4]
- `min(num_list)` function
- `max(num_list)` function
- `sum(num_list)` function
- List comprehension
  - ex: `squares = [value**2 for value in range(1,11)]`

#### Working with Part of a List
- List slicing (:)
  - `ar[-3:]` returns last 3 elements
- `sample_list[start:end:step]`
- `sample_list = another_list[:]` copy without reference

#### Tuples
- immutable
- ()
- `tup = (1,)` include trailing comma for tuple with 1 element

---

# Chapter 5: If Statements

- A Simple Example
- Conditional Tests
- if Statements
- Using if Statement with Lists
- Styling Your if Statements

#### Conditional Tests
- Equality operator
- Inquality operator
- < > <= >=
- and   or
- in    not in
- Boolean Values & Expressions

#### if Statements
- Simple if statement
- if-else block
- if-elif-else chain
- omitting the else block
- series of if statements

#### Using if statements with Lists
- Checking That a List Is Not Empty 
  
    ```python
        requested_toppings = []
        if requested_toppings:
            for requested_topping in requested_toppings:
                print(f"Adding {requested_topping}.")
            print("\nFinished making your pizza!")
        else:
            print("Are you sure you want a plain pizza?")
    ```

---

# Chapter 6: Dictionaries

- A Simple Dictionary
- Working with Dictionaries
- Looping through a Dictionary
- Nesting

#### Working with Dictionaries
- {key:value,...}
- To access a value in a dictionary
  - `sample_dict[key]`
- Dynamic data structures
- To remove key-value pairs
  - `del sample_dict[key]`
- `sample_dict.get(key)` method
  - returns 'None' or the default value passed as a parameter if the key doesn't exists.

#### Looping through a Dictionary
- `for key,value in dict_1.items():`
  - to loop through each key-value pair for each iteration
- `for key in dict_1.keys():`
  - same as `for key in dict_1:`
  - `if key in dict_1.keys():`
- `for value in dict_1.values():`
- `set(dict_1.values())` to get unique values
  - set : `{value1, value2}`

---