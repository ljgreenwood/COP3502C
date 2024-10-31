class Cow:
    """
    facilittes the creation and use of cow objects
    """
    def __init__(self, name=None):
        self.name = name
        self.image = None
    def get_name(self):
        return self.name 
    def set_image(self, image):
        self.image = image
    def get_image(self):
        return self.image 
         
