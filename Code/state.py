import pandas as pd
import os
import numpy as np

file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'State', 'Election', '1976-2020-senate.csv')
election_data = pd.read_csv(file_path)

election_data_simplified = []
election_years = [2000, 2004, 2008, 2012, 2016, 2020]

def get_totals_for_year(year, data):

    approxEligibleVotersByState = {
        "AL": 2528963,
        "AK": 473648,
        "AZ": 2173122,
        "AR": 1555809,
        "CA": 15707307,
        "CO": 2274152,
        "CT": 1874245,
        "DE": 505360,
        "District of Columbia": 354410,
        "FL": 8752717,
        "GA": 3859960,
        "HI": 637349,
        "ID": 728085,
        "IL": 7129026,
        "IN": 4000809,
        "IA": 1841346,
        "KS": 1623623,
        "KY": 2556815,
        "LA": 2730380,
        "ME": 882337,
        "MD": 2715366,
        "MA": 4008796,
        "MI": 6861342,
        "MN": 3265324,
        "MS": 1739858,
        "MO": 3860672,
        "MT": 698260,
        "NE": 1085217,
        "NV": 898347,
        "NH": 856519,
        "NJ": 4710768,
        "NM": 972895,
        "NY": 11262816,
        "NC": 5122123,
        "ND": 490198,
        "OH": 7537822,
        "OK": 2233602,
        "OR": 1943699,
        "PA": 7781997,
        "RI": 655107,
        "SC": 2157006,
        "SD": 471152,
        "TN": 3181108,
        "TX": 10267639,
        "UT": 1123238,
        "VT": 427354,
        "VA": 3770273,
        "WA": 3335714,
        "WV": 1067822,
        "WI": 4192515,
        "WY": 220012,
    }
    
    returnData = {}

    for index, row in election_data.iterrows():
        if row['year'] == year:
            currentState = row['state_po']
            totalVotes = row['totalvotes']

            turnoutRate = totalVotes / approxEligibleVotersByState[currentState]

            state_data = returnData.get(currentState, {'turnoutRate': 0, 'totalVotes': 0, 'partyPercentages': {}})

            state_data['turnoutRate'] = turnoutRate
            state_data['totalVotes'] = totalVotes

            party_votes = state_data['partyPercentages'].get(row['party_simplified'], 0)
            state_data['partyPercentages'][row['party_simplified']] = party_votes + row['candidatevotes'] / totalVotes

            returnData[currentState] = state_data

    return returnData

for year in election_years[0:1]:
    totals = get_totals_for_year(year, election_data)
    election_data_simplified.append(totals)

for i in election_data_simplified:
    for key, value in i.items():
        print(f"{key}: {value}")
        print('\n\n')
    print('\n\n')