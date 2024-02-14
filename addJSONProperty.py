import json
import csv

output = open("output.csv",'w')
writer = csv.writer(output)

with open('input.csv') as file:
  reader = csv.reader(file)
  for row in reader:
    if len(row) > 0:
      data = json.loads(row[0])
      itenum = data["field_enum"]
      del data["field_enum"]
      data["field_enums"] = {
        "it": itenum,
        "finance": {
          "tgif": "",
          "tsg": ""
        }
      }
      row = [json.dumps(data,indent=4,sort_keys=False)]
      print(row)
      writer.writerow(row)

output.close()

