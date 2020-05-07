cache = {}

def expensive_seq(x, y, z):
    if x <= 0:
        return y + z

    if x > 0:
        first_tup = (x - 1, y + 1, z)
        sec_tup = (x - 2, y + 2, z * 2)
        third_tup = (x - 3, y + 3, z * 3)
    
    if first_tup not in cache:
        cache[first_tup] = expensive_seq(x - 1, y + 1, z)
    if sec_tup not in cache:
        cache[sec_tup] = expensive_seq(x - 2, y + 2, z * 2)
    if third_tup not in cache:
        cache[third_tup] = expensive_seq(x - 3, y + 3, z * 3)

    return cache[first_tup] + cache[sec_tup] + cache[third_tup]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
