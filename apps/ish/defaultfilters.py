from django import template


def mult(value, arg):
    return int(value) * int(arg)


def sub(value, arg):
    return int(value) - int(arg)


def div(value, arg):
    return int(value) / int(arg)


def add(value, arg):
    return int(value) + int(arg)


template.register_filter("mult", mult, True)
template.register_filter("sub", sub, True)
template.register_filter("div", div, True)
template.register_filter("add", add, True)
