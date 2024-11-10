from together import Together
from plinderpdoibio import get_markdown

# docking results on page number 7 of the pdf
page_num = "7"
plinderp_file = get_pdf_base64('plinder', '1erm_' + page_num)

client = Together()

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[  {
                "role": "user",
                "content": [
                        {
                                "type": "text",
                                "text": "Please analyze this and make a report of the binding of the ligand to the target"
                        }
                ]
        }],
    max_tokens=null,
    temperature=0.7,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1,
    stop=["<|eot_id|>","<|eom_id|>"],
    image_base64=[plinderp_file],
    stream=True
)
for token in response:
    if hasattr(token, 'choices'):
        print(token.choices[0].delta.content, end='', flush=True)
