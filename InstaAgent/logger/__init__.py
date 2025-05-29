import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
def from_root():
    # Returns the root directory of the project (where this file's parent is)
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Constants
LOG_DIR = "logs"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Number of rotated logs to keep
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FILE_TIMESTAMP = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# Ensure log directory exists
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)

# Helper to get log file path
def get_log_file_path(filename_prefix: str = "app", use_timestamp: bool = True) -> str:
    filename = (
        f"{filename_prefix}_{LOG_FILE_TIMESTAMP}.log" if use_timestamp else f"{filename_prefix}.log"
    )
    return os.path.join(log_dir_path, filename)

# Optional colored formatter (simple version)
class ColorFormatter(logging.Formatter):
    COLOR_MAP = {
        logging.DEBUG: "\033[94m",    # Blue
        logging.INFO: "\033[92m",     # Green
        logging.WARNING: "\033[93m",  # Yellow
        logging.ERROR: "\033[91m",    # Red
        logging.CRITICAL: "\033[95m", # Magenta
    }
    RESET = "\033[0m"

    def format(self, record):
        log_fmt = f"[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(log_fmt, datefmt=LOG_DATE_FORMAT)
        color = self.COLOR_MAP.get(record.levelno, self.RESET)
        return color + formatter.format(record) + self.RESET

def configure_logger(
    logger_name: str = "",
    level: int = None,
    log_filename: str = None,
    console_level: int = logging.INFO,
    use_color: bool = True
) -> logging.Logger:
    """
    Configures and returns a logger with both file and console handlers.

    Args:
        logger_name (str): The name of the logger.
        level (int): Overall logging level. If None, defaults to DEBUG.
        log_filename (str): Full path to log file.
        console_level (int): Logging level for console.
        use_color (bool): Whether to use colored logs in console.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(logger_name)
    if logger.handlers:
        return logger  # Prevent duplication

    level = level or logging.DEBUG
    logger.setLevel(level)

    # File Formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s", datefmt=LOG_DATE_FORMAT)

    # File Handler
    if not log_filename:
        log_filename = get_log_file_path()
    file_handler = RotatingFileHandler(log_filename, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    # Console Handler
    console_handler = logging.StreamHandler()
    if use_color:
        console_handler.setFormatter(ColorFormatter())
    else:
        console_handler.setFormatter(formatter)
    console_handler.setLevel(console_level)
    logger.addHandler(console_handler)

    return logger

# Usage
logger = configure_logger()
logger.info("Logger is configured and enhanced.")
