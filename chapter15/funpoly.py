
# polymorphism in function 

class pen:
    def use(self):
        return "writting"

class Eraser:
    def use(self):
        return "erasing"

def perform_task(tool):
    print(tool.use())

perform_task(pen())
perform_task(Eraser())