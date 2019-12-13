class planet:
    def __init__(self, pos_li: list):
        self.x = pos_li[0]
        self.y = pos_li[1]
        self.z = pos_li[2]
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def set_vel_x(self, vel_x):
        self.vel_x = vel_x

    def set_vel_y(self, vel_y):
        self.vel_y = vel_y

    def set_vel_z(self, vel_z):
        self.vel_z = vel_z

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z


# p1 = planet([-2, 9, -5])
# p2 = planet([16, 19, 9])
# p3 = planet([0, 3, 6])
# p4 = planet([11, 0, 11])

p1 = planet([-1, 0, 2])
p2 = planet([2, -10, -7])
p3 = planet([4, -8, 8])
p4 = planet([3, 5, -1])

planets = [p1, p2, p3, p4]

for _ in range(10):
    x_pos = [p.x for p in planets]
    x_pos.sort()
    for p in planets:
        idx = x_pos.index(p.x)
        if idx == 0:
            p.set_vel_x(3)
        elif idx == 1:
            p.set_vel_x(1)
        elif idx == 2:
            p.set_vel_x(-1)
        else:
            p.set_vel_x(-3)

    y_pos = [p.y for p in planets]
    y_pos.sort()
    for p in planets:
        idx = y_pos.index(p.y)
        if idx == 0:
            p.set_vel_y(3)
        elif idx == 1:
            p.set_vel_y(1)
        elif idx == 2:
            p.set_vel_y(-1)
        else:
            p.set_vel_y(-3)

    z_pos = [p.z for p in planets]
    z_pos.sort()
    for p in planets:
        idx = z_pos.index(p.z)
        if idx == 0:
            p.set_vel_z(3)
        elif idx == 1:
            p.set_vel_z(1)
        elif idx == 2:
            p.set_vel_z(-1)
        else:
            p.set_vel_z(-3)

    for p in planets:
        p.update()

total_es = []
for p in planets:
    total_es.append((p.x + p.y + p.z) * (p.vel_x + p.vel_y + p.vel_z))

print(sum(total_es))
