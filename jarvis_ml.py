import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class JarvisML:
    def __init__(self):
        # Load pre-trained GPT-2 model and tokenizer
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def generate_response(self, input_text, max_length=100):
        # Tokenize the input text
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt")

        # Generate response using the GPT-2 model
        output = self.model.generate(input_ids, max_length=max_length, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

        # Decode the generated response
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

# Example usage
jarvis_ml = JarvisML()

while True:
    user_input = input("You: ")
    
    # Check for exit condition
    if user_input.lower() == "exit":
        break

    # Generate and print Jarvis's response
    jarvis_response = jarvis_ml.generate_response(user_input)
    print("Jarvis:", jarvis_response)
