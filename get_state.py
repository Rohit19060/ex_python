import pandas as pd

file_path = "venues_phunnel.xlsx"
output_file_path = "unique_venues.xlsx"  # Output file for unique rows

# Load the data from the specified Excel sheet
data = pd.read_excel(file_path, sheet_name="venues_phunnel")

if "STATE" in data.columns and "CITY" in data.columns and "COUNTRYCODE" in data.columns:
    # Create a set to store unique city-country pairs globally
    unique_city_country = set()

    # Create a list to store unique rows
    unique_rows = []

    # Loop through each row in the DataFrame
    for index, row in data.iterrows():
        state = str(row["STATE"]).strip() if pd.notna(row["STATE"]) else ""
        city = str(row["CITY"]).strip() if pd.notna(row["CITY"]) else ""
        country = (
            str(row["COUNTRYCODE"]).strip() if pd.notna(row["COUNTRYCODE"]) else ""
        )

        if state == "":
            continue

        # Create a tuple for the city-country pair
        city_country_tuple = (city, country)

        # Only add the row if the city-country pair is not already in the set
        if city_country_tuple not in unique_city_country:
            unique_city_country.add(city_country_tuple)
            unique_rows.append((state, city, country))

    # Create a new DataFrame from the unique rows
    unique_data = pd.DataFrame(unique_rows, columns=["State", "City", "Country"])

    # Save the new DataFrame to an Excel file
    unique_data.to_excel(output_file_path, index=False)

    print(f"Unique data saved to {output_file_path}.")
else:
    print(
        "The DataFrame does not contain the required 'STATE', 'CITY', or 'COUNTRYCODE' columns."
    )
