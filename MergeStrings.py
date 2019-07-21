c = []
a = "abc"
b = "stuvwx"
for x in range(max(len(a),len(b))):
    c.append(a[x] if x < len(a) else '')
    c.append(b[x] if x<len(b) else '')
print(c)