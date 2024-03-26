from util import Card

def genres(movies):
    return {g for m in movies for g in m.genres}

def actors(movies):
    return {a for m in movies for a in m.actors}

def repeat_consecutive(xs, n):
    return [i for i in xs for _ in range(n)]

def repeat_alternating(xs, n):
    return [i for _ in range(n) for i in xs]

def cards(values, suits):
    return {Card(v, s) for s in suits for v in values}