import instructor
from openai import OpenAI
from datetime import datetime
from .schemas import QueryPlan
from .prompts import SYSTEM_PROMPT

class QueryInterpreter:
    def __init__(self, api_key: str):
        self.client = instructor.patch(OpenAI(api_key=api_key))
        
    def parse_request(self, user_input: str) -> QueryPlan:
        """
        Processes raw text and returns a QueryPlan object.
        """
        return self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            response_model=QueryPlan,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT.format(
                    current_date=datetime.now().strftime("%Y-%m-%d")
                )},
                {"role": "user", "content": user_input}
            ]
        )