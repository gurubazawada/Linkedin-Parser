import csv
import os

# Path to the folder containing the HTML files
folder_path = "/Users/gurubazawada/Desktop/linkedin parser/pages"

# Get a list of all HTML files in the folder
file_names = [f for f in os.listdir(folder_path) if f.endswith(".html")]

# Text string to search for
search_text = 'class="visually-hidden"><!---->View'

# Open a CSV file in write mode and write the profile names to it
with open("names.csv", mode="w") as file:
    writer = csv.writer(file)
    writer.writerow(["Profile Name"])

    for file_name in file_names:
        with open(os.path.join(folder_path, file_name), "r") as f:
            html = f.read()
            index = html.find(search_text)
            while index != -1:
                start_index = index + len(search_text) + 1
                end_index = html.find("’s profile", start_index)
                if end_index != -1:
                    profile_name = html[start_index:end_index].strip()[:40]
                    writer.writerow([profile_name])
                index = html.find(search_text, end_index)