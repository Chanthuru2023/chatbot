from flask import Flask, request, jsonify
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = Flask(__name__)

# Load the model and tokenizer
model_path = 'C:\\Users\\USER\\Downloads\\fine_tuned_gpt2-20240807T143039Z-001\\fine_tuned_gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Ensure the model is on the correct device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    input_text = data.get("input_text", "")

    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    output_ids = model.generate(
        inputs.input_ids,
        max_length=100,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.9,
        temperature=0.7
    )
    response_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
