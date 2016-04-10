class Car:
    def __init__(self):
        self.color = 0xFF0000
        self.wheel_size = 16
        self.displacement = 2000

    def forward(self):
        print('전진!')

    def backward(self):
        print('후진!')

    def turn_left(self):
        print('좌회전!')

    def turn_right(self):
        print('우회전!')

if __name__ == '__main__':
    car = Car()

    print('0x{:02}'.format(car.color))
    print(car.wheel_size)
    print(car.displacement)

    car.forward()
    car.backward()
    car.turn_left()
    car.turn_right()
