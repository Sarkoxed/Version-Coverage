from version_coverage import Machine, Package
import random
import time

#class bucket_queue:
#    def __init__

def greedy_search(machines, deps: set[str], rand: bool = False):
    if rand:
        random.seed(time.time())

    def assemble_ground_set(machines):
        S = set()
        for m in machines: 
            S |= m
        return S

    def weight(m, C):
        return len(m & C)
    
    S = [set(m.packages.items()) for m in machines if all(x in deps for x in m.packages)]
    U = assemble_ground_set(S)

    S_prime = []
    C = set()
    
    while C != U:
        key_f = lambda x: weight(x, C)
        S1 = min(S, key=key_f)  
        if rand:
            kk = key_f(S1)
            S1 = random.choice([x for x in S if key_f(x) == kk])

        C |= S1
        S_prime.append(S1)
    
    res = []
    for m in machines:
        if set(m.packages.items()) in S_prime and m not in res:
            res.append(m)
    return res

# Thoughts
# if we want 1 coverage: => sort and take first every change of first
# if we want 2 coverage: =>

if __name__ == "__main__":
    python2 = Package("python", 2)
    python3 = Package("python", 3)
    
    perl2 = Package("perl", 2)
    perl3 = Package("perl", 3)
    
    rust2 = Package("rust", 2)
    rust3 = Package("rust", 3)
    rust4 = Package("rust", 4)

    m1 = Machine([python2, perl2, rust3])
    m2 = Machine([python3, perl2, rust4])
    m3 = Machine([python2, perl3, rust2])
    m4 = Machine([python2, perl3, rust4])
    m5 = Machine([python3, perl2, rust3])
    
    machines = [m1, m2, m3, m4, m5]

    print(greedy_search(machines, {"python", "perl", "rust"}))
