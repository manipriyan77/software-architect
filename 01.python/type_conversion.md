# Type Conversion in Python

Type conversion is the process of changing a value from one data type to another. Python supports two kinds: **implicit** (done automatically by the interpreter) and **explicit** (done manually by the programmer, also called type casting).

## Implicit Type Conversion

Python automatically converts one data type to another when there's no risk of losing information. This commonly happens in arithmetic involving mixed types (e.g. `int` and `float`).

```python
num_int = 10
num_float = 2.5

result = num_int + num_float
print(result)       # 12.5
print(type(result))  # <class 'float'>
```

Here Python promotes `num_int` to a float before adding, since converting `int -> float` is safe and lossless. Python will not implicitly convert incompatible types:

```python
"5" + 5  # TypeError: can only concatenate str (not "int") to str
```

## Explicit Type Conversion (Type Casting)

When Python can't or won't convert automatically, you convert manually using built-in functions.

### `int()` — convert to integer

```python
discount = "15"
discount_int = int(discount)
print(discount_int)  # 15
```

- Converts numeric strings (`"15"`) or floats (truncates decimal part, doesn't round).
- Raises `ValueError` on non-numeric strings: `int("abc")` fails.

```python
int(3.99)     # 3  (truncates, not rounds)
int("42")     # 42
int("3.5")    # ValueError - int() can't parse decimal strings directly
```

### `float()` — convert to floating-point

```python
float("3.14")  # 3.14
float(10)      # 10.0
```

### `str()` — convert to string

```python
str(15)      # "15"
str(3.14)    # "3.14"
str(True)    # "True"
```

### `bool()` — convert to boolean

```python
bool(0)      # False
bool(1)      # True
bool("")     # False (empty string is falsy)
bool("no")   # True  (any non-empty string is truthy)
```

### `list()`, `tuple()`, `set()` — convert between collections

```python
list("abc")        # ['a', 'b', 'c']
tuple([1, 2, 3])    # (1, 2, 3)
set([1, 2, 2, 3])   # {1, 2, 3}
```

## Common Pitfalls

- `int("3.5")` fails — go through `float()` first: `int(float("3.5"))` → `3`.
- `int()` truncates toward zero; use `round()` if you need rounding.
- Converting `None` directly raises errors: `int(None)` → `TypeError`.
- Always validate/handle errors when converting user input:

```python
value = input("Enter a number: ")
try:
    number = int(value)
except ValueError:
    print("That wasn't a valid number.")
```

## Quick Reference

| Function  | Purpose                  | Example              |
|-----------|---------------------------|-----------------------|
| `int()`   | Convert to integer        | `int("15")` → `15`   |
| `float()` | Convert to float           | `float("3.14")` → `3.14` |
| `str()`   | Convert to string          | `str(15)` → `"15"`   |
| `bool()`  | Convert to boolean         | `bool(0)` → `False`  |
| `list()`  | Convert to list            | `list("ab")` → `['a','b']` |
| `tuple()` | Convert to tuple           | `tuple([1,2])` → `(1,2)` |
| `set()`   | Convert to set             | `set([1,1,2])` → `{1,2}` |
