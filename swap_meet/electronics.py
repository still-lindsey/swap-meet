from .item import Item

class Electronics(Item):
    # def __init__(self, category = "Electronics", condition = 3.5, age = 2):
    #     self.category = category
    #     self.condition = condition
    #     self.age = age
    def __init__(self, category = "Electronics", condition = 3.5, age = 2):
        super().__init__(category, condition, age)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."

