from together import Together

client = Together()

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[],
    max_tokens=512,
    temperature=0.7,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1,
    stop=["<|eot_id|>","<|eom_id|>"], image_urls=["s3://together-ai-uploaded-user-images-prod/6c8ef3aa-df91-4681-a48f-325dfe658fbe.png"],
    stream=True
)
for token in response:
    if hasattr(token, 'choices'):
        print(token.choices[0].delta.content, end='', flush=True)
