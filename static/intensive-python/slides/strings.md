% Strings

## Strings

Three ways to define string literals:

- with single quotes: 'Ni!'

- double quotes: "Ni!"

- Or with triples of either single or double quotes, which creates a multi-line string:

    ```Python
    >>> """I do HTML for them all,
    ... even made a home page for my dog."""
    'I do HTML for them all,\neven made a home page for my dog.'
    ```

## Strings

Note that the REPL echoes the value with a `\n` to represent the newline character. Use the print function to get your intended output:

```python
>>> nerdy = """I do HTML for them all,
... even made a home page for my dog."""
>>> nerdy
'I do HTML for them all,\neven made a home page for my dog.'
>>> print(nerdy)
I do HTML for them all,
even made a home page for my dog.
```

That's pretty [nerdy](http://braverhund.com).

## Strings

Choice of quote character is usually a matter of taste, but the choice can sometimes buy convenience. If your string contains a quote character you can either escape it:

```python
>>> journey = 'Don\'t stop believing.'
```

or use the other quote character:

```python
>>> journey = "Don't stop believing."
```

- How does Python represent the value of the variable `journey` ?

## String Operations

Because strings are sequences we can get a string's length with `len()`:

```python
>>> i = "team"
>>> len(i)
4
```

and access characters in the string by index (offset from beginning – first index is 0) using `[]`:

```python
>>> i[1]
'e'
```

Note that the result of an index access is a string:

```python
>>> type(i[1])
<class 'str'>
>>> i[3] + i[1]
'me'
>>> i[-1] + i[1] # Note that a negative index goes from the end
'me'
```

- What is the index of the first character of a string?
- What is the index of the last character of a string?

## String Slicing

`[:end]` gets the first characters up to but not including `end`

```python
>>> al_gore = "manbearpig"
>>> al_gore[:3]
'man'
```

`[begin:end]` gets the characters from `begin` up to but not including end

```python
>>> al_gore[3:7]
'bear'
```

`[begin:]` gets the characters from `begin` to the end of the string

```python
>>> al_gore[7:]
'pig'
>>>
```

- What is the relationship between the ending index of a slice and the beginning index of a slice beginning right after the first slice?

## String Methods

`str` is a class (you'll learn about classes later) with many methods (a method is a function that is part of an object). Invoke a method on a string using the dot operator.

`str.find(substr)` returns the index of the first occurence of
`substr` in `str`

```python
>>> 'foobar'.find('o')
1
```

- Write a string slice expression that returns the username from an email address, e.g., for 'bob@aol.com' it returns 'bob'.
- Write a string slice expression that returns the host name from an email address, e.g., for 'bob@aol.com' it returns 'aol.com'.

## Conclusion

Your turn:

- Exercise 1
