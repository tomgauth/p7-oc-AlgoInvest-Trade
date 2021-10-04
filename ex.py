iterable = ['A', 'B', 'C', 'D']


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    print("START FUNCTION")
    pool = tuple(iterable)
    print("pool: ", pool)
    n = len(pool)
    print("n: ", n)
    if r > n:
        print("r > n:", r, " > ", r)
        return
    indices = list(range(r))  # [0, 1, 2]
    print("indices: ", indices)
    # yield tuple(pool[i] for i in indices)
    print(" ----- ")
    while True:
        for i in reversed(range(r)):  # range iterator object [2, 1, 0]
            print("   indices[i]: ", indices[i])  # 2
            print("   i: ", i)  # 2
            print("   i + n - r: ", i + n - r)
            if indices[i] != i + n - r:  # 2 != 2 + 4 - 3 True
                print("     True: ", indices[i], " != ", i + n - r)
                break
        else:
            print("   else! return")
            return
        print("exit for loop")
        indices[i] += 1
        print(" incremented indices[i]: ", indices[i])
        print(" range(i+1), r: ", range(i+1, r))
        for j in range(i+1, r):  # for j in [?]
            print("   j: ", j)
            print("   indices[j-1] + 1: ", indices[j-1] + 1)
            indices[j] = indices[j-1] + 1
            print("   indices[j]: ", indices[j])

        yield tuple(pool[i] for i in indices)


for i in combinations(iterable, 3):
    print("RESULTS:   ", i)
