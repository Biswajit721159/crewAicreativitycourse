from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
from djangobackend.Function import FunctionForSubject


async def TestToGiveChatgpt(result):
    try:
        question = [{"role": "user", "content": result}]
        api_key = os.getenv("OPENAI_API_KEY")
        client = OpenAI(
            api_key=api_key,
        )
        response = client.chat.completions.create(
            model="gpt-4",
            messages=question,
            functions=FunctionForSubject,
            function_call="auto",
        )
        responseMessage = response.choices[0].message
        if responseMessage.function_call == None:
            content = responseMessage.content
            content = json.loads(content)
            content = content["Subjects"]
            return content
        functionArgs = json.loads(responseMessage.function_call.arguments)
        return functionArgs["Subjects"]
    except Exception as error:
        print("Error is ", error)
        return [
            "Your maximum context is reached or your query is invalid. Please refresh this page and write your query again."
        ]
