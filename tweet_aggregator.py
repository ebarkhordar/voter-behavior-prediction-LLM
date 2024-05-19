import json
import os
from tqdm import tqdm
import pandas as pd

# Load the survey data
df_survey_data = pd.read_excel('dataset/survey_model_outputs_edited_filtered.xlsx')

# Initialize a dictionary to store the loaded data for all users
tweets_data = {}

# Directory where the tweet files are stored
directory = 'dataset/tweets/'

# Iterate over each row in the DataFrame with a progress bar
for index, row in tqdm(df_survey_data.iterrows(), total=len(df_survey_data), desc="Processing tweets"):
    # Generate the expected filename in lowercase
    expected_file_name = f"{row['id']}_{row['username'].lower()}.json"
    # List all files in the directory and convert them to lowercase to match
    files = {f.lower(): f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))}

    # Check if the expected filename is in the list of files (both in lowercase)
    if expected_file_name in files:
        # Find the original filename (with original case) that matches our expected filename
        original_file_name = files[expected_file_name]
        file_path = os.path.join(directory, original_file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                user_tweets = json.load(file)
                if row['username'] in tweets_data:
                    tweets_data[row['username']].extend(user_tweets)
                else:
                    tweets_data[row['username']] = user_tweets
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file: {file_path}")
    else:
        print(f"File not found: {os.path.join(directory, expected_file_name)}")

# Save the dictionary to a JSON file
with open('dataset/tweets.json', 'w', encoding='utf-8') as file:
    json.dump(tweets_data, file, ensure_ascii=False, indent=4)

print("Tweets data saved to 'tweets.json'")
