import json

file_path = '../data/schacon.repos.json'
with open(file_path, 'r') as file: 
   data = json.load(file)

with open('chason.csv', 'w') as csv_file:
   for repo in data[:5]: 
      name = repo.get('name', '')
      html_url = repo.get('html_url', '')
      updated_at = repo.get('updated_at', '')
      visibility = repo.get('visibility', '')
      
      line = f"{name}, {html_url}, {updated_at}, {visibility}\n" 
      csv_file.write(line)

