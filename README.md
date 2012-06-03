# biggraphs

Biggraphs is a fun project using graphviz for visualizing the numbers that share large amounts of common factors.

## usage

./runme.sh X Y

Graphs edges between each number a, b such that
   a, b in cartesian product of {1..X} with itself,
   a != b,
   |factors(a) U factors(b)| > Y

## results

<img src="" alt="First result of using graphviz to draw point-cloud like graphs" />

<img src="" alt="Second result of using graphviz to draw points with edges" />