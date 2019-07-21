def work_sched(s, max_week, max_day):
    results = []
    cur_week = 0
    for i in range(len(s)):
        if s[i].isdigit():
            cur_week += int(s[i])
    recurse(s, 0, "", cur_week, max_week, max_day, results)
    return results


def recurse(s, start, partial, cur_week, max_week, max_day, results):
    if cur_week == max_week and len(partial) == len(s):
        results.append(partial)
        return
    elif cur_week>max_week or start>=len(s):
        return
    if s[start] == "?":
        for i in range(0, max_day+1):
            recurse(s, start+1, partial+str(i), cur_week+i, max_week, max_day, results)
    else:
        recurse(s, start+1, partial+s[start], cur_week, max_week, max_day, results)

if __name__ == '__main__':
    pattern = "08???80"
    total = 24
    result=work_sched(pattern,total,4)
    print(result)