import gradio as gr

def tensorboard():
  with gr.Row():
    gr.Markdown("## Tensorboard")
  with gr.Row():
    gr.HTML(
      """<iframe width="100%" 
                    height="700" 
                    src="http://localhost:6006" 
                    title="Tensordboard" 
                    frameborder="0" 
                    allowfullscreen>
                </iframe>
                """,
                label="Tensorboard",
                show_label=True
                ) 
