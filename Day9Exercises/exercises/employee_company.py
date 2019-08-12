from Day9Exercises.Classes.Employee import Employee

new_employee = Employee('Adam', 'Kropkowski', 0)
new_employee.say_hello()
another_new_employee = Employee('Franek',)
another_new_employee.say_hello()


from Day9Exercises.Classes.Articles import bike_types, Bike, Frame, Wheel, ElectricBike

front_wheel = Wheel(28,)
back_wheel = Wheel(28,)
frame = Frame(19, 'red', 'sport')

bike = Bike('red', bike_types['cross'], front_wheel, back_wheel, frame)
print(bike)
bike.ride()
bike.dzwonek()

electric_bike = ElectricBike('red', bike_types['cross'], front_wheel, back_wheel, frame)
electric_bike.motor_power_increase

new_employee = Employee('Mateusz', 'Cebula', 3000)
new_employee.increase_salary(30)
new_employee.chceck_salary()

