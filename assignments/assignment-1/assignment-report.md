# COMP 218: Introduction to Computer Programming with Python
## Assignment 1

| | |
|---|---|
| **name** | Simon Dawkins |
| **student ID** | 3793522 |
| **estimated time taken** | 4h |

***

## Short-Answer Questions

### Question 1
The following **cannot** be used as identifiers:

- **(2) `5ty`** — cannot begin with a digit
- **(4) `if`** — python reserved keyword
- **(6) `h$`** — `$` not a valid character

The remaining options (`D3a`, `x6`, `program`, `title`, `john`, `__init__`, `p_q`) are all valid identifiers, though naturally `__init__` may cause unintended results.

***

### Question 2

Given: `m = 3`, `n = 5`, `x = 13`, `y = 15`

| # | Expression | Work | Result | Notes
|---|---|---|---|---|
| 1 | `y / n * m` | `15 / 5 * 3 = 3.0 * 3` | `9.0` |
| 2 | `n ** m` | `5 ** 3` | `125` |
| 3 | `x % m` | `13 % 3 = 12 R: 1` | `1` |
| 4 | `n // m` | `5 // 3` | `1` |
| 5 | `(x * y) % m` | `(13 * 15) % 3 = 195 % 3` | `0` |
| 6 | `m \| n` | `011 \| 101 = 111` | `7` | bitwise OR
| 7 | `(m*n) & (y-x)` | `15 & 2 = 01111 & 00010` | `0` | bitwise AND
| 8 | `m ^ x + (y // n)` | `3 ^ (13 + 3) = 3 ^ 16 = 00011 ^ 10000` | `19` | bitwise XOR (comes after arithmetic)
| 9 | `m > n and y < x` | `False and False` | `False` |
| 10 | `y % n == 0` | `15 % 5 == 0 → 0 == 0` | `True` |

***

### Question 3
*(mentally-run code)*

#### a.
```py
s = 0
for i in range(9):
    s += i
    print(i, ':', s)
```
will return:
```
0 : 0
1 : 1
2 : 3
3 : 6
4 : 10
5 : 15
6 : 21
7 : 28
8 : 36
```

#### b.

```py
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, 'x', i, '=', i * j, end = ' ')
        print('\n')
```
the second print statement was kind of misleading to look at, and I couldn't figure out why it wasn't triple-spacing for a bit.
each print statement will create a `\n` automatically, and this one adds an extra explicit `\n`, resulting in two newlines (double spaced). But this just negates the fact that the first print statement overrides its ending newline with a space...  
anyway as written, this would print double-spaced:
```
1 x 1 = 1 

1 x 2 = 2 

2 x 2 = 4 

1 x 3 = 3 

2 x 3 = 6 

3 x 3 = 9 

1 x 4 = 4 

...
(and so on)
...
ending with:

8 x 9 = 72 

9 x 9 = 81 
```

#### c.

```py
mx = 100
cnt = 0
for i in range(1, mx):
    if (i % 3 == 0):
        cnt += 1
        print(i, end = '')
        if (cnt < 11):
            print(end=' ')
        else:
            print(end='\n')
            cnt = 0
```
`end` overrides the default newline, so a newline only gets printed *when* the counter == 11, then it gets reset

```
3 6 9 12 15 18 21 24 27 30 33 
36 39 42 45 48 51 54 57 60 63 66 
69 72 75 78 81 84 87 90 93 96 99
```

#### d.
```py
content = "However, list comprehensions are usually more human
readable than lambda"
account = 0
for c in content:
    if c == 'a':
        account += 1
print(f'there are {account} \'a\' in "{content}"')
```
not sure if the string assignment is intended to be broken across two lines.
if intentional, this would just return an error.
if it's meant to be on one line, it would return:
```
there are 6 'a' in "However, list comprehensions are usually more human readable than lambda"
```

#### e.
```py
ln1 = "---------"
ln2 = '/       /'
i = 1
for i in range(10):
    if (i == 0 or i == 9): # 1st and last line
        print(' '*(9-i), ln1) 
    else:
        print(' '*(9-i), ln2)
```
I think pretty typical way of printing shapes top to bottom that have some kind of slant. It'd be kind of neat to write a little function that also takes in a transformation function as mx + b in params and transforms the output, since monospace text can be treated like a cartesian plane (rounded to integers though haha).  the different quotes on the lines threw me for a bit, wondering if there was some way they would mess up printing one line and not the other.  
anyway the `9` in `' '*(9-i)` is the starting positive X offset. this should return:
```
         ---------
        /       /
       /       /
      /       /
     /       /
    /       /
   /       /
  /       /
 /       /
---------
```

***

## Coding Problems

**Note:** all solutions are functions in `assignment1/src/coding-problem-solutions.py`, which display their output by default and return objects where appropriate.  

### 1 – Largest of Three Numbers

**Interpretation:** Read three numbers from input and output the largest.

**Algorithm:**
1. Prompt for three numbers via input
2. Convert each to float
3. Use `max()` to find the largest number
4. Print & return result

**Name:** `largest_of_3()`

***

### Problem 2 – Parallelogram

**Interpretation:** Use a for loop to print a right-leaning parallelogram shape similar to the snippet from question 3e. Easy to make parametric so might as well.

**Algorithm:**
1. Define the top/bottom and middle lines with dashes and slashes respectively using dimension from params
2. Loop from i = 0 to height, printing the top line followed by middle lines, each with decreasing leading spaces
3. Print the bottom line with no leading space

**Name:** `para_parallelogram()` (get it?)
***

### Problem 3 – Employee Pay Calculator

**Interpretation:** Calculate daily pay based on day type (weekday/weekend) and hours worked. Rates: $15/hr, $21/h on weekends or after 1st 8h on weekdays.

**Algorithm:**
1. Prompt for day type and hours
2. Branch on weekday vs weekend
3. Weekday: compute $15 per hour plus additional $6 per hour over 8 hours
4. For weekends: compute $21 per hour
5. Print/return pay amount

**Name:** `pay_calc()`

***

### Problem 4 – Canadian Federal Income Tax

**Interpretation:** Calculate federal income tax using 2026 progressive brackets from the CRA, excluding credits/deductions (namely the Basic Personal Amount).

**Brackets used (2026 tax year):**
- 14% on the first $58,523
- 20.5% on $58,524 – $117,045
- 26% on $117,046 – $181,440
- 29% on $181,441 – $258,482
- 33% on income $258,483 +

**Algorithm:**
1. Prompt for annual income
2. Iterate through brackets
3. Apply rate to the taxable portion within each bracket
4. Sum and print/return total tax

**Name:** `income_tax()`
***

### Problem 5 – GPA Converter

**Interpretation:** Convert a percentage grade to GPA units using the U of C grading scale. Added letter grades for completeness since they were in the same table I referenced.

**Scale used (University of Calgary / standard Alberta scale):**

| % Range | Letter | GPA |
|---|---|---|
| 90–100 | A+ | 4.0 |
| 85–89 | A | 4.0 |
| 80–84 | A- | 3.7 |
| 77–79 | B+ | 3.3 |
| 73–76 | B | 3.0 |
| 70–72 | B- | 2.7 |
| 67–69 | C+ | 2.3 |
| 63–66 | C | 2.0 |
| 60–62 | C- | 1.7 |
| 55–59 | D+ | 1.3 |
| 50–54 | D | 1.0 |
| < 50 | F | 0.0 |

**Algorithm:**
1. Prompt for percentage grade input
2. Use if/elif chain to match to bracket (could be list of tuples but eh... that felt over-engineered)
3. Print letter grade and GPA

**Name:** `perc_to_GPA()`