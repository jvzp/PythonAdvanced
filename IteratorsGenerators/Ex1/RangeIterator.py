#!/usr/bin/env python3

class my_first_iterable_class:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return my_first_iterable_class_iterator(self)


class my_first_iterable_class_iterator:
    def __init__(self, my_first_iterable_class):
        self.current = my_first_iterable_class.start-1
        self.stop = my_first_iterable_class.stop-1

    def __next__(self):
        if self.stop == self.current:
            raise StopIteration
        else:
            self.current += 1
            return self.current

def main():
    for i in my_first_iterable_class(0,10):
        print ("{}".format(i))

if __name__ == "__main__":
    main()
