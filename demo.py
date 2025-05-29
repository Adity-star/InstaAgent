# some_agent_task.py

from InstaAgent.exception import AgentException
import sys

def run_agent_task():
    try:
        # Example: Simulating a failure
        result = 1 / 0
    except Exception as e:
        raise AgentException(e, sys)
