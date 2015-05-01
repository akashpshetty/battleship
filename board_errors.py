class InvalidPlacementError(Exception):
    def __init__(self, message, error_code):
        # Call the base class constructor with the parameters it needs
        super(InvalidPlacementError, self).__init__(message)
        self.error_code = error_code


class InvalidDirectionError(InvalidPlacementError):
    message = "Invalid direction"
    error_code = 1

    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super(InvalidDirectionError, self).__init__(self.message, self.error_code)


class InvalidStartPositionError(InvalidPlacementError):
    message = "Initial position outside the board"
    error_code = 2

    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super(InvalidStartPositionError, self).__init__(self.message, self.error_code)
