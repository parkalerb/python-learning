from exceptions import (
    InvalidVehicleNumberError,
    InvalidVehicleTypeError,
    InvalidSpeedError
)


VALID_VEHICLE_TYPES = ["Car", "Bike", "Bus", "Truck"]


def validate_vehicle_number(vehicle_number):
    if not vehicle_number.strip():
        raise InvalidVehicleNumberError(
            "Vehicle number cannot be empty."
        )


def validate_vehicle_type(vehicle_type):
    if vehicle_type not in VALID_VEHICLE_TYPES:
        raise InvalidVehicleTypeError(
            f"Invalid vehicle type: {vehicle_type}"
        )


def validate_speed(speed):
    if speed < 0:
        raise InvalidSpeedError(
            "Vehicle speed cannot be negative."
        )


def validate_traffic_data(vehicle_number, vehicle_type, speed):
    validate_vehicle_number(vehicle_number)
    validate_vehicle_type(vehicle_type)
    validate_speed(speed)


def main():
    print("🚦 Traffic Data Validator")
    print("-" * 30)

    try:
        vehicle_number = input("Enter vehicle number: ")
        vehicle_type = input("Enter vehicle type: ")
        speed = float(input("Enter vehicle speed: "))

        validate_traffic_data(
            vehicle_number,
            vehicle_type,
            speed
        )

    except InvalidVehicleNumberError as error:
        print(f"❌ Validation Error: {error}")

    except InvalidVehicleTypeError as error:
        print(f"❌ Validation Error: {error}")

    except InvalidSpeedError as error:
        print(f"❌ Validation Error: {error}")

    except ValueError:
        print("❌ Invalid speed. Please enter a number.")

    else:
        print("\n✅ Traffic data is valid!")
        print(f"Vehicle Number : {vehicle_number}")
        print(f"Vehicle Type   : {vehicle_type}")
        print(f"Speed          : {speed} km/h")

    finally:
        print("\n🔄 Validation process completed.")


if __name__ == "__main__":
    main()