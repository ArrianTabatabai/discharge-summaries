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
                "low_cpu_mem_usage": True,
            },
            device_map="auto",
        )

        # Initialize the document with a limit of 50 tokens for faster testing
        self.init_text = open("prompts/init_prompt", "r").read()

        init_dict = [{
            "role": "system",
            "content": self.init_text
        },
        {
            "role": "user",
            "content": "Who are you and what do you do"
        }]

        # Limiting to 50 tokens
        i = self.pipeline(
            init_dict,
            max_new_tokens=50  # Limit tokens for faster processing
        )
        print(i)

    def summarize(self, text):

        prompt_initializer = "Summarize the following documents into a complete discharge summary:"

        full_prompt = prompt_initializer + text

        # Limiting to 50 tokens for testing
        x = self.pipeline(
            full_prompt,
            max_new_tokens=50,  # Limit tokens for faster processing
            temperature=0.001,
            top_p=1
        )

        print(x)
        return x


class Dataset():

    def __init__(self, dataset_id):
        self.dataset_id = dataset_id
        self.data = load_dataset(self.dataset_id)


if __name__ == "__main__":
    trainer = ModelTrainer()
    test_summary = open(r"C:\Users\rajib\Documents\GitHub\discharge-summaries\Example Training\2 (Single File Format)\input", "r").read()
    out = trainer.summarize(text=test_summary)

    # Access the generated text from the output
    out = out[0]["generated_text"]
    open("output.txt", "w").write(out)

    while True:
        text = input("Enter documents: ")
        out = trainer.summarize(text=text)