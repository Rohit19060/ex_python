import csv
import json
import re

# Path to your CSV file
csv_file_path = "test.csv"  # Replace with your actual file path


# Function to clean up the JSON string
def clean_json_string(json_string):
    # Remove unwanted characters and fix quotes
    json_string = json_string.replace("\\", "")  # Remove backslashes

    # Add quotes around keys that are not quoted
    json_string = re.sub(r"(\w+):", r'"\1":', json_string)

    # Ensure string values are properly quoted
    json_string = re.sub(r':\s*([^"\s]+)([,}])', r': "\1"\2', json_string)

    return json_string.strip()  # Return cleaned string


# Function to extract the JSON from a single string (third column)
def extract_json_from_row(row):
    # Join the relevant parts of the row to form a single JSON string
    json_string = "".join(row[2:3])  # Join elements that form the JSON string
    return clean_json_string(json_string)  # Clean and return


# Function to extract data from CSV
def extract_data_from_csv(csv_file_path, delimiter=",", quotechar='"'):
    extracted_data = []

    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        # Specify the delimiter and quote character in the CSV reader
        reader = csv.reader(file, delimiter=delimiter, quotechar=quotechar)

        # Loop through rows and extract the relevant data
        for row in reader:
            print(f"Processing row: {row}")  # Debugging output
            if len(row) > 2:  # Ensure there are at least three columns
                try:
                    cleaned_json_string = extract_json_from_row(
                        row
                    )  # Clean the JSON string
                    print(
                        f"Cleaned JSON string: {cleaned_json_string}"
                    )  # Debugging output
                    json_data = json.loads(cleaned_json_string)  # Parse JSON
                    extracted_data.append(json_data)
                except json.JSONDecodeError as e:
                    print(
                        f"Error decoding JSON: {e} in row: {row}"
                    )  # Print error details
                    continue

    return extracted_data


# Extract and print the JSON data
extracted_json = extract_data_from_csv(csv_file_path, delimiter=",", quotechar='"')
print(json.dumps(extracted_json, indent=2))  # Pretty print the JSON output
