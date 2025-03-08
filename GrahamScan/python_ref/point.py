''' Definition of a Point.

In the reference version, this is just a type
alias for a tuple.  I put it in a separate
module so that if that changes, the change
is purely local to here.
'''

type Point = tuple[int,int]
