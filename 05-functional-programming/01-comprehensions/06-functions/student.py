import re


def movie_count(movies, director):
    return len([m for m in movies if m.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([m.runtime for m in movies if actor in m.actors])

def has_director_made_genre(movies, director, genre):
    return any([m for m in movies if m.director == director and genre in m.genres])

def is_prime(n):
    if 0 == n or n == 1:
        return False
    return not any([i for i in range(2, n) if n % i == 0])

def is_increasing(ns):
    return all([comp[0] <= comp[1] for comp in zip(ns, ns[1:])])

def count_matching(xs, ys):
    return len([n for n in zip(xs, ys) if n[0] == n[1]])

def weighted_sum(ns, weights):
    return sum(n[0] * n[1] for n in zip(ns, weights))

def alternating_caps(string: str):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(string)])

def find_repeated_words(sentence: str):
    words = list(map(lambda s: s.lower(), re.findall(r'(\w+)', sentence)))
    return {word[0] for word in zip(words, words[1:]) if word[0] == word[1]}