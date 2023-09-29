import os
import google.generativeai as palm

# palm.configure(api_key=os.environ.get('API_KEY'))
palm.configure(api_key="AIzaSyDp5fkGPgw8VeKa5oN_AJqM7MezZOg8VR4")

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
def getAbstractSummary(rawtext,size):
    rawtext += "\n Summarize the above for a "+int(size)*2+" mark question"
    completion = palm.generate_text(
        model=model,
        prompt=rawtext,
        temperature=0,
        max_output_tokens=800,
    )
    print(completion.result)
    return completion.result