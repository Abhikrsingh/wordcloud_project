

# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


#Below is the second shell to upload the .txt file full with only text.while running second shell code a Brower button will created where you have to select the file that only contain the text for the same i have uploaded abhishek.txt file.


def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


#Below is the impotant coding part means logic on the code after writing the below code run it.


def calculate_frequencies(file_contents):
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the","for", "a", "to", "if", "is","not","on", "it", "of", "and", "or", "an", "as","in", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","than"]
    new_content = ""
    frequencies = {}
    for ch in file_contents:
        if ch not in punctuations:
            new_content += ch
    temp_file = new_content.split(" ")
    while "" in temp_file:
        temp_file.remove("")
    for word in temp_file:
        if word.lower() not in uninteresting_words:
            if word in frequencies:
                frequencies[word] +=1
            else:
                frequencies[word] = 1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


#Below is the last shell of the code to display the image.


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# If your word cloud image did not appear, go back and rework your `calculate_frequencies` function until you get the desired output.  Definitely check that you passed your frequecy count dictionary into the `generate_from_frequencies` function of `wordcloud`. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!
