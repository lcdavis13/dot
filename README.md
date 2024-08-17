# dot-accessible dictionaries and dictionary-containing classes

`dicy`: dot-accessible dictionary

`ency`: dot-accessible "ecyclopedia" - a custom class containing one or more dictionaries, and possibly other data. 
This is intended to be used as an abstract class, inherited in your custom data class. 
If there are multiple contained dictionaries, they are prioritized based on the explicit ordering. When there are two or more identical keys exist in contained dictionaries, the priority determines which is accessed.

Features:
- dot-accessed create*/read/update/delete operations for dictionary keys
- IDE auto-completion**
- pickle serialization

*: Key creation can be dot-accessed for `dicy`. In `ency`, dot-create adds a new class attribute, as is standard in python. 
**: Auto-complete is tested in pycharm but others should work.


# Installation

> pip install dotsy

# example usage

> from dotsy import dicy
> 
> dd = dicy({"a": 1})
> 
> print(dd.a) # prints 1
> 
> dd.b = 2
> 
> print(dd["b"]) # prints 2
> 
> dd.c = dicy({"i": 3})
> 
> print(dd.c.i) # prints 3

