import openai

class AI():

    API_TOKEN = "API TOKEN" # <--- insert API TOKEN here

    def __init__(self):
        self.dialog = [{"role":"system", "content":"Chat User"}]
        self.ai_outputs = []
        self.max_messages = 25 # max number of "remembered" messages (increasing number might increase token costs)

    def askGPT(self, prompt):
        openai.api_key = self.API_TOKEN

        self.dialog.append({"role":"user", "content":f"{prompt}"})
        
        result = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.dialog,
            max_tokens=150
        )

        output = result.choices[0].message['content']
        self.dialog.append({"role":"assistant", "content":output})
        self.ai_outputs.append(output)

        if len(self.dialog) > self.max_messages:
            excess_length = len(self.dialog) - self.max_messages
            self.dialog = self.dialog[excess_length:]

        return output

gpt = AI()