def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = func(*args, **kwargs)

        print("Function completed")
        return result

    return wrapper


@log_function
def add_traffic_data(vehicle_number, speed):
    return f"{vehicle_number} is moving at {speed} km/h"


print(add_traffic_data("MH12AB1234", 60))
print()

print(add_traffic_data(vehicle_number="MH14CD5678", speed=45))