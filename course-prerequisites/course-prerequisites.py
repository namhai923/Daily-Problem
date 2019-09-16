def courses_to_take(course_to_prereqs):
    result = []
    for _ in range (0, len(course_to_prereqs)):
        for key in course_to_prereqs:
            if set(course_to_prereqs[key]).issubset(set(result)):
                if key not in result:
                    result.append(key)
                else:
                    continue
    if len(result) == 0:
        return 'NULL'
    return result

courses = {'CSC300': ['CSC100','CSC200'],
            'CSC200': ['CSC100'],
            'CSC100': []
}

print(courses_to_take(courses))