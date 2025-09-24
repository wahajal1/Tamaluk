import chainlit as cl
from transformers import pipeline

chatbot = None  # نخليها None بالبداية

@cl.on_message
async def main(message: str):
    global chatbot
    if chatbot is None:
        chatbot = pipeline("text-generation", model="distilgpt2")

    response = chatbot(message, max_new_tokens=50, do_sample=True, temperature=0.7)
    reply = response[0]["generated_text"]

    await cl.Message(content=reply).send()
