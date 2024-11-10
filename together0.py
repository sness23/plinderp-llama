from together import Together

client = Together()

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[
        {
                "role": "user",
                "content": [
                        {
                                "type": "text",
                                "text": "test"
                        }
                ]
        }
],
    max_tokens=null,
    temperature=0.7,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1,
    stop=["<|eot_id|>","<|eom_id|>"],
    update_at="2024-11-10T13:03:34.885Z",
    stream=True
)
for token in response:
    if hasattr(token, 'choices'):
        print(token.choices[0].delta.content, end='', flush=True)

