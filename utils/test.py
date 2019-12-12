import json
for line in open("/data/split_opencorpus/1.json"):
  if len(line.strip()) == 0:
    continue
  a = json.loads(line)
  print(a)

