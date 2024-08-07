# Import necessary libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the text data from a file
file_path = "bee.txt"  # Update this with your text file's path

# Read the contents of the text file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Create a WordCloud object
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='turbo', # prism, viridis, brg, turbo, terrain, gnuplot2
    collocations=False,  # Avoid displaying collocations (bigrams)
).generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axes
plt.show()
