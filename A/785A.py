# Time: 1575 ms
# Memory: 9284 KB
n = int(input())
poly = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
sol = 0
for i in range(n):
	si = str(input())
	sol += poly[si]
print(sol)
