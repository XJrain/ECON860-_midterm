import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize the target URL
URL = "http://www.charcoalpaper.com/exams/github/user/dataset"

# Make a GET request to the target URL
response = requests.get(URL)

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Attempt to find the 'GitHub Data' heading on the webpage
heading = soup.find('h1', string='GitHub Data')
if not heading:
    raise ValueError("Could not find the 'GitHub Data' heading on the webpage.")

# Get all sibling div elements of the heading
main_data_rows = heading.find_next_siblings('div')

# Initialize an empty list to store extracted data
data = []


def extract_data_from_row(row_div):

    # Find all div elements inside the current row
    data_divs = row_div.find_all('div')

    # If the row doesn't contain the expected number of data points, return None
    if not data_divs or len(data_divs) < 4:
        return None

    # Attempt to extract the login_id from the ghid attribute
    login_div = data_divs[0]
    ghid = login_div.get('ghid')
    if ghid:
        # If ghid attribute exists, extract the login_id from it
        login_id = ghid.split('--')[-1].strip()
    else:
        # Otherwise, get the text content of the div
        login_id = login_div.text.strip()

    # Return None if the row contains headers
    if login_id == "Login ID":
        return None

    # Extract remaining data points
    repo_count = int(data_divs[1].text.strip())
    follower_count = int(data_divs[2].text.replace('*', '').strip())
    member_since = data_divs[3].text.split('(')[-1].replace(')', '').strip()

    return [login_id, repo_count, follower_count, member_since]


# Loop through each row div and extract data
for row_div in main_data_rows:
    extracted_data = extract_data_from_row(row_div)
    if extracted_data:
        login_id, repo_count, follower_count, member_since = extracted_data

        if follower_count < 0 or member_since == "0000-00-00":
            continue

        data.append(extracted_data)

# Convert the data list to a DataFrame
df = pd.DataFrame(data, columns=["Login ID", "Repo Count", "Follower Count", "Member Since"])

# Remove duplicates and rows with invalid Login ID
df.drop_duplicates(subset="Login ID", inplace=True)
df = df[df["Login ID"].notna() & (df["Login ID"] != "")]

# Save the DataFrame to a CSV file
df.to_csv("github_users.csv", index=False)

# Part 2

#Import the time module
import time

with open('token.txt', 'r') as f:
    TOKEN = f.read().strip()

API_URL = "https://api.github.com/users/"
login_ids = df["Login ID"].tolist()

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

data = []
failed_logins = []

print("Starting data fetching from GitHub API")
for login_id in login_ids:
    response = requests.get(API_URL + login_id, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data for {login_id}. Status code: {response.status_code}")
        failed_logins.append(login_id)
        continue

    user_data = response.json()
    avatar_url = user_data.get('avatar_url', '')
    url = user_data.get('url', '')
    following = user_data.get('following', '')
    starred_response = requests.get(API_URL + login_id + '/starred', headers=headers)
    starred_count = len(starred_response.json())
    full_name = user_data.get('name', '')
    company = user_data.get('company', '')
    blog = user_data.get('blog', '')
    location = user_data.get('location', '')
    email = user_data.get('email', '')
    hireable = user_data.get('hireable', '')
    bio = user_data.get('bio', '')
    created_at = user_data.get('created_at', '')
    updated_at = user_data.get('updated_at', '')
    data.append([login_id, avatar_url, url, following, starred_count, full_name, company, blog, location, email, hireable, bio, created_at, updated_at])

# Filter out the failed logins from the original DataFrame
df = df[~df["Login ID"].isin(failed_logins)]

# Overwrite the original CSV file with the updated DataFrame
df.to_csv("github_users.csv", index=False)

time.sleep(1)

columns = ["Login ID", "Avatar URL", "URL", "Following", "Starred Count", "Full Name", "Company", "Blog", "Location", "Email", "Hireable", "Bio", "Created At", "Updated At"]
df_results = pd.DataFrame(data, columns=columns)
df_results.to_csv("github_user_details.csv", index=False)

