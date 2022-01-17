
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
