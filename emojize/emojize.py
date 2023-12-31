import emoji
import requests

text = input("Input: ").split(":")
emoji_requested = text.strip(":")
emoji.emojize(f"{text})
