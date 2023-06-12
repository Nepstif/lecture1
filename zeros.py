
def zeros(n):
    count= 0
    while n >= 5:
        n = n // 5
        count += n
    return count

print(zeros(12))


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7