import json
import random

courses = json.loads( open("courses.json").read() )

cut_offs = {}

for i in courses:
  cut_offs[i] = random.randint(160,301)

file = open("cut_off_scores.json","w")
file.write(json.dumps(cut_offs))
file.close()
