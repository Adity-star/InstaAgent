# some_agent_task.py

from InstaAgent.services.gpt_service import get_gpt_response

def test_gpt():
    user_message = "Hi,are you available for makeup this weekand?"
    reply = get_gpt_response(user_message)
    print("Agent reply:", reply)

if __name__ == "__main__":
    test_gpt()

