import gradio as gr

def greet(name):
    return "Hello " + name + "!!"

gr.Interface(fn=greet, inputs="text", outputs="text").launch()
