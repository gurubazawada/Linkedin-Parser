import csv

# Open the input CSV file in read mode
with open('links.csv', mode='r') as input_file:
    # Create a CSV reader object to read the input file
    reader = csv.reader(input_file)

    # Create a list to hold the rows of the output CSV file
    output_rows = []

    # Loop through each row in the input CSV file
    for row in reader:
        # Extract the first name and last initial from the name column
        name_parts = row[0].split()
        first_name = name_parts[0]
        last_initial = name_parts[-1][0]

        # Create the email address in the format of firstname.lastinitial@spotify.com
        email = f'{first_name.lower()}{last_initial.lower()}@spotify.com'

        # Append the row with the new email column to the output rows list
        row.append(email)
        output_rows.append(row)

# Open the output CSV file in write mode and write the output rows
with open('emails.csv', mode='w') as output_file:
    # Create a CSV writer object to write the output rows
    writer = csv.writer(output_file)

    # Loop through the output rows and write each row to the output CSV file
    for row in output_rows:
        writer.writerow(row)