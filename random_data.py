import random
"""
randomly select name, phone, address, and email address
"""

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main st.', 'High ave.', 'Pearl road', 'Maple blvd.', 'Park st.', 'Oak vis.', 'Pine st.', 'Cedar ave.', 'Elm rd.', 'Washington blvd.', 'Lake st.', 'Hill lane']

random_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnyvale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

email_domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'gov.ca', 'star.io', 'like.we', 'algo.io', 'ai.io']

for num in range(100):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    phone_number = f'{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}'
    street_num = random.randint(100, 999)
    street_name = random.choice(street_names)
    city = random.choice(random_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    domain = random.choice(email_domain)
    email = f"{first_name}.{last_name}@{domain}"

    print(f'{first_name} {last_name}\n{phone_number}\n{street_num} {street_name}\n{city}, {state} {zip_code}\n{email}\n')
