import csv

# Define the mapping between the input and output columns
mapping = {
    'username': 'username',
    'user_email': 'user_email',
    'user_login': 'user_login',
    'Email': 'email',
    'firstname': 'first_name',
    'Lastname': 'last_name',
    'ur_form_id': 'ur_form_id',
    'ur_user_status': 'ur_user_status',
    'Registration type': 'user_registration_select_1678973765',
    'street': 'billing_address_1',
    'city': 'billing_city',
    'zip': 'billing_postcode',
    'state': 'billing_state',
    'expiry': 'expiry',
    'phone': 'user_registration_input_box_1680744695',
    'type': 'type',
    'user_registration_input_box_1680744374': 'user_registration_input_box_1680744374', # street
    'user_registration_input_box_1680744514': 'user_registration_input_box_1680744514', # city
    'user_registration_input_box_1680744592': 'user_registration_input_box_1680744592', # zip
    'user_registration_input_box_1680744537': 'user_registration_input_box_1680744537', # state
    'user_registration_country_1680744618': 'user_registration_country_1680744618'

}

ignored = [
  'Username',
  'user_login',
  'user_email',
  'username',
  'ur_form_id',
  'ur_user_status',
  'type',
  'user_registration_input_box_1680744374',
  'user_registration_input_box_1680744514',
  'user_registration_input_box_1680744592',
  'user_registration_input_box_1680744537',
  'user_registration_country_1680744618'
]

# Open the input and output CSV files
with open('/Users/michelleliu/67373/master.csv', 'r') as input_file, open('/Users/michelleliu/67373/target.csv', 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    print(mapping.values())
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=(mapping.values()))
    
    existing_users = {}

    # Write the header row to the output file
    writer.writeheader()
    
    # Iterate over each row in the input file and map the columns to the output file
    for row in reader:
        if row['Email'] == '' or row['Email'] in existing_users:
            continue
        mapped_row = {}
        existing_users[row['Email']] = True
        mapped_row['username'] = row['Email']
        mapped_row['user_login'] = row['Email']
        mapped_row['user_email'] = row['Email']
        mapped_row['username'] = row['Email']
        mapped_row['ur_form_id'] = '2171'
        mapped_row['ur_user_status'] = '1'
        mapped_row['type'] = 'legacy'
        mapped_row['user_registration_input_box_1680744374'] = row['street']
        mapped_row['user_registration_input_box_1680744514'] = row['city']
        mapped_row['user_registration_input_box_1680744592'] = row['zip']
        mapped_row['user_registration_input_box_1680744537'] = row['state']
        mapped_row['user_registration_country_1680744618'] = 'US'

        for input_col, output_col in mapping.items():
            if input_col not in ignored:
              mapped_row[output_col] = row[input_col]
        writer.writerow(mapped_row)
