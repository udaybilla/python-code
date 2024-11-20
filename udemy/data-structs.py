## Learning different data structures in python and writing some code on it
## 4 built in data types that we can use Lists, Tuples, Sets, Dictionaries

SITE = 'https://jerrynsh.com/tuples-vs-lists-vs-sets-in-python/'

## What are the main takeaways?

## If you need to store duplicates, go for List or Tuple.
## For List vs. Tuple, consider mutability. If you need immutability, go for Tuple.
## If you do not need to store duplicates, always go for Set or Dictionary. Hash maps are significantly faster when it comes to determining if an object is present in the Set (e.g. x in set_or_dict).

### Lists
UDAY_INVENTORY=[1,3,3,4,4,8]

### Tuple
SONY_INVENTORY=(1,3,3,4,5)

### Sets (set cannot contain duplicates)
BABY_INVENTORY={1,3,3,8,7}

### Dictonaries (Cannot have duplicates)
BABY_CLASS={'diapers': 3, "gear": "stroller"}