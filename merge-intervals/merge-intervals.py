def merge(intervals):
    out = []
    intervals = sorted(intervals, key=lambda i:i[0])
    for i in intervals:
        if out and int(i[0]) <= int(out[-1][-1]):
            out[-1] = list(out[-1])
            out[-1][-1] = max(out[-1][-1], i[-1])
            out[-1] = tuple(out[-1])
        else:
            out.append(i)
    return out

print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))