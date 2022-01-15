
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
