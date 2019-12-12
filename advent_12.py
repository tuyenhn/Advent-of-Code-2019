inp = """<x=-2, y=9, z=-5>
<x=16, y=19, z=9>
<x=0, y=3, z=6>
<x=11, y=0, z=11>""".split('\n')

positions = []
for vect in inp:
    temp = vect.strip('<>').split(', ')
    temp = [int(n[2:]) for n in temp]

    print(temp)
