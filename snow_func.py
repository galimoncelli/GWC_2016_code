class SnowFlake():
    def __init__(self, size, position, wind):
        self.size = size
        self.position = position
        self.wind = wind
        self.snow_list = []

    
    def fall(self, speed):
        self.position[1] += speed  
        if self.wind:              #makes wind move random direction when parameter true
            self.position[0] += random.randint(-speed, speed)
        
    def draw(self):
        pygame.draw.circle(screen, WHITE, self.position, 3)
