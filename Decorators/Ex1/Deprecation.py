#!/usr/bin/env python

def deprecation_warning(func):
    """Decorator for deprecation warning"""
    def deprecated():
        print("This function will not be used departing from 2020...")
        return func()
    return deprecated

@deprecation_warning
def foo():
    print("Dit is een test")

def main():
    foo()

if __name__ == "__main__":
    main()
