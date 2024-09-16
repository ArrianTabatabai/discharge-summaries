
import transformers
import torch
from transformers import AutoTokenizer
from datasets import load_dataset



class ModelTrainer():


    def __init__(self,
                 model_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
                 ):


        self.model_id = model_id
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_id,
            model_kwargs={
                "torch_dtype": torch.bfloat16,
                "quantization_config": {"load_in_4bit": True},  # tag these out once on server, only for test env
                "low_cpu_mem_usage": True,
            },
            device_map = "auto",

        )

        ##Init document

        self.init_text = open("prompts/init_prompt","r").read()

        #Implement tools for searching?

        init_dict = [{
            "role":"system",
            "content": self.init_text
        },
            {
                "role":"user",
                "content": "Who are you and what do you do"
            }]

        i= self.pipeline(
            init_dict,
            max_new_tokens = 512,
        )
        print(i)


        self.pipeline.save_pretrained(r"C:\Users\rajib\Documents\GitHub\discharge-summaries\saved_model")


        return

    def summarize(self,
                  text):

        promptInitializer = ("Summarize the following documents into a complete discharge summary:")

        text = promptInitializer + text

        prompt = [
            {
                "role": "user",
                "content": text
            }
        ]

        x = self.pipeline(
            prompt,
            max_new_tokens = 1024,
            temperature = 0.001,
            top_p = 1
        )


        print(x)


        return x



class Dataset():

    def __init__(self,
                 dataset_id):

        self.dataset_id = dataset_id
        self.data = load_dataset(self.dataset_id)


        return



if __name__ == "__main__":
    trainer = ModelTrainer()
    #testSummary = open(r"C:\Users\rajib\Documents\GitHub\discharge-summaries\Example Training\2 (Single File Format)\input","r").read()
    #out = trainer.summarize(
    #    text= testSummary
    #)
    #out = out[0]["generated_text"][1]["content"]
    #open("output.txt","w").write(out)




