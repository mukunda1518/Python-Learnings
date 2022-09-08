class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0

    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False

    def accelerate(self):
        if self.is_engine_started:
            if self.current_speed + self.acceleration <= self.max_speed:
                self.current_speed += self.acceleration
        else:
            print("Car has not started yet")

    def apply_brakes(self):
        if self.current_speed - self.tyre_friction >= 0:
            self.current_speed -= self.tyre_friction
        else:
            self.current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car has not started yet")


def default_test():
    car = Car(color="Blue", max_speed=150, acceleration=20, tyre_friction=2)
    print(car.color)
    print(car.max_speed)
    print(car.acceleration)
    print(car.tyre_friction)

    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    print(car.is_engine_started)  # As car is not yet started, it should print False
    car.start_engine()  # Starting the engine
    print(car.is_engine_started)  # As engine is on, it should print True
    car.stop_engine()  # Stopping the engine
    print(car.is_engine_started)  # As engine is off, it should print False

    car = Car(color="Red", max_speed=50, acceleration=10, tyre_friction=3)
    car.accelerate()  # Calling the accelerate method when the is_engine_started is False
    # The above line will print "Car has not started yet"
    print(car.current_speed)
    car.start_engine()  # Starting the car engine
    print(car.current_speed)  # Car engine is started but not yet accelerated => 0
    car.accelerate()  # Calling the accelerate method when the is_engine_started is True
    print(car.current_speed)  # current_speed value has increased by acceleration value (0 + 10 => 10)
    car.accelerate()
    print(car.current_speed)  # current_speed value is 10 and increasing again by acceleration value (10 + 10 => 20)
    car.accelerate()
    car.accelerate()
    car.accelerate()
    print(car.current_speed)
    car.accelerate()  # Accelerating the car more than its max_speed
    print(car.current_speed)  # Any car cannot accelerate more than its max_speed => 50

    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    car.start_engine()
    car.accelerate()  # Calling the accelerate method when the is_engine_started is True
    print(car.current_speed)  # 10
    car.apply_brakes()  # Calling the apply_brakes method
    # current_speed of the car should decrease according to the tyre_friction value.
    print(car.current_speed)  # (10 - 3 => 7)
    car.apply_brakes()
    print(car.current_speed)  # 7 - 3 => 4
    car.apply_brakes()
    print(car.current_speed)  # 4 - 3 => 1
    car.apply_brakes()
    print(car.current_speed)  # 1 - 3 => 0 (current_speed should never go behind 0.)

    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    car.sound_horn()  # Calling the accelerate method when the is_engine_started is False
    car.start_engine()  # Starting the engine
    car.sound_horn()  # Calling the accelerate method when the is_engine_started is True


default_test()
