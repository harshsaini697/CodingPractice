def asteroidCollision( asteroids):
    ans = []
    for new in asteroids:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
                continue
            elif ans[-1] == -new:
                ans.pop()
            break
        else:
            ans.append(new)
    return ans

print(asteroidCollision([5,10,-5,10,-10]))