import os
import openai

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def mount_messages(new_message):
    return [
        {"role": "user", "content": new_message},
    ]


def extract_openia_response(response):
    returned_response = response['choices'][0]['message']['content']
    return returned_response


def get_ia_response(new_message):
    messages = mount_messages(new_message)

    response = openai.ChatCompletion.create(
        temperature=0.7,
        messages=messages,
        model="gpt-3.5-turbo",
    )

    response = extract_openia_response(response)

    return response
