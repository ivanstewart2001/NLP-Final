# Hypothesis: Voter turnout varies significantly between general elections and primary elections.
# Uses data in federal/presidential and federal/primary_election folders to test hypothesis.

import pandas as pd
import os
import numpy as np

file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'Federal', 'Presidential', '1976-2020-president.csv')
general_election_data = pd.read_csv(file_path)

def simplify_election_data(year, total_votes, party):
    simplified_data = {'year': year}

    total_votes_summed = sum(total_votes)
    simplified_data['total_votes'] = total_votes_summed

    approx_num_us_citizens = {
        2000: 210000000,
        2004: 215000000,
        2008: 225000000,
        2012: 235000000,
        2016: 245000000,
        2020: 255000000
    }

    simplified_data['voter_turnout'] = total_votes_summed / approx_num_us_citizens[year]

    data_year = general_election_data[general_election_data['year'] == year]
    party_data_grouped = data_year.groupby(['party_detailed'])['candidatevotes'].sum()
    top_parties = party_data_grouped.sort_values(ascending=False).head(5)

    for party, value in top_parties.items():
        simplified_data[f"{party}_percent"] = value / total_votes_summed

    return simplified_data

general_election_data_simplified = []
general_election_years = [2000, 2004, 2008, 2012, 2016, 2020]

def get_totals_for_year(year, data):
    total_votes_totals = []
    party_totals = []

    for index, row in general_election_data.iterrows():
        if row['year'] == year:
            total_votes_totals.append(row['candidatevotes'])
            party_totals.append(row['party_simplified'])

    return total_votes_totals, party_totals

for year in general_election_years:
    total_votes_totals, party_totals = get_totals_for_year(year, general_election_data)
    data = simplify_election_data(year, total_votes_totals, party_totals)
    general_election_data_simplified.append(data)

for i in general_election_data_simplified:
    print(i, '\n\n')

primary_election_file_names = os.listdir(os.path.join(os.path.dirname(__file__), '..', 'Data', 'Federal', 'Primary Election'))

primary_election_data_simplified = {}

def calculate_average_percentage(input_list):
    results = []
    
    for data in input_list:
        if type(data) == str and data != 'VEP Total Ballots Counted':
            value = float(data.split('%')[0])
            results.append(value)

    return np.mean(results)

for file_name in primary_election_file_names:
    file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'Federal', 'Primary Election', file_name)
    year = file_name.split(' ')[0]
    data = pd.read_csv(file_path)

    if '2000' in file_name or '2004' in file_name:
        primary_election_data_simplified[year] = calculate_average_percentage(data['VEP Turnout Rate'])
    else:
        primary_election_data_simplified[year] = calculate_average_percentage(data['Turnout Rate'])

print(primary_election_data_simplified)