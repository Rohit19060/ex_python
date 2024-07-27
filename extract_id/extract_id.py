import re

import chardet


# Function to extract text between square brackets from a string
def extract_bracketed_text(text):
    return re.findall(r"\[([^\]]*)\]", text)


# Detect encoding
with open("input.txt", "rb") as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result["encoding"]

# Read from the file with the detected encoding
with open("matches.txt", "w", encoding=encoding) as output_file:
    with open("input.txt", "r", encoding=encoding) as file:
        for line in file:
            matches = extract_bracketed_text(line)
            if matches:
                # Print matches found
                for match in matches:
                    print(f"Found: {match}")
                    output_file.write(f"{match}\n")
            else:
                # Print line if no matches are found
                print(f"No brackets: {line.strip()}")
