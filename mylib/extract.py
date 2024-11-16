import requests
import os

def extract(
    url="https://raw.githubusercontent.com/nogibjj/Mu-Niu-Pandas-Descriptive-Statistics-Script/main/student_performance.csv",
    file_path="data/student_performance.csv",
):
    """Extract a URL to a file path"""
    try:
        # Debug: Starting extraction
        print(f"Starting extraction from: {url}")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        print(f"Directory ensured: {os.path.dirname(file_path)}")

        # Perform the request
        response = requests.get(url)
        if response.status_code == 200:  # Check if the request was successful
            print(f"HTTP request successful. Status code: {response.status_code}")

            # Write content to file
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"File successfully saved to: {file_path}")
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    except Exception as e:
        # Print any errors that occur
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    extract()
