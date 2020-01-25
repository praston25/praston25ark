import sys
import json
import io
hobbies = "Coding, Oprek Android, Oprek Windows, Game"
hobbies_list  = hobbies.split(",")

x = {
  "name": "Prasetyo Sukmo Pawenang",
  "age": 20,
  "adress": "Bugel, RT 003 / RW 002, Kel Bugel, Kec Sidorejo, Kota Salatiga",
  "hobbies": hobbies_list,
  "is_married": False,
  "list_school": {
      "name": "SMA Negeri 1 Salatiga",
      "year_in": "2015",
      "year_out": "2017",
      "major": "IPA",
      },
  "skills": {
       "skill_name" : "Web Development",
       "level"      : "Beginer",
       },
  "interest_in_coding" : True
}

y = json.dumps(x)
print(y)

with open('data.json', 'w') as f:
  json.dump(x, f, ensure_ascii=False)
