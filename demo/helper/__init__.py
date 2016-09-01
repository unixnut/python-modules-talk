from . import helper2

def say_hi():
    print(string_help() + " " + helper2.more_help())

def string_help():
    return "foo"


__all__ = (say_hi, )
