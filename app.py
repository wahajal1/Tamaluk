import chainlit as cl
from transformers import pipeline

# نجهز الموديل
chatbot = pipeline("text-generation", model="gpt2")

@cl.on_message
async def main(message: str):
    # نرسل رسالة للموديل
    response = chatbot(message, max_new_tokens=50, do_sample=True, temperature=0.7)
    reply = response[0]["generated_text"][len(message):].strip()

    # نرجع الرد للواجهة
    await cl.Message(content=reply).send()