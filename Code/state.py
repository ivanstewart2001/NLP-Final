import pandas as pd
import os
import numpy as np

file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'State', 'Election', '1976-2020-senate.csv')
election_data = pd.read_csv(file_path)

election_data_simplified = []
election_years = [2000, 2004, 2008, 2012, 2016, 2020]

def get_totals_for_year(year, data):

    approxEligibleVotersByState = {
        "AL": 3826693,
        "AK": 531417,
        "AZ": 5358326,
        "AR": 2214758,
        "CA": 25986149,
        "CO": 4410916,
        "CT": 2656634,
        "DE": 774746,
        "District of Columbia": 510714,
        "FL": 16365830,
        "GA": 7734398,
        "HI": 1050763,
        "ID": 1421619,
        "IL": 9018008,
        "IN": 5050535,
        "IA": 2353889,
        "KS": 2113647,
        "KY": 3356052,
        "LA": 3336267,
        "ME": 1132456,
        "MD": 4396788,
        "MA": 5155024,
        "MI": 7627434,
        "MN": 4259705,
        "MS": 2175222,
        "MO": 4652414,
        "MT": 887675,
        "NE": 1417874,
        "NV": 2246393,
        "NH": 1121461,
        "NJ": 6459151,
        "NM": 1560752,
        "NY": 13930369,
        "NC": 8067643,
        "ND": 580564,
        "OH": 8936519,
        "OK": 2930170,
        "OR": 3181347,
        "PA": 9905729,
        "RI": 823712,
        "SC": 4101895,
        "SD": 679545,
        "TN": 5316827,
        "TX": 20021307,
        "UT": 2341476,
        "VT": 524649,
        "VA": 6367607,
        "WA": 5612884,
        "WV": 1387628,
        "WI": 4465647,
        "WY": 441700,
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

for year in election_years:
    totals = get_totals_for_year(year, election_data)
    election_data_simplified.append({'totals': totals, 'year': year})

print(election_data_simplified)