class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")

    def changeGear(self):
        print("changing gear")

    
audi = Car("r8","blue","audi",180)
print(audi.start())

