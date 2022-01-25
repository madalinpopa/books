
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

## Item 41: Consider Composing Functionality with Mix-in Classes
- Avoid using multiple inheritance with instance attributes and `__init__` if mixin in classes can achieve the same
outcome.
- Use pluggable behaviors at the instance level to provide per-class customization when mix-in classes may require it.
- Mix-ins can include instance methods or class methods, depending on your needs.
- Compose mix-ins to create complex functionality from simple behaviors.

## Item 42: Prefer Public Attributes Over Private Ones
- Private attributes aren't rigorously enforced by the Python compiler.
- Plan from the beginning to allow subclasses to do more with your internal APIs and attributes instead of choosing to
lock them out.
- Use documentation of protected fields to guide subclasses instead of trying to force access control with private
attributes.
- Only consider using private attributes to avoid name conflicts with subclasses that are out of your control.

## Item 43: Inherit from `collections.abc` for Custom Container Types
- Inherit directly from Python's container types (like  `list` or `dict`) simple use cases.
- Beware of the large number of methods required to implement custom container types correctly.
- Have your custom container types inherit from the interfaces defined in `collections.abc` to ensure that your classes
match required interfaces and behaviors

## Item 44: Use Plain Attributes Instead of Setter and Getter Methods
- Define new class interfaces using simple public attributes and avoid defining setter and getter methods
- Use `@property` to define special behavior when attributes are accesed on your objects, if necessary.
- Follow the rule of least surprise and avoid odd side effects in your `@property` methods.
- Ensure that `@property` methods are fast: for slow or complex work - especially involving I/O or causing side effects
use normal methods instead.

## Item 45: Consider `@property` Instead of Refactorig Attributes
- Use `@property` to give existing instance attributes new functionality
- Make incremental progress toward better data models by using `@property`
- Consider refactoring a class and all call sites when you find yourself using `@property` too heavily

## Item 46: Use Descriptors for Reusable `@property` Methods
- Reuse the behavior and validation of `@property` methods by defining your own descriptor classes.
- Use `WeakKeyDictionary` to ensure that your descriptor classes don't cause memory leaks.
- Don't get bogged down trying to understand exactly how `__getattribute__` use the descriptor protocol for fetting
and settings attributes

## Item 47: Use `__getattr__`, `__getattributed__`, and `__setattr__` for Lazy Attributes
- Use `__getattr__` and `__setattr__` to lazily load and save attributes for an object.
- Understand that `__getattr__` only gets called when accessing a missing attribute, whereas `__getattribute__` gets
called every time any attribute is accessed.
- Avoid infinite recursion in `__getattribute__` and `__setattr__` by using methods from `super()` to access instance
attributes

## Item 48: Validate Subclass with `__init_subclass__`
- The `__new__` method of metaclasses is run after the `class` statement's entire body has been processed.
- Metaclasses can be used to inspect or modify a class after it's defined but before it's created, but they're often
more heavyweight than what you need.
- Use `__init_subclass__` to ensure that subclasses are well formated at the time they are defined, before objects
of their type are constructed.
- Be sure to call `super().__init_subclass__` from within your class's `__init_subclass__` definition to enable
validation in multiple layers of classes and multiple inheritance.

## Item 49: Register Class Existence with `__init_subclass_`
- Class registration is a helpful pattern for building modular Python programs.
- Metaclasses let you run registration code automatically each time a base class is subclassed in a program
- Using metaclasses for class registration helps you avoid errors by ensuring that you never miss a registration call
- Prefer `__init_subclass__` over standard metaclass machinery because it's clearer and easier for beginers to
understand.

## Item 50: Annotate Class Attributes with `__set_name__`
- Metaclasses enable you to modify a class's attributes before the class is fully defined.
- Descriptors and metaclasses make powerful combination for declarative behavior and runtime introspection
- Define `__set_name__` on your descriptors classes to allow them to take into account their surrounding class and its
property names.
- Avoid Memory leaks and `weakref` built-int module by having descriptors store data they manipulate directly within a
class's instance directory.

## Item 51: Prefer Class Decorators Over Metaclasses for Composable Class Extension
- A class decorator is a simple function that receives a `class` instance asa a parameter and returns either a new class
or a modified version of the original class.
- Class decorators are useful when you want to modify every method or attribute of a class with minimal boilerplate.
- Metaclasses can't be composed together easily, while many class decorators can be used to extend the same class
without conflicts.

## Item 52: Use `subprocess` to Manage Child Processes
- Use the `subprocess` module to run child processes and manage their input and output streams.
- Child processes run in paralell with the Python Interpreter, enabling you to maximize your usage of CPU cores.
- Use the `run` convenience function for simple usage, and the `Popen` class for advanced usage like UNIX-style
pipelines.
- Use the `timeout` parameter of the `communicate` method to avoid deadlocks and hanging child processes.

## Item 53: Use Threads for Blocking I/O, Avoid Parallelism
- Python threads can't run in parallel on multiple CPU cores because of the global interpreter lock
- Python threads are still useful despite the GIL because they provide an easy way to do multiple things seemingly
at the same time.
- Use Python threads to make multiple calls in parallel. This allows you to do blocking I/O at the same time as
computation.

## Item 54: Use `Lock` to Prevent Data Races in Threads
- Even though Python has a global interpreter lock, you're still responsible for
protecting against data races betweent the threads in your programs.
- Your programs will corrupt their data structures if you allow multiple threads to modify the same objects without
mutual-exclusion locks (mutexes).
- Use the `Lock` class from the `threading` built-in module to enforce your program's invariants between multiple
threads.

## Item 55: Use `Queue` to coordinate Work Between Threads
- Pipelines are a great way to organize sequences of work -- especially I/O-bound programs-that run concurrently
using multiple Python threads.
- Be aware of the many problems in building concurrent pipelines: busy waiting, how to tell workers to stop, and
potential memory explosion.
- The `Queue` class has all the facilities you need to build robust pipelines: blocking operations, buffer sizes, and
joining.

## Item 56: Know how to Recognize When Concurrency Is Necessary
- A program often grows to require multiple concurent lines of execution as its scope and complexity increases.
- The most common types of concurrency coordination are fan-out (generating new units of concurrency) and fan-in
(waiting for existing units of concurency to complete)
- Python has many different ways of achieving fan-out and fan-in

## Item 57: Avoid Creating New `Thread` Instances for On-demand Fan-out
- Threads have many downside: They're costly to start and run if you need a lot of them, they each require a signifiant
amount of memory, and they require special tools like `Lock` instances for coordination.
- Threads do not provide a built-in way to raise exceptions back in the code that started a thread or that is waiting
for one to finish, which makes them difficult to debug.

## Item 58: Understand How Using `Queue` for Concurency Requires Refactoring
- Using `Queue` instances with a fixed number of worker threads improves the scalability of fan-out and fan-in using
threads.
- It takes a significant amount of work to refactor existing code to use `Queue`, especially when multiple stages of
a pipeline are required.
- Using `Queue`, fundamentally limits the total amount of I/O parallelism a program can leverage compared to
alternative approaches provided by other built in Python features and modules.

## Item 59: Consider `ThreadPoolExecutor` When Threads are Necessary for Concurrency
- `ThreadPoolExecutor` enables simple I/O parallelism with limited refactoring, easily avoiding the cost of thread
startup each time fanout concurrency is required.
- Although `ThreadPoolExecutor` eliminates the potential memory blow-up issues of using threads directly, it also limits
I/O parallelism by requiring `max_workers to be specified upfront`

## Item 60: Achieve Highly Concurrent I/O with Coroutines
- Functions that are defined using `async` keyword are called coroutines. A caller can receive the result of a
dependent coroutine by using the `await` keyword
- Coroutines provde an efficient way to runs tens of thousands of functions seemingly at the same time.
- Coroutines can use fan-out and fan-in in order to parallelize I/O, while also overcoming all of the problems
associated with doing I/O in threads

## Item 61: Know How to Port Threaded I/O to `asyncio`
- Python provides asynchronous versions of `for` loops, `with` statements, generators, comprehensions, and helper
  functions that can be used as drop-in replacements in coroutines.
- The `asyncio` built-in module makes it straightforward to port existing code that uses threads and blocking I/O over to coroutines and asynchronous I/O

## Item 62: Mix Threads and Coroutines to Ease the Transition to `asyncio`
- The awaitable `run_in_executor` method of the asyncio event loop enables coroutines to run synchronous functions into `ThreadPoolExecutor` pools.
This facilitates top-down migrations to `asyncio`
- The `run_until_complete` method of the `asyncio` event loop enables synchronous code to run a coroutine until it finishes. The `asyncio.run_coroutine_threadsafe` function provides the same functionality across thread boundaries. Together these help with bottom-up migrations to `asyncio`

## Item 63: Avoid Blocking the `asyncio` Event Loop to Maximize Responsiveness
- Making system call sin coroutines, including blocking I/O and starting threads, can reduce program responsiveness and increase the perception of latency.
- Pass the `debug=True` parameter to `asyncio.run` in order to detect when certain coroutines are preventing the event loop from reacting quickly.

## Item 64: Consider `concurent.futures` for True Paralleism
- Moving CPU bottlenecks to C-extension modules can be an effective way to improve performance while maximizing your investment in Python code. However, doing so has a high cost and may introduce bugs.
- The `multiprocessing` module provides powerful tools that can parallelize certin types of Python computation with minimal effort.
- The power of `multiprocessing` is best accessed thorugh the `concurrent.futures` built-in module and its simple `ProcessPoolExecutor` class.
- Avoid the advanced parts of the `multiprocessing` module until you've exhausted all other options.

## Item 65: Take Advantage of Each Block in `try/except/else/finally`
- The `try/finally` compound statement lets you run cleanup code regardless of wheather exceptions were raised in the `try` block.
- The `else` block helps you minimize the amount of code in `try` blocks and visually distinguish the success case from the `try`/`except` blocks.
- An `else` block can be used to perform additional actions after a successful `try` block but before common cleanup in a `finally` block

## Item 66: Consider `contextlib` and `with` Statements for Reusable `try/finally` Behavior
- The `with` statement allows you to reuse logic from `try/finally` blocks and reduce visual noise.
- The `contextlib` built-in module provides a `contextmanager` decorator that makes it easy to use your own functions in `with` statements.
- The value yielded by context managers is supplied to the `as` part of the `with` statement. It's useful for letting your code directly access the cause of a special context.

## Item 67: Use `datetime` Instead of `time` for Local Clocks
- Avoid using the `time` module for translating between different time zones.
- Use the `datetime` built-in module along with the `pytz` community module to reliably convert between times in different time zone.
- Always represent time in UTC and do conversions to local time as the very final step before presentation.

## Item 68: Make `pickle` Reliable with `copyreg`
- The `pickle` built-in module is useful only for serializing and deserializing objects between trusted programs.
- Deserializing previously pickled objects may break if the classes involved have changed over time
- Use the `copyreg` built-in module with `pickel` to ensure backward compabilitiy for serialized objects.

## Item 69: Use `decimal` When Precision Is Paramount
- Python has built-in types and classes in modules that can represent practically every type of numerical value.
- The `Decimal` class is ideal for situations that require high precision and control over rounding behavior, such as computations of monetary values.
- Pass `str` instances to the `Deciaml` constructor, instead of `float` instance it it's important to compute exact answers and not floatint point aproximations.

## 70: Profile Before Optimizing
- It's important to profile Python programs before optimizing because the sources of slowdowns are ofthen obscure
- Use the `cProfile` module instead of the `profile` module because it provides more accurate profiling information
- The `Profile` objects' `runcall` method provides everything you need to profile a tree of function calls in insolation.
- The `Stats` objects lets you select and print the subset of profiling information you need to see to understand your programs's performance.

## 71: Prefer `deque` for Producer-Consumer Queues
- The `list` type can be used as FIFO queue by having the producer call `append` to add items and the consumer call `pop(0)` to receive items. However, this may cause problems because the performance of `pop(0)` degrades superlinearyly as the queue length increases.
- The `dequea` class from the `collections` built-in module takes constant time--regardles of lenght--for `append` and `popleft`, making it ideal for FIFO queues.

## Item 72: Consider Searching Sorted Sequences with `bisect`
- Searching sorted data containerd in a `list` takes linear time using the `index` method for a `for` loop with simple comparisons.
- The `bisect` built-int module' `bisect_left` function takes logarithmic time to search for values in sorted lists, which can be orders of magnitude faster than other approaches.

## Item 73: Know How to Use `heapq` for Priority Queues
- Priority queues allow you to process itmes in order of importance instead of in first-in, first-out order
- If you try to use `list` operations to implement a priority queue, your program's performance will degrade superlinearly aas the queue grows.
- The `heapq` built-in module provides all the functions you need to implement a priority queue that scales efficiently.
- To use `heapq`, the items being prioritized must have a natural sort order, which requires special methods like `__lt__` to be defined for classes.

## Item 74: Consider `memoryview` and `bytearray` for Zero-Copy Interactions with `bytes`
- The `memoryview` built-int type provides a zero-copy interface for reading and writing slices of objects that support Python's high performance buffer protocol.
- The `bytearray` built-in type provides a mutable `bytes` like type that can be used for zero-copy data reads with functions like `socket.recv_from`
- A `memoryview` can wrap a bytearray, allowing for received data to be spliced into an arbitrary buffer location without copying costs.

## Item 75: Use `repr` Strings for Debugging Output
- Vsllinh `print` on built-in Python types produces the humanreadable string version of a value which hides type information.
- Calling `repr` on built-in Python types produces the printable string version of a value. These `repr` strings can often be passed to the `eval` built-in function to get back the original value.
- '%s' in format strings produces human-readable strings like `str`. `%r` produces printable strings like `repr`
F-strings produce humareadable strings for replacement text expressions unless you specify the !r sufix.
- You can define the `__repr__` special method on a class to customize the printable representation of instances and provide more deatailed debugging information.

## Item 76: Verify Related Behaviors in `TestCase` Subclasses
- You can create tests by subclassing the `TestCase` class from the `unittest` built-in module and defining one method per behavior you’d like to test. Test methods on `TestCase` classes must start with the word tests
- Use the various helper methods defined by the `TestCase` class, such as assertEqual, to confirm expected behaviors in your tests instead of using the built-in assert statements
- Consider writing data-driven tests using the subTest helper method in order to reduce boilerplate

## Item 77: Isolate Tests from Each Other with `setUp`, `tearDown`,`setUpModule` and `tearDownModule`
- It’s important to write both unit tests (for isolated functionality) and integration tests (for modules that interact with each other).
- Use the setUp and tearDown methods to make sure your tests are isolated from each other and have a clean test environment.
- For integration tests, use the setUpModule and tearDownModule module-level functions to manage any test harnesses you need for the entire lifetime of a test module and all of the TestCase classes that it contains.

# Item 78: Use Mocks to Test Code with Complex Dependencies
- The unittest.mock module provides a way to simulate the behavior of interfaces using the Mock class. Mocks are useful in tests when it’s difficult to set up the dependencies that are required by the code that’s being tested.
- When using mocks, it’s important to verify both the behavior of the code being tested and how dependent functions were called by that code, using the Mock.assert_called_once_with family of methods.
- Keyword-only arguments and the unittest.mock.patch family of functions can be used to inject mocks into the code being tested.

## Item 79: Envapsulate Dependencies to Facilitate Mocking and Testing
- When unit tests require a lot of repeated boilerplate to set up mocks, one solution may be to encapsulate the functionality of dependencies into classes that are more easily mocked.
- The Mock class of the unittest.mock built-in module simulates classes by returning a new mock, which can act as a mock method, for each attribute that is accessed.
- For end-to-end tests, it’s valuable to refactor your code to have more helper functions that can act as explicit seams to use for injecting mock dependencies in tests.

## Item 80: Consider Interactive Debugging with pdb
- You can initiate the Python interactive debugger at a point of interest directly in your program by calling the breakpoint built-in function.
- The Python debugger prompt is a full Python shell that lets you inspect and modify the state of a running program.
- pdb shell commands let you precisely control program execution and allow you to alternate between inspecting program state and progressing program execution.
- The pdb module can be used for debug exceptions after they happen in independent Python programs (using python -m pdb -c continue <program path>) or the interactive Python interpreter (using import pdb; pdb.pm()).

## Item 81: Use tracemalloc to Understand Memory Usage and Leaks
- It can be difficult to understand how Python programs use and leak memory.
- The gc module can help you understand which objects exist, but it has no information about how they were allocated
- The tracemalloc built-in module provides powerful tools for understanding the sources of memory usage.

## Item 82: Know Where to Find Community-Built Modules
- The Python Package Index (PyPI) contains a wealth of common packages that are built and maintained by the Python community.
- pip is the command-line tool you can use to install packages from PyPI.
- The majority of PyPI modules are free and open source software.

## Item 83: Use Virtual Environments for Isolated and Reproducible Dependencies
- Virtual environments allow you to use pip to install many different versions of the same package on the same machine without conflicts.
- Virtual environments are created with python -m venv, enabled with source bin/activate, and disabled with deactivate.
- You can dump all of the requirements of an environment with python3 -m pip freeze. You can reproduce an environment by running python3 -m pip install -r requirements.txt

## Item 84: Write Docstrings for Every Function, Class, and Module
- Write documentation for every module, class, method, and function using docstrings. Keep them up-to-date as your code changes.
- For modules: Introduce the contents of a module and any important classes or functions that all users should know about.
- For classes: Document behavior, important attributes, and subclass behavior in the docstring following the class statement.
- For functions and methods: Document every argument, returned value, raised exception, and other behaviors in the docstring following the def statement
- If you’re using type annotations, omit the information that’s already present in type annotations from docstrings since it would be redundant to have it in both places.

## Item 85: Use Packages to Organize Modules and Provide Stable APIs
- Packages in Python are modules that contain other modules. Packages allow you to organize your code into separate, non-conflicting namespaces with unique absolute module name
- Simple packages are defined by adding an __init__.py file to a directory that contains other source files. These files become the child modules of the directory’s package. Package directories may also contain other packages.
- You can provide an explicit API for a module by listing its publicly visible names in its __all__ special attribute.
- You can hide a package’s internal implementation by only importing public names in the package’s __init__.py file or by naming internal-only members with a leading underscore.
- When collaborating within a single team or on a single codebase, using __all__ for explicit APIs is probably unnecessary.

## Item 86: Consider Module-Scoped Code to Configure Deployment environments
- Programs often need to run in multiple deployment environments that each have unique assumptions and configurations.
- You can tailor a module’s contents to different deployment environments by using normal Python statements in module scope
- Module contents can be the product of any external condition, including host introspection through the sys and os modules.

## Item 87: Define a Root Exception to Insulate Callers from APIs
- Defining root exceptions for modules allows API consumers to insulate themselves from an API.
- Catching root exceptions can help you find bugs in code that consumes an API.
- Catching the Python Exception base class can help you find bugs in API implementations
-  Intermediate root exceptions let you add more specific types of exceptions in the future without breaking your API consumer

## Item 88: Know How to Break Circular Dependencies
- Circular dependencies happen when two modules must call into each other at import time. They can cause your program to crash at startu
- The best way to break a circular dependency is by refactoring mutual dependencies into a separate module at the bottom of the dependency tree.
- Dynamic imports are the simplest solution for breaking a circular dependency between modules while minimizing refactoring and complexity.

## Item 89: Consider warnings to Refactor and Migrate Usage
- The warnings module can be used to notify callers of your API about deprecated usage. Warning messages encourage such callers to fix their code before later changes break their programs.
- Raise warnings as errors by using the -W error command-line argument to the Python interpreter. This is especially useful in automated tests to catch potential regressions of dependencies.
- In production, you can replicate warnings into the logging module to ensure that your existing error reporting systems will capture warnings at runtime.
- It’s useful to write tests for the warnings that your code generates to make sure that they’ll be triggered at the right time in any of your downstream dependencies.

## Item 90: Consider Static Analysis via typing to Obviate Bugs
- Python has special syntax and the typing built-in module for annotating variables, fields, functions, and methods with type information.
- Static type checkers can leverage type information to help you avoid many common bugs that would otherwise happen at runtim
- There are a variety of best practices for adopting types in your programs, using them in APIs, and making sure they don’t get in the way of your productivity.

