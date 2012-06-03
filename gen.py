import math
import sys

def factors(n):  
    """
    return the factors of n
    """
    factors = [1, n] # ever integer has 1 and itself as factors
    check = 2
    while check <= math.sqrt(n):  
        if n % check == 0:
            factors.append(check)
            factors.append(n / check)
        check += 1
    factors.sort()  
    return factors

def factsim(a, b, memdict={}, memo=True):
    """
    the number of common factors between a, b
    """
    if memo:
        if a not in memdict:
            memdict[a] = factors(a)
        if b not in memdict:
            memdict[b] = factors(b)
        afact = memdict[a]
        bfact = memdict[b]
    else:
        afact = factors(a)
        bfact = factors(b)
    return len(set(afact).intersection(set(bfact)))

# defaults for run
X = 100
Y = 5
def run(x, y):
    """
    Generates a DOT files for graphviz:

    print edges between each number a, b such that:
      a, b in cartesian product of the first x integers
      a != b and
      |factors(a) intersect factors(b)| > y

    result is a dot file
    """
    fi = """# Generated with the commant $ python gen.py %s %s
graph test123 {
        graph [bgcolor="#FFFFFF", outputorder="edgesfirst", dpi=1000];
        node [width=0.0008, fixedsize=true, shape=point, color="#00000099"];
        edge [penwidth=0.1, color="#00000099"]
    """ % (x, y)
    for a in xrange(1,x):
        for b in xrange(1,x):
            if a != b and factsim(a,b) > y:
                fi += "\t%s -- %s;\n" % (a,b)
    fi += "}\n"
    return fi

if __name__ == "__main__":
    x = int(sys.argv[1]) if len(sys.argv) > 1 else X
    y = int(sys.argv[2]) if len(sys.argv) > 2 else Y
    print(run(x, y))
