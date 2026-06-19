# Use *args to build a function that totals any number of numbers passed to it.
def _add_argus(*args):
    return sum(args)
    
print(_add_argus(2,3))
print(_add_argus(67,34))