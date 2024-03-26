def title_to_director(movies):
    return {m.title : m.director for m in movies}

def director_to_titles(movies):
    return {m1.director : [m2.title for m2 in movies if m2.director == m1.director] for m1 in movies}