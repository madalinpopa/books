
# Effective Python: 90 Specific Ways to Write Better Python, 2nd Edition

- always use f string instead of format and C style format.
- don't use or expression to set default values in variables.
- always write helper function and avoid long expressions.
- use unpacking for tuples instead getting itmes through index.
- you can use unpacking to swap values in place without the need to create a temporary variable.
- unpacking is generalized in python and can be applied to any iterable, including many levels of iterables within
interables.
- reduce visual noise and increase code clarity by using unpacking to avoid explicitly indexin into sequences.

## Item 7: Prefer `enumerate` over `range`
- `enumerate` provides concise syntax for looping over an iterator and getting the index of each item from the iterator
as you go.
- prefer `enumerate` instead of looping over a range and indexing into a sequence.
- you can suply a second parameter to enumerate to specify the number from which to begin counting.

## Item 8: Use `zip` to process iterators in parallel
- the `zip` built-in function can be used to iterate over multiple iterators in parallel.
- `zip` creates a lazy generator that produces tuples, so it can be used on indefinitely long inputs.
- `zip` truncates its outputs sliently to the shortest iterator if you supply it with iterators of different lengths
- use the `zip_longest` function from the `itertools` built-in module if you want to use zip on iterators of unequal
lengths without truncation.

## Item 9: Avoid `else` blocks after `for` and `while` loops
- python has special syntax that allows `else` blocks to immediately follow `for` and `while` loop interior blocks.
- the `else` block after a loop runs only if the loop body did not encounter a `break` statement.
- avoid using `else` blocks after loops because their behavior isn't intuitive and can be confusing.

## Item 10: Prevent repetition with assignment expressions
- assignment expressions use the valrus operator `:=` to both assign and evaluate variable names in a single expression.
- when an assignment expression is a subexpression of a larger expression, it must be surrounded with parantheses.
- although switch/case statements and do/while loops are not available in Python, their functionality can be emulated
much more clearly by using assignment expression.

## Item 11: Know how to slice sequences
- avoid being verbose when slicing: Don't supply `0` for the start index of the length of the sequence for the end
index.
- slicing is forgiving of start or end index that are out of bounds, which means it's easy to express slices on the
front or back boundaries of a sequence (like `a[:20] or a[-20:]`)
- assigning to a `list` slice replaces that range in the original sequence with what's referenced even if the lengths
are different.

## Item 12: Avoid Striding and Slicing in a Single Expression
- specifying start, end and stride in a slice can be extremely confusing.
- prefer using positive stride values in slices without start or end indexex. Avoid negative stride values if possible.
- Avoid using start, end, and stride together in a single slice. If you need all three parameters, consider doing two
	assignments( one to stride and another to slice ) or using islice from itertools built-in module.

## Item 13: Prefer Catch-All Unpacking Over Slicing
- unpacking assignments may use a starred expression to catch all values that weren't assigned to other parts of the
unpacking pattern into a `list`
- starred expressions mayh appear in any position, and they will always become a `list`, containing the zero or more
values they recive.
- when dividing a `list` into non-overlapping pices, catch-all unpacking is much less error prone than slicing and
indexing.

## Item 14: Sort by Complex Criteria Using the `key` Parameter
- the `sort` method of the `list` type can be used to rearrange a list's contents by the natural ordering of built-in
types like strings, integers, tuples and so on.
- the `sort` method doesn't work for objects unless they define a natural ordering using special methods, which is
uncommon.
- the `key` parameter of the `sort` method can be used to supply a helper function that returns the value to use for
sorting in place of each item from the `list`
- returning a `tuple` from a `key` function allows you to combine multiple sorting criteria together.
the unary minus operator can be used to reverse individual sort orders for types that allow it.
- for types that can't be negated, you can combine many sorting criteria together
by calling the sort method multiple times using different `key` and `reverse`
values, in the order of lowest rank `sort` call to highest rank `sort` call

## Item 15: Be Cautious When Relying on `dict` Insertion Ordering
- since python 3.7, you can rely on the fact that iterating a dict instance's contents will ocurr in the same
order in which the keys were initially added.
- python makes it easy to define objects that act like dictionaries but that aren't dict instances. For these types you
can't assume that insertion ordering will be preserved.
- there are three ways to be careful about dictionary-like classes: write code that dosen't rely on insertion ordering
, explicitly check for the `dict` at runtime, or requiere `dict` values using type annotaions and static analysis.

## Item 16: Prefer `get` Over `in` and `KeyError` to Handle Missing Dictionary Keys
- there are four common ways to detect and handle missing keys in dictionaries:
using `in` expressions, `KeyError` exceptions, the `get` method and the `setdefault` method.
- the `get` method is best for dictionaries that contain basic types like counters, and it is preferable along with
assignment expressions when creating dictionary values has a high cost or may raise exceptions.
- when the `setdefault` method of `dict` seems like the best fit for your problem, you should consider using defaultdict
instead.

## Item 17: Prefer `defaultdict` Over `setdefault` to Handle Missing Items in Internal State
- If you're creating a dictionary to manage an arbitrary set of potential keys, then you should prefer using a
`defaultdict` instance from the `collections` built-in module if it suits your problem.
- If a dictionary of arbitrary keys is passed to you, and you don't control its creation, then you should prefer the
`get` method to access its items. However, it's worth considering using the `setdefault` method for the few situations
in which it leads to shorter code.

## Item 18: Know How to Construct Key-Dependent Default Values with `__missing__`
- the `setdefault` method of `dict` is a bad fit when creating the default value has high computational cost or
may raise exceptions.
- the function passed to `defaultdict` must not require any arguments, which makes it impossible to have the default
value depend on the key being accessed.
- you can define your own `dict` subclass with a `__missing__` method in order to construct default values
that must know which key was being accessed.

## Item 19: Never Unpack More Than Three Variables When Functions Return Multiple Values
- you can have functions return multiple values by putting them in a tuple and having the caller take advantage of
Python's unpacking syntax.
- multiple return values froma function can also be unpacked by catch-all starred expressions.
- unpacking into four or more variables is error prone and should be avoided; instead, return a small class or
`namedtuple` instance

## Item 20: Prefer Raising Exceptions to Returning `None`
- functions that return `None` to indeicate special meaning are error prone because `None` and other values
(e.g, zero, the empty string) all evaluate to `False`
- raise exceptions to indicate special situation instead of returning `None`
Expect the caling code to handle exceptions properly when they're documented.
- type annotations can be used to make it clear that a function will never return the value `None`, even in special
situations.

## Item 21: Know How Closures Interact with Variable Scope
- closure functions can refer to variables from any of the scopes in which they were defined.
- by default, closure can't affect enclosing scopes by assigning variables.
- use the `nonlocal` statement to indicate when a closure can modify a variable in its enclosing scopes
- avoid using nonlocal statements for anything beyond simple functions.

## Item 22: Reduce Visual Noise with Variable Positional Arguments
- functions can accept a variable number of positional arguments by using `args` in the `def` statement.
- you can use the items from a sequence as the positional arguments for a function with `*` operator.
- using the `*` operator with a generator may cause a program to run out of memory and crash.
- adding new positional parameters to functions that accept `*args` can introduce hard-to-detect bugs

## Item 23: Provide Optional Behavior with Keyword Arguments
- function arguments can be specified by position or by keyword
- kwywords make it clear what the purpose of each argument is when it would be confusing with only positional
arguments.
- keyword arguments with default values make it easy to add new behaviors to a function
without needing to migrate all existing callers.
- optional keyword arguments should always be passed by keyword instead of by position.

## Item 24: Use `None` and Docstrings to Specify Dynamic Default Arguments
- a default argument value is evaluated only once: during function definition at module load time. This can
cause odd behaviors for dynamic values (like `{}`, `[]` or `datetime.now()`)
- use `None` as the default value for any keyword argument that has a dynamic value. Document the actual
behavior in the function's docstring.
- Using `None` to represent keyword argument default values also works correctly with type annotations.

## Item 25: Enforce Clarity with Keyword-Only and Positional-Only Arguments
- Keyword-only arguments forces callers to supply certain arguments by keyword (instead of by position), which
makes the intention of a function call clearer. Keyword-only arguments are defined after a single `*` in the argument
list.
- Positional-only arguments ensure that callers can't supply certain parameters using keywords, which helps reduce
coupling. Positional-only arguments are defined before a single `/` in the argument list.
- Parameters between the `/` and `*` characters in the argument list may be supplied by position or by keyword,
which is the default for python parameters

## Item 26: Define Function Decorators with `functools.wraps`
- Decorators in Python are syntax to allow one function to modify another function at runtime.
- Using decorators can cause strange behaviors in tools that do introspection, such as debuggers.
- Use the `wraps` decorator from the functools built-in module when define your own decorators to avoid issues.

## Item 27: Use Comprehensions Instead of `map` and `filter`
- List comprehensions are clear than the `map` and `filter` built-in functions because they don't require `lambda`
expressions.
- List comprehensions allow you to easily skip items from the input `list`, a behavior that `map` doesn't support
without help from `filter`
- Dictionaries and sets may also be created using comprehensions.

## Item 28: Avoid More Than Two Control Subexpressions in Comprehensions
- Comprehensions support multiple levels of loops and multiple conditions per loop level.
- Comprehensions with more than two control subexpression are very difficult to reand and should be avoided.

## Item 29: Avoid Repeated Work in Comprehensions by Using Assignment Expressions
- Assignment expressions make it possible for comprehensions and generator expressions to reuse the value
from one condition elsewhere in the same comprehensions, which can improve readibility and performance.
- Although it's possible to use an assignment expression outside of a comprehension or generator expression's condition
, you should avoid doing so.

## Item 30: Consider Generators Instead of Returning Lists
- Using generators can be clearer than the alternative of having a function return a `list` of accumulated results.
- The iterator returned by a generator produces the set of values passed to `yield` expressions within the generator
function's body.
- Generators can produce a sequence of outputs for arbitrarily large inputs because their working memory doesn't
include all inputs and outputs.

## Item 31: Be Defensive When Iterating Over Arguments
- Beware of functions and methods that iterate over input arguments multiple times. If these arguments
are iterators, you may see strange behavior and missing values.
- Python's iterator protocol defines how containers and itrators interact with the `iter` and `next` built-in functions
, `for` loops, and related expressions.
- You can easily define your own iterable container type by implementing the `__iter__` method as generator
- You can detect that a value is an iterator (instead of a container) if caling `iter` on it produces the same value as
you passed in. Alternatively, you can use the `isinstance`, built-in function with the `collections.abc.Iterator`
class.

## Item 32: Consider Generator Expressions for Large List Comprehensions
- List comprehensions can cause problems for large inputs by using too much memory
- Generator expressions avoid memory issues by producing outputs one at a time as iterators
- Generator expressions can be composed by passing the iterator from on generator expression in the for
subexpression of another.
- Generator expressions execute very quicly when chained together and are memory efficient.

## Item 33: Compose Multiple Generators with `yield from`
- The `yield from` expression allows you to compose multiple nested generators together into a single combined
generator.
- `yield from` provided better performance than manually iterating nested generators and yielding their outputs.

## Item 34: Avoid Injecting Data into Generators with `send`
- The `send` method can be used to inject data into a generator by giving the `yield` expression a value that can
be assigned to a variable.
- Using `send` with `yield from` expressions may cause surprising behavior, such as `None`, values appearing at
unexpected times in the generator output.
- Providing an input iterator to a set of composed generators is better approach tha using the `send` method,
which should be avoided.

## Item 35: Avoid Causing State Transitions in Generators with `throw`
- The `throw` method can be used to re-raise exceptions within generators at the position of the most recently executed
`yield` expression.
- Using `throw` harms readability because it requires additional nesting and boilerplace in order to raise and catch
exceptions.
- A better way to provide exceptional behavior in generators is to use a class that implements the `__iter__` method
along with methods to cause exceptional state transitions.

## Item 36: Consider `itertools` for Working with Iterators and Generators
- The `itertools` functions fall into three main categories for working with iterators and generators: linking iterators
together, filtering items they output, and producing combinations of items.
- There are more advance functions, additional parameters, and useful recipes available in the documentation at
`help(itertools)`

## Item 37: Compose Classes Instead of Nesting Many Levels of Built-in Types
- Avoid making dictionaries with values that are dictionaries, long tuples or complex nestings of other built-in types
- Use `namedtuple` for lightweight, immutable data containers before you need the flexibility of a full class.
- Move your bookkeeping code to using multiple classes when your internal state dictionaries get complicated.

## Item 38: Accept Functions Instead of Classed for Simple Interfaces
- Instead of defining and instantiating classes, you can often simply use functions for simple interfaces between
components in Python.
- References to functions and methods in Python are first class, meaning they can be used in expressions
(like any other type)
- The `__call__` special method enables instances of a class to be called like plain Python Functions
- When you need a function to maintain state, consider defining a class that provides the `__call__` method instead of
defining a stateful closure.

## Item 39: Use `@classmethod` Polymorphism to Construct Objects Generically
- Python only supports a single constructor per class: the `__init__` method.
- Use `@classmethod` to define alternative constructors for your classes.
- Use class method polymorphism to provide generic ways to build and connect many concrete sublasses.

## Item 40: Initialize Parent Classes with `super`
- Python's standard method resolution order (MRO) solves the problem of superclass initialization order and
diamond inheritance.
- Use the `super` built-in function with zero arguments to initialize parent classes.
