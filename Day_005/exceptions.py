# Custom exceptions for Traffic Data Validator


class InvalidVehicleNumberError(Exception):
    """Raised when vehicle number is empty or invalid."""
    pass


class InvalidVehicleTypeError(Exception):
    """Raised when vehicle type is not supported."""
    pass


class InvalidSpeedError(Exception):
    """Raised when vehicle speed is negative."""
    pass