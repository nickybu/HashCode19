from .model import Image

def parse_dataset(filename):
    if filename == "a_example.txt":
        return [
            Image("H", ["cat", "beach", "sun"]),
            Image("V", ["selfie", "smile"]),
            Image("V", ["garden", "selfie"]),
            Image("H", ["garden", "cat"])
        ]
    else:
        raise ValueError("I only support a_example.txt right now")

