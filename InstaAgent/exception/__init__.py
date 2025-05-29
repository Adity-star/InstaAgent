# agent_exception.py

import sys
import traceback
import logging
from logger import logger  # Ensure the logger is imported from your logging setup

def get_agent_error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information specific to an agent, including file name,
    line number, and the error message, with a logger-aware structure.
    
    Args:
        error (Exception): The original exception object.
        error_detail (sys): The sys module for accessing traceback details.

    Returns:
        str: A formatted error message for logging and raising.
    """
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = (
            f"[AGENT EXCEPTION] Error occurred in script: [{file_name}] "
            f"at line number [{line_number}] — {str(error)}"
        )
    else:
        error_message = f"[AGENT EXCEPTION] {str(error)}"

    logger.error(error_message)
    return error_message


class AgentException(Exception):
    """
    Custom exception class specifically for agent-related errors.
    Captures traceback info and logs it with an agent context.
    """
    def __init__(self, error: Exception, error_detail: sys):
        self.error_message = get_agent_error_message_detail(error, error_detail)
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return self.error_message
