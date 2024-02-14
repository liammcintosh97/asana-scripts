import asana
import json
import sys
import csv

# FUNCTIONS #
def getTeams():
  return client.teams.get_teams_for_organization(workspace)

def getTeamProjects(gid):
  return client.projects.get_projects({'workspace': workspace, 'team': gid}, opt_pretty=True)


if len(sys.argv) == 1:
  print("no arguments")
  sys.exit()

toFind = sys.argv[1]
propertyName = sys.argv[2]
outputFileName = sys.argv[3]


venuesFile = open("venues.json")
output = open(outputFileName,'w')
writer = csv.writer(output)
venues = json.load(venuesFile)
workspace = "996763182203"


client = asana.Client.access_token("")

for team in list(getTeams()):
  for venue in venues:
    if team['name'] == venue:
      for project in list(getTeamProjects(team["gid"])):
        if project['name'] == toFind:
          row = [venue,"\"" + propertyName + "\":" + "\"" + project["gid"] + "\""]
          writer.writerow(row)

venuesFile.close()
output.close()
