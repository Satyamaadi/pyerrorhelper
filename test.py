from pyerrorhelper import ErrorManager

if __name__ == "__main__":
    error_manager = ErrorManager()
    error_manager.install()

def cause_error():
    return 1 / 0  # This will raise a ZeroDivisionError

cause_error()