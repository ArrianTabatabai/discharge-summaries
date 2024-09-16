import transformers
import torch
from transformers import AutoTokenizer



class alpha():
    def __init__(self,
                 model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"): # Had to use 8B as opposed to 70B because of gpu memory limit cri

        self.model_id = model_id
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_id,
            model_kwargs={
                "torch_dtype": torch.float32,
                "quantization_config" : {"load_in_4bit":True}, #tag these out once on server, only for test env
                "low_cpu_mem_usage": True,
            },

        )

        x = self.pipeline("hey how are you")
        print(x)

        self.message_history = [] #This will be a list of messages

        self.terminators = [
            self.pipeline.tokenizer.eos_token_id,
            self.pipeline.tokenizer.convert_tokens_to_ids(""),
        ]


        return

    def set_message_history(self, msg):

        self.message_history += [msg]

        return
    @staticmethod
    def generate_dict_message(role,msg):
        return {"role": role, "content":msg}

    def gen_response(self,
                     query,
                     max_tokens=1024,#Max tokens to generate
                     temperature = 0.1, ##Temperature is a float value defining the amount of randomness 1 being most random, and 0 being shifted to the most likely logit,
                     top_p = 0.9 #Another prob var, if set below 1 then the smallest # of most probable tokens that add up to top_p are kept - try changing for different results
    ):

        self.set_message_history(query)

        #prompt = self.pipeline.tokenizer.apply_chat_template(self.message_history,tokenizer=False, add_generation_prompt=True)

        self.pipeline(
            query,
            max_new_tokens = max_tokens,
            #eos_token_id = self.terminators,
            #do_sample = True, ##True, this parameter enables decoding strategies such as multinomial sampling, beam-search multinomial sampling, Top-K sampling and Top-p sampling. All these strategies select the next token from the probability distribution over the entire vocabulary with various strategy-specific adjustments.
            temperature = temperature,
            top_p = top_p
        )

        return

    def test_response(self):
        self.gen_response(query="hello")

        return


if __name__ == "__main__":
    torch.cuda.empty_cache()
    a = alpha()
    a.test_response()

