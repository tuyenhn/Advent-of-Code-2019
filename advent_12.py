class planet:
    def __init__(self, pos_li: list):
        self.x = pos_li[0]
        self.y = pos_li[1]
        self.z = pos_li[2]
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def set_vel_x(self, vel_x):
        self.vel_x += vel_x

    def set_vel_y(self, vel_y):
        self.vel_y += vel_y

    def set_vel_z(self, vel_z):
        self.vel_z += vel_z

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z


p1 = planet([-2, 9, -5])
p2 = planet([16, 19, 9])
p3 = planet([0, 3, 6])
p4 = planet([11, 0, 11])

# p1 = planet([-1, 0, 2])
# p2 = planet([2, -10, -7])
# p3 = planet([4, -8, 8])
# p4 = planet([3, 5, -1])

planets = [p1, p2, p3, p4]

for _ in range(1000):
    x_pos = [p.x for p in planets]
    y_pos = [p.y for p in planets]
    z_pos = [p.z for p in planets]
    for p in planets:
        p_x = p.x
        p_y = p.y
        p_z = p.z
        temp_vel_x = 0
        temp_vel_y = 0
        temp_vel_z = 0

        for x_p in x_pos:
            if p_x < x_p:
                temp_vel_x += 1
            elif p_x > x_p:
                temp_vel_x -= 1
        p.set_vel_x(temp_vel_x)

        for y_p in y_pos:
            if p_y < y_p:
                temp_vel_y += 1
            elif p_y > y_p:
                temp_vel_y -= 1
        p.set_vel_y(temp_vel_y)

        for z_p in z_pos:
            if p_z < z_p:
                temp_vel_z += 1
            elif p_z > z_p:
                temp_vel_z -= 1
        p.set_vel_z(temp_vel_z)

    for p in planets:
        p.update()


# PART ONE - SOLVED
total_es = []
for p in planets:
    total_es.append((abs(p.x) + abs(p.y) + abs(p.z)) *
                    (abs(p.vel_x) + abs(p.vel_y) + abs(p.vel_z)))

print(sum(total_es))
