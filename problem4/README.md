## tutorialAI
### Problem 4

Some puzzles courtesy of [AIND](https://gist.github.com/napratin/42dff8b1e66950fbc66ed6d38b3095f6).


## Wheel of Chance

![Wheel of Chance](https://gist.githubusercontent.com/napratin/42dff8b1e66950fbc66ed6d38b3095f6/raw/6c6ff468e4ec394b92539ef59effbdd4a9d7046f/Wheel-of-Chance.png)

In this game of chance, we have a wheel divided into 8 equal sectors or pie slices. 4 of them are marked $200, 3 are $500 and 1 is $1000.

It costs you $100 to place a bet on any one of the unique numbers on the wheel, and spin once. If the wheel stops with the arrow pointing at the number you chose, you win that amount plus your $100 back, otherwise you lose your bet.

Assuming all sectors are equally likely, what is the ﻿⁠⁠expected value﻿⁠⁠ of betting on each number ($200, $500 and $1000)?


## Narcissistic Numbers

A ﻿⁠⁠_narcissistic number﻿⁠⁠_ is an ﻿⁠⁠⁠⁠`n﻿⁠⁠⁠⁠`-digit whole number that is equal to the sum of its digits raised to the power ﻿⁠⁠⁠⁠`n﻿⁠⁠⁠⁠`. For instance, ﻿⁠⁠⁠⁠`153﻿⁠⁠⁠⁠` is such a 3-digit number (﻿⁠⁠⁠⁠`1^3 + 5^3 + 3^3 = 153﻿⁠⁠⁠⁠`) and ﻿⁠⁠⁠⁠`8208﻿⁠⁠⁠⁠` is a 4-digit example (﻿⁠⁠⁠⁠`8^4 + 2^4 + 0^4 + 8^4 = 8208﻿⁠⁠⁠⁠`).

Write a function ﻿⁠⁠⁠⁠`is_narcissistic(x)﻿⁠⁠⁠⁠` that returns ﻿⁠⁠_true﻿⁠⁠_ if ﻿⁠⁠⁠⁠`x﻿⁠⁠⁠⁠` is narcissistic. Now use this to find as many narcissistic numbers as you can. How high up can you go?

﻿⁠⁠_Note: 1-digit numbers are all trivially narcissistic, so you may skip them.﻿⁠⁠_


## Knights & Knaves﻿⁠⁠⁠

You are shipwrecked on an unknown island where there are two kinds of people - Knights & Knaves. Knights always tell the truth and knaves always lie. To survive, you need to know who is who.

For each person in the following scenarios, can you figure out if they are a knight or a knave?
Support your answer with a logical justification / proof.

1. Persons: A & B
- A says: “B is a knave.”
- B says: “We are both knights.”

2. Persons: A & B
- A says: “We are both knights."
- B says: “We are both knaves.”

3. Persons: A, B & C
- A says: “B is a knave.”
- B says: “C is a knave.”
- C says: “B and myself are knights.”

4. Persons: A & B
- A says: “At least one of the two of us is a knight.”
- B says: “La la la!”


## OOP Scavenger Hunt

Python has supported Object Oriented Programming from its beginning, but not everyone makes use of this paradigm.  How well do you understand inheritance and instantiation, and their mechanics as it relates to Python?  Open the `search.py` file at Norvig's library link below and find an example of each of the following *as they are related to* the `GraphProblem` class found at *line 789* of `search.py`. All of the answers are found in this one large module, and there are more than one answer for a number of the items. You can list your answers in the form:

```item, name, line-number
class, GraphProblem, 789
parent class, ... , ... ```

> *Item*
> 1. parent class
> 2. Instance variable - inherited
> 3. instance variable - added in this subclass
> 4. constructor - inherited but overridden
> 5. function - inherited but overridden
> 6. function - inherited and NOT overridden
> 7. function - added in this subclass
> 8. sibling class (has same parent class)
> 9. child class (subclassed from GraphProblem)
> 10. instantiated GraphProblem object

AIMA Code - Python:
https://github.com/aimacode/aima-python/blob/master/search.py


## Latin Squares

An `r` × `n` Latin rectangle based on `1`, …, `n` is a 2-dimensional array of `r` rows and `n` columns, where `r` < `n`, such that each entry is one of the integers `1`, …, `n` and each of these integers occurs _at most once_ in each row and _at most once_ in each column.

Is it true that every `r` × `n` Latin rectangle can be extended to an `n` × `n` Latin rectangle (a _Latin square_)? Why or why not?


## Unconscious Bias

You have a coin that, when flipped, lands on heads with probability `p` and tails with probability `1-p`, but `p` is unknown. How can we use this coin to generate an unbiased random process that returns `0` or `1` with equal probability?


## Voting Tree

Consider a uniform rooted tree of height `h`; that is, every leaf is at distance `h` from the root. Every internal node (including the root) has three children. Each leaf has a value of either `0` or `1` associated with it, unknown to us, and each transmits its value to its parent. Each internal node computes the value transmitted to it by the majority of its children and then transmits this value to its parent node. In the end, a final value will be computed by the root by majority vote of its children.

The evaluation problem consists of determining what the value of the root will be by only reading the values at the children. At each step, an algorithm can choose one leaf whose value it wishes to read.

Consider the recursive algorithm that evaluates the first two children of the root. If these values agree, the root takes the value of those two children. If the children’s values disagree, the algorithm evaluates the third subtree to determine which value has the majority vote.

What is the expected number of leaves that will be inspected during a given run of the algorithm?