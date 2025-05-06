#13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine object is part of Car

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Access Engine's method via Car

# Create Engine object
my_engine = Engine()

# Pass Engine to Car
my_car = Car(my_engine)

# Start the car (which starts the engine)
my_car.start_car()
