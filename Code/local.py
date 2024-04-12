import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'Local', 'ohio-2022-primary-election.csv')
election_data = pd.read_csv(file_path)

cityNames = []
for index, row in election_data.iterrows():
    if row['Media Market'] not in cityNames:
        cityNames.append(row['Media Market'])

finalData = []
for city in cityNames:
    registeredVotersSum = election_data[election_data['Media Market'] == city]['Registered Voters'].sum()
    totalVotesSum = election_data[election_data['Media Market'] == city]['Total Ballots Cast'].sum()
    democraticVotesSum = election_data[election_data['Media Market'] == city]['Democratic Ballots Cast'].sum()
    republicanVotesSum = election_data[election_data['Media Market'] == city]['Republican Ballots Cast'].sum()

    data = {
        'city': city,
        'registered_voters': registeredVotersSum,
        'total_votes': totalVotesSum,
        'democratic_votes': democraticVotesSum,
        'republican_votes': republicanVotesSum,
        'democratic_percent': f"{(democraticVotesSum / totalVotesSum) * 100} %",
        'republican_percent': f"{(republicanVotesSum / totalVotesSum) * 100} %",
        'voter_turnout': f"{(totalVotesSum / registeredVotersSum) * 100} %"
    }
    finalData.append(data)

print(finalData)

###########################################################################################################################################

from openai import OpenAI

client = OpenAI(api_key="")

prompt = f'Given the following data on the 2022 Ohio Primary Election give 3 insights you can gather: "{finalData}"'
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Use GPT-3.5
    messages=[
        {"role": "system", "content": prompt}
    ],
    temperature=1,  # Set temperature to 0 for deterministic output
)
insights = response.choices[0].message.content

print(insights)