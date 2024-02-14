import asana
import json
import sys

# FUNCTIONS #
def getTeams():
  return client.teams.get_teams_for_organization(workspace)

def getTeamProjects(gid):
  return client.projects.get_projects({'workspace': workspace, 'team': gid}, opt_pretty=True)

def duplicateProject(gid,name):
  toInclude = [
    "members"
  ]
  return client.projects.duplicate_project(gid, {'include': toInclude, 'name': name}, opt_pretty=True)

# FUNCTIONS #

if len(sys.argv) == 1:
  print("no arguments")
  sys.exit()

f = open("venues.json")
venues = json.load(f)

toCopy = sys.argv[1]
newName = sys.argv[2]
workspace = "996763182203"

client = asana.Client.access_token("")

for team in list(getTeams()):
  for venue in venues:
    if team['name'] == venue:
      for project in list(getTeamProjects(team["gid"])):
        if project['name'] == toCopy:
          duplicateProject(project["gid"],newName)


