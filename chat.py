import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Load model and intents
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_file:
    intents = json.load(json_file)

data = torch.load("data.pth")

model = NeuralNet(data["input_size"], data["hidden_size"], data["output_size"]).to(device)
model.load_state_dict(data["model_state"])
model.eval()

all_words = data['all_words']
tags = data['tags']

def get_response(user_input):
    # Tokenize the input message
    sentence = tokenize(user_input)
    # Bag of words representation
    X = bag_of_words(sentence, all_words)
    # Convert to tensor
    X = torch.tensor(X).unsqueeze(0)  # Add batch dimension

    # Predict the class (tag)
    output = model(X)
    print(output.shape)  # Add this line to check the shape of output

    # Get the class with the highest probability
    _, predicted = torch.max(output, dim=1)  # Make sure dim=1 is valid
    tag = tags[predicted.item()]

    # Get the response for the predicted tag
    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            break

    return response