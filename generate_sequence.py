import itertools
from sage.all import binomial

def generate(n, m, r=1, l=1):
    tuples = [(i, j, k, f) for i in range(n) for j in range(m) for k in range(r) for f in range(l)]

    N = n * m * r * l
    min_ = True
    final_tuples = []
    for k in range(1, N + 1):
        for subset in itertools.combinations(tuples, r=k):
            result_tuple = [set(), set(), set(), set()]
            for c in subset:
                result_tuple[0].add(c[0])
                result_tuple[1].add(c[1])
                result_tuple[2].add(c[2])
                result_tuple[3].add(c[3])

            if (
                len(result_tuple[0]) == n
                and len(result_tuple[1]) == m
                and len(result_tuple[2]) == r
                and len(result_tuple[3]) == l
            ):
                min_ = False
                final_tuples.append(subset)

        if not min_:
            return k, final_tuples


def generate_smart(n, m):  # surj n -> m
    return sum((-1) ** i * binomial(n, i) * (n - i) ** m for i in range(n))


def count_static(a, n):
    for i in range(a, n + 1):
        k, tups = generate(a, i)
        print(k, len(tups))
    print()


def count_static_smart(a, n):
    for i in range(a, n + 1):
        k = a + i
        ltups = generate_smart(a, i)
        print(k, ltups)
    print()

#count_static(2, 10)
# count_static(2, 10)
# count_static(3, 10)
# count_static(4, 10)
# count_static_smart(1, 10)
# count_static_smart(2, 10)
# count_static_smart(3, 10)
# count_static_smart(4, 10)

#k, tups = generate(2, 3, 1)
#print(len(tups))

#k, tups = generate(2, 3, 3)
#print(k, len(tups))
#print(generate_smart(2, 3) * generate_smart(3, 3))
#k, tups = generate(2, 3, 4)
#print(k, len(tups))
#print(generate_smart(2, 4) * generate_smart(3, 4))
#k, tups = generate(2, 3, 5)
#print(k, len(tups))
#print(generate_smart(2, 5) * generate_smart(3, 5))
#k, tups = generate(2, 3, 6)
#print(k, len(tups))
#print(generate_smart(2, 6) * generate_smart(3, 6))
#k, tups = generate(2, 3, 7)
#print(k, len(tups))
#print(generate_smart(2, 7) * generate_smart(3, 7))


#k, tups = generate(2, 3, 4, 5)
#print(k, len(tups))

#total_covereges = generate_smart(2, 5) * generate_smart(3, 5) * generate_smart(4, 5)
#M = 2 * 3 * 4 * 5
#total_choices = binomial(M, 5)
#
#print("Covereges: ", total_covereges)
#print("Random choices: ", total_choices)
#print("Prob: ", total_covereges * 100 / total_choices, "%")


def find_prob(versions):
    versions = sorted([len(v) for v in versions])
    N = max(versions)
    M = N
    total_coverages = 1
    for v in versions[:-1]:
        total_coverages *= generate_smart(v, N)
        M *= v

    total_choices = binomial(M, N)
    return total_coverages * 100 / total_choices

# TODO: generalaize to not perfect choices and come up with an algorithm to construct one

#versions = [["0.1", "0.2", "0.3"], ["1.2", "1.3", "1.7", "1.19"], ["2.3", "2.5", "2.11", "2.20", "3.0"]]
#print(find_prob(versions), "%")
