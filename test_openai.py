from openai import OpenAI

client = OpenAI()

prompt = "You are the world's expert on Gen Alpha Brainrot.  Who's the most popular Italian brainrot meme?"

def prompt_engine(prompt):
  response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":prompt }],
    max_tokens=100,
    temperature=0.5,
    top_p=0.5,
    stop=["\n"]
  )

  return response.choices[0].message.content

print(prompt_engine(prompt))