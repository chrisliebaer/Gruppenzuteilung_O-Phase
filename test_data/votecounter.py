import sys
import json

# read "first argument as json"
if len(sys.argv) > 1:
	with open(sys.argv[1], 'r', encoding='utf-8') as file:
		json_data = file.read()

	data = json.loads(json_data)
		

	group_votes = {}

	# init for all groups with 0 votes on all places
	for id, group in data["groups"].items():
		group_votes[id] = [0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0]

	# loop over ratings, and resolve and add them
	for id, ratings in data["ratings"].items():
		team = data["teams"][id]
		member_count = len(team)

		for group_id, score in ratings.items():
			group_votes[group_id][score] += member_count


	# some groups appear multiple times, with spaces, keep track what we already printed
	printed_groups = []

	# sanity check (add all first places)
	total_votes = 0

	# print the result
	for group_id, votes in group_votes.items():
		name = data["groups"][group_id]["name"].strip()

		if name in printed_groups:
			continue
		
		total_votes += votes[0]

		print(name + ":")
		for i, vote_count in enumerate(votes):
			if vote_count > 0:
				place = i + 1
				print("\t" + str(place) + ": " + str(vote_count))
		print("")
		printed_groups.append(name)
		
	print("Total votes: " + str(total_votes))
	

else:
	print("No argument provided")
