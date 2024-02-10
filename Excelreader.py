import pandas as pd

# Function to read test data from Excel file
def read_test_data(file_path, sheet_name):
    try:
        # Read Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Convert DataFrame to list of dictionaries
        test_data = df.to_dict(orient='records')
        return test_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
