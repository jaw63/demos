import random

# intialize k
k = 4

def train_model(text, k):
    model = {}
    for i in range(len(text) - k):
        seq = text[i:i+k]
        next_char = text[i+k]
        if seq not in model:
            model[seq] = {}
        if next_char not in model[seq]:
            model[seq][next_char] = 0
        model[seq][next_char] += 1
    return model

def generate_text(model, length=100):
    seed = random.choice(list(model.keys()))
    output = seed
    for i in range(length):
        if seed in model:
            next_char = random.choices(list(model[seed].keys()), weights=list(model[seed].values()))[0]
            output += next_char
            seed = output[-k:]
        else:
            seed = random.choice(list(model.keys()))
    return output

# Example usage

# Read in training text
file = open('bee.txt', 'r') 
text = file.read() 
file.close()

model = train_model(text,k)
output = generate_text(model, length=500)
print(output)
