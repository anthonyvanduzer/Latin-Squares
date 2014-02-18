permpy
=======

## A Python Permutations Class

Contains Various tools for working interactively with permutaions. 
Easily extensible. 


Installation
------------

Python 3 not yet supported.
The easiest way is to install is to use 

    git clone https://github.com/cheyneh/permpy.git

This will copy the package into the current directory. 
If you don't have a git client, you can download the package 
as a zip file from 
[here](http://github.com/cheyneh/permpy/zipball/master/).

Then just use 

    import permpy

or

    from permpy import *
    
    
### Examples:
```python
>>>
>>> import permpy as pp
>>> 
>>> 
>>> p = pp.Perm.random(8)
>>> 
>>> p
 5 4 7 1 6 2 3 8 
>>> 
>>> 
>>> p.cycles()
'( 6 2 4 1 5 ) ( 7 3 ) ( 8 )'
>>> 
>>> p.order()
10
>>> 
>>> p ** 10
 1 2 3 4 5 6 7 8
>>>

>>> S = pp.PermSet.all(6)
>>> 
>>> S
 Set of 720 permutations
>>> 
>>> S.total_statistic(Perm.inversions)
 5400
>>> 
>>> S.total_statistic(Perm.descents)
 1800
>>> 

>>> 
>>> A = pp.AvClass([ [1,3,2] ])
>>> 
>>> A
[Set of 0 permutations,
 Set of 1 permutations,
 Set of 2 permutations,
 Set of 6 permutations,
 Set of 24 permutations,
 Set of 120 permutations,
 Set of 720 permutations,
 Set of 5040 permutations,
 Set of 40320 permutations]
>>> 
>>> 
>>> p = Perm.random(12)
>>> p
 3 6 11 12 7 9 4 8 10 2 1 5 
>>>
>>> q = Perm([ 1324 ])
>>>
>>> p.avoids(q)
 False
>>>
```
