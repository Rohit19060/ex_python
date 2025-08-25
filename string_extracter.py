import re


def extract_magnet_links(file_path):
    # Define a regular expression pattern to match the string starting with 'magnet' and ending with '"'
    pattern = r'magnet:\?xt[^"]*"'

    # Read the file content
    with open(file_path, "r") as file:
        content = file.read()

    # Find all matches based on the pattern
    magnet_links = re.findall(pattern, content)

    # Clean up the results by removing the trailing quote
    magnet_links = [link.rstrip('"') for link in magnet_links]

    return magnet_links


# Example usage:
file_path = "input.txt"  # Replace with the path to your file
magnet_links = extract_magnet_links(file_path)

# Print the extracted links
for link in magnet_links:
    print(link)
