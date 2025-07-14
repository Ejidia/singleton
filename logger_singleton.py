# logger_singleton.py
# Implements the Singleton Logger class

class LoggerSingleton:
    # Class-level variable to hold the single instance
    _instance = None

    def __new__(cls, logfile='app.log'):
        # If no instance exists, create one
        if cls._instance is None:
            print("Creating Logger instance")
            # Call the superclass __new__ to actually create the object
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
            # Set the log file name
            cls._instance.logfile = logfile
            # Open the log file for appending
            cls._instance._open_log()
        # If instance already exists, just return it
        return cls._instance

    def _open_log(self):
        # Open the log file in append mode
        self.log_file = open(self.logfile, 'a')

    def log(self, message):
        # Write the message to the log file and flush immediately
        self.log_file.write(message + '\n')
        self.log_file.flush()
        # Also print to the console for feedback
        print(f"LOGGED: {message}")

    def __del__(self):
        # Ensure the log file is closed when the logger is destroyed
        if hasattr(self, 'log_file'):
            self.log_file.close()
