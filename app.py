import gradio as gr
import os
import openai

openai.api_key = "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"

def answer_request(text):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": text}
      ]
    )

    return completion.choices[0].message.content

demo = gr.Interface(
    fn=answer_request, 
    inputs=gr.Textbox(label="Eingabe",lines=2, placeholder="Stell mir eine rechtliche Frage!"), 
    outputs=gr.Textbox(label="Antwort")
)

demo.launch(share=True) 