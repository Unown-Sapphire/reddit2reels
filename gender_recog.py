import spacy

nlp = spacy.load("en_core_web_sm")
characters_to_remove = ",-'.?!()[]{}@#$%^&*" 
translator = str.maketrans("", "", characters_to_remove)

with open("randompost.txt", "r", encoding="utf-8") as f:
    text = f.readlines(-1)

for word in text:
    translated_text = word.translate(translator)

    text_list = []
    pos_list = []
    shape_list = []

    doc = nlp(translated_text)
    for token in doc:
        text_list.append(token.text)
        pos_list.append(token.pos_)
        shape_list.append(token.shape_)

    for i, s in enumerate(shape_list):
        if s in ["ddX", "ddx", "dx", "dX"]:
            # Female
            if i > 0 and text_list[i-1].lower() in ["my", "me", "i", "i'm"]:
                print(text_list[i-1])
                print("> Author located! The author is female!")
                gender = "f"
            else:
                print(text_list[i-1] if i > 0 else "N/A")
                print("Not the author")
        elif s in ["dd", "d"]:
            # Male
            if i > 0 and text_list[i-1].lower() in ["my", "me", "i", "i'm"]:
                print(text_list[i-1])
                print("> Author located! The author is male!")
                gender = "m"
            else:
                print(text_list[i-1] if i > 0 else "N/A")
                print("Not the author")
        elif s in ["Xdd", "xdd", "xd", "Xd"]:
            for x, y in enumerate(text_list):
                if i == x:
                    for q in y:
                        if q in ["F", "f"]:
                            print("Female Located")
                            while i <= len(shape_list):
                                if text_list[i-1].lower() in ["my", "me", "i", "m"]:
                                    print("Author Located")
                                    gender = "f"
                                    break
                                elif text_list[i-2].lower() in ["my", "me", "i", "m"]:
                                    print("Author located")
                                    gender = "f"
                                    break
                                else:
                                    break
                        elif q in ["M", "m"]:
                            print("Male Located")
                            while i <= len(shape_list):
                                if text_list[i-1].lower() in ["my", "me", "i", "m"]:
                                    print("Author Located")
                                    gender = "m"
                                    break
                                elif text_list[i-2].lower() in ["my", "me", "i", "m"]:
                                    print("Author located")
                                    gender = "m"
                                    break
                                else:
                                    print("Author NF")
                                    gender = 'nb'
                                    break
                        else:
                            pass
        else:
            gender = "nb"