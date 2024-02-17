# Write your code here
def process_data(string_data: list[str]):
    out = {}
    for substring in string_data:
        split = substring.split(',')
        name  =     split[0]
        age   = int(split[1])
        courses =   split[2:]
        out[name] = {'age': age, 'courses': courses}
    return out

def average_age(data: dict):
    t_age = 0
    for key in data:
        t_age += data[key]['age']
    return t_age / len(data)

def courses(data: dict):
    courses = set()
    for key in data:
        for course in data[key]['courses']:
            courses.add(course)
    return courses

def most_common_course(data: dict):
    courses = {}
    for key in data:
        for course in data[key]['courses']:
            courses[course] = courses.get(course, 0) + 1
    
    max_count = max(courses, key=lambda x: courses[x])
    return { course for item in courses if courses[item] == max_count }