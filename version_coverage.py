import itertools

class Package:
    def __init__(self, name: str, version: int):
        self.name = name
        self.version = version

    def __repr__(self):
        return f"{self.name}:{self.version}"

class Machine:
    def __init__(self, packages: list[Package] = []):
        self.packages = {pack.name: pack.version for pack in packages}

    def add_package(self, package: Package):
        assert package.name not in self.packages
        self.packages[package.name] = package.version

    def upgrade_package(self, package: Package):
        assert package.name in self.packages
        self.packages[package.name] = package.version

    def dump_packages(self):
        return self.packages

    def __hash__(self):
        return hash(tuple(self.packages))

    def __repr__(self):
        return str(self.packages)

#def naive_changable_and_appendable(machines: list[Machine])

def naive_immutable(machines: list[Machine], deps: list[str]):
    candidates = [m for m in machines if all(name in m.dump_packages() for name in deps)]

    def merge(machines, deps):
        totals = {pack_name: set() for pack_name in deps}
        for m in machines:
            for pack in deps:
                totals[pack].add(m.packages[pack])
        return totals

    totals = merge(candidates, deps)
    N = len(candidates)
    for k in range(1, N + 1):
        for subset in itertools.combinations(candidates, r=k):
            cur_totals = merge(subset, deps)
            if cur_totals == totals:
                return subset

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
    
    print(naive_immutable([m1, m2, m3, m4, m5], ["python", "perl"]))
