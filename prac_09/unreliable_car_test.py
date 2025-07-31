from prac_09.unreliable_car import UnreliableCar

test_taxi = UnreliableCar("Prius 1", 100, 1.23, 30)

test_time = 100
drive_time = 0
for i in range(test_time):
    distance_driven = test_taxi.drive(100)
    if distance_driven > 0:
        drive_time += 1

print(drive_time)