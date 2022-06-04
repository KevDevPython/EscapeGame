class BaseLighting:
    def __init__(self, xapx, yapx, color, brightness):
        self.xapx, self.yapx = xapx, yapx
        self.color = color
        self.brightness = brightness
        self.on = False

    def draw(self):
        pass


class PointLight(BaseLighting):
    def __init__(self, xapx, yapx, color, brightness, radius):
        super(PointLight, self).__init__(xapx, yapx, color, brightness)
        self.radius = radius

    def draw(self):
        pass


class DirectionalLight(BaseLighting):
    def __init__(self, xapx, yapx, color, brightness, dmax, dmin, angle, direction):
        super(DirectionalLight, self).__init__(xapx, yapx, color, brightness)
        self.dmax, self.dmin = dmax, dmin
        self.angle = angle
        self.direction = direction

    def draw(self):
        pass