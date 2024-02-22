#!/usr/bin/python3
"""
Purpose: Function with position-only arguments

    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        -----------    ----------     ----------
            |             |                  |
            |        Positional or keyword   |
            |                                - Keyword only
            -- Positional only

    When to use positional-only arguments
        Use positional-only if names do not matter or have no meaning, and there are only a few arguments which will always be passed in the same order.
        Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names.

NOTE: Introduced in python 3.8
"""
def sample(a,b,/,c,*,d,e):
    sum = a+b+c+d+e
    sub = a-b-c-d-e
    multi = a*b*c*d*e
    return sum,sub,multi

sum,sub,multi = sample(12,13,c=45,d=3,e=5)
print(f"sum :{sum} sub :{sub} multi :{multi}")
