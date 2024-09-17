##This file loads up the model and handles direct interactions with said model
import transformers
import torch
#from transformers import AutoTokenizer


class Interactor():
    def __init__(self, model_path):

        model_kwargs = { ##may change this for actual deployment depending on hardware
                "torch_dtype": torch.bfloat16,
                "quantization_config": {"load_in_4bit": True},  # tag these out once on server, only for test env
                "low_cpu_mem_usage": True,
            }

        self.pipeline = transformers.pipeline(
            "text-generation",
            model = model_path,
            model_kwargs=model_kwargs,
            device_map="auto"
        )

        self.promptInitializer = ("Summarize the following documents into a complete discharge summary:")

        #model loaded just awaiting instruction



    def send_prompt(self,
                    text,
                    role = "user"):

        prompt = [
            {
                "role":role,
                "content":text
            }
        ]

        max_tokens = 2048  # Max tokens to generate
        temperature = 0.001  ##Temperature is a float value defining the amount of randomness 1 being most random, and 0 being shifted to the most likely logit,
        top_p = 1  # Another prob var, if set below 1 then the smallest # of most probable tokens that add up to top_p are kept - try changing for different results

        raw_output = self.pipeline(
            prompt,
            max_new_tokens=max_tokens,
            temperature = temperature,
            top_p = top_p
        )

        formatted_output = raw_output[0]["generated_text"][1]["content"]

        return formatted_output

    def hello_world(self):

        x = self.send_prompt("Who are you and what do you do")
        print(x)
        return x

    def summarize(self, text): # text should be in correct format - formatter code will be made
        text = self.promptInitializer + text
        x = self.send_prompt(text)

        return x

if __name__ == "__main__":

    path = r""#ENTER PATH OF
    i = Interactor(path)
    i.hello_world()
