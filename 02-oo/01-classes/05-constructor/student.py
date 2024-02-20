class Wall:
    def __init__(self, depth, width, height) -> None:
        self.depth = depth
        self.width = width
        self.height = height
        self.volume = depth * width * height
        