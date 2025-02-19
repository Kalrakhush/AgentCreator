import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = None, level: int = logging.INFO) -> logging.Logger:
    """
    Sets up a logger that writes to both the console and a rotating log file.
    The log file is stored in a 'logs' folder at the project root (outside of src).
    
    :param name: Name of the logger.
    :param log_file: Optional custom log file path. If not provided, defaults to 'logs/app.log' in the project root.
    :param level: Logging level.
    :return: Configured logger.
    """
    # Determine the log file path; default to a 'logs' folder in the current working directory (project root)
    if log_file is None:
        logs_dir = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        log_file = os.path.join(logs_dir, "app.log")

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Create a rotating file handler
    file_handler = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=2)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid adding duplicate handlers if logger already has them
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger
