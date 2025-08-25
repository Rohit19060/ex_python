import pandas as pd

# Load the Excel file
file_path = 'roaster.xlsx'  # Update this with your file path
sheet_name = 'Sheet1'  # Update this with your sheet name if necessary
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Define the table and column names
table_name = 'users'
columns = [
    'id', 'name', 'image', 'role', 'email', 'password', 'addr', 'mobile', 'link', 
    'company', 'pt_id', 'cat_id', 'cap_id', 'chap_des', 'usp', 'branches', 'exp', 
    'dream_r', 'com_brief', 'email_verified_at', 'status', 'remember_token', 
    'created_at', 'updated_at'
]

# Generate the INSERT INTO statement
insert_query = f"INSERT INTO `{table_name}` ({', '.join([f'`{col}`' for col in columns])}) VALUES\n"

# Iterate through each row and format the values into the SQL query
values = []
for index, row in df.iterrows():
    # Format each value, handling NULLs and escaping strings
    formatted_values = []
    for col in columns:
        value = row[col]
        if pd.isna(value):  # Check for NaN values and convert them to NULL
            formatted_values.append('NULL')
        elif isinstance(value, str):
            formatted_values.append(f"'{value.replace("'", "''")}'")  # Escape single quotes in strings
        else:
            formatted_values.append(str(value))
    values.append(f"({', '.join(formatted_values)})")

# Combine all values into the final query
insert_query += ",\n".join(values) + ";"

# Output the query
print(insert_query)
