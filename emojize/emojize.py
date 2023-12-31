import emoji

text = input("Input: ").split(":")
emoji_requested = text.strip(":")
emoji.emojize(f"{text})
