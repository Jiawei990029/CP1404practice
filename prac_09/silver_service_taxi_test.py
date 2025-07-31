from prac_09.silver_service_taxi import SilverServiceTaxi

test_taxi = SilverServiceTaxi("One", 200, 2)
test_taxi.start_fare()
test_taxi.drive(18)
print(test_taxi.get_fare())