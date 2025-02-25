import os
import random

emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def random_emotion():
    emotion = random.choice(emotions)
    return emotion
    
def select_picture(emotion):
    allImages = list()
    directory = "./emotions/" + emotion
    print(directory)
    for img in os.listdir(directory):
        allImages.append(img)
    random_index = random.randint(0, len(allImages) - 1)
    result = allImages[random_index]
    return result