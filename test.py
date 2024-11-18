from version_coverage import Machine, Package, naive_immutable
from version_coverage2 import greedy_search
from generate_sequence import find_prob
from random import randint, choice
from time import time
from pprint import pprint

N = 20
deps = {"python", "perl", "java", "rust", "haskell", "c++", "node", "pizda"}

packages = {}
for dep in deps:
    packages[dep] = []
    for i in range(randint(1, 10)):
        packages[dep].append(Package(dep, i))

machines = []
for i in range(N):
    machine_packs = [choice(versions) for versions in packages.values()]
    machines.append(Machine(machine_packs))


def optimal_number(machines, deps):
    packs = {dep: set() for dep in deps}
    for m in machines:
        for name, v in m.packages.items():
            if name in deps:
                packs[name].add(v)
    return max([len(x) for x in packs.values()])


def prob(machines, deps):
    packs = {dep: set() for dep in deps}
    for m in machines:
        for name, v in m.packages.items():
            if name in deps:
                packs[name].add(v)

    return find_prob([x for x in packs.values()])

pprint(machines)
print()
print(f"Optimal number of entries: {optimal_number(machines, deps)}")
print(f"Probability of choosing at random: {prob(machines, deps)}%")
print()
start = time()
res1 = greedy_search(machines, deps)
end = time()
print(f"Greedy: #{len(res1)}, time: {end - start}")
pprint(res1)

start = time()
res0 = naive_immutable(machines, deps)
end = time()
print(f"Naive: #{len(res0)}, time: {end - start}")
pprint(res0)
