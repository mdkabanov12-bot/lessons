import math

class Camera:
    def __init__(self, x=0, y=5, z=-10, speed=0.01, sensitivity=0.002):
        self.x, self.y, self.z = x, y, z
        self.yaw = 0
        self.pitch = 0
        self.speed = speed
        self.sensitivity = sensitivity

    def move(self, forward, right, up, dt):
        # Расчет векторов направления на основе угла поворота (Yaw)
        forward_x = math.sin(self.yaw)
        forward_z = -math.cos(self.yaw)
        right_x = math.cos(self.yaw)
        right_z = math.sin(self.yaw)

        if forward != 0:
            self.x += forward_x * self.speed * dt * forward
            self.z += forward_z * self.speed * dt * forward
        if right != 0:
            self.x -= right_x * self.speed * dt * right
            self.z -= right_z * self.speed * dt * right
        if up != 0:
            self.y += self.speed * 5 * dt * up

    def rotate(self, dx, dy):
        # Поворот камеры на дельту мыши
        self.yaw -= dx * self.sensitivity
        self.pitch -= dy * self.sensitivity
        # Ограничение Pitch для предотвращения переворота камеры
        if self.pitch > math.pi/5: self.pitch = math.pi/5
        if self.pitch < -math.pi/3: self.pitch = -math.pi/3

    @property
    def position(self):
        return (self.x, self.y, self.z)

    @property
    def rotation(self):
        return (self.yaw, self.pitch)