from subreddit import random_title

import tts_audio

import string

timing_list = []

new_list = []

def location():
    location = new_list.index(element)
    print("Located: " + element)
    timing = new_list[location-1]
    timing_list.append(timing)
    del new_list[0:location+1]
with open(file="spedup.srt", mode="r+", encoding="utf-8") as file:
    file_line = file.readlines(-1)
    for line in file_line:
        x = line.rstrip("\n")
        new_list.append(x)
    new_list = [i for i in new_list if i != '']
    characters_to_remove = ",-'"
    for element in new_list:

        #translate the element/title to make sure there are no unessecary punctuations
        translator = str.maketrans("", "", characters_to_remove)
        translated_title = random_title.translate(translator)
        translated_element = element.translate(translator)

        #Check for punctuation
        if element.endswith(".") and random_title.lower().endswith(element.rstrip(".")):
            location()
            break
        elif element.endswith("?") and random_title.lower().endswith(element):
            location()
            break
        elif element.endswith(".") and random_title.lower().endswith(element):
            location()
            break
        elif translated_title.lower().endswith(element):
            location()
            break
        elif random_title.lower().endswith(translated_element):
            location()
            break
        else:
            pass

    writing_list = []
    for z in new_list:
        spaced_element = z + "\n"
        writing_list.append(spaced_element)
    if len(writing_list) % 3 == 0:
        number_of_occurences = int(len(writing_list)/3)
    else:
        pass
    a = 3
    n = 0 
    while n < number_of_occurences:
        writing_list.insert(a, "\n")
        a+=4
        n+=1    

    file.truncate(0)
    file.seek(0)
    for line in writing_list:
        file.write(line)
print(translated_title)
    

#conditions:
    #The SRT ends with "." but random title doesn't (done)
    #The SRT and title end with "." (done)
    #The SRT and title end with "?" (done)
    #if SRT and title last punctuation doesnt match but word match (done)
    #SRT and title have the essential same word but the apostrophe or hyphens are non existent (done)
    #SRT has hyphens but title doesnt (to-do)