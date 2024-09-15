import transformers
import torch
from transformers import AutoTokenizer


class alpha():
    def __init__(self,
                 model_id="meta-llama/Meta-Llama-3.1-8B-Instruct"):  # Using 8B due to GPU memory limit

        self.model_id = model_id
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_id,
            model_kwargs={
                "torch_dtype": torch.float32,
                #"quantization_config": {"load_in_4bit": True},  # Uncomment if needed for test env
                "low_cpu_mem_usage": True,
            },
        )

        # Limiting to 50 tokens for testing purposes
        x = self.pipeline("hey how are you", max_new_tokens=50)
        print(x)

        self.message_history = []  # This will be a list of messages

        self.terminators = [
            self.pipeline.tokenizer.eos_token_id,
            self.pipeline.tokenizer.convert_tokens_to_ids(""),
        ]

    def set_message_history(self, msg):
        self.message_history += [msg]

    @staticmethod
    def generate_dict_message(role, msg):
        return {"role": role, "content": msg}

    def gen_response(self,
                     query,
                     max_tokens=50,  # Limiting to 50 tokens for faster processing
                     temperature=0.1,  # Low temperature for less randomness
                     top_p=0.9):  # Keeping top-p sampling

        self.set_message_history(query)

        self.pipeline(
            query,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )

    def test_response(self):
        self.gen_response(query="hello")


if __name__ == "__main__":
    torch.cuda.empty_cache()
    a = alpha()
    a.test_response()