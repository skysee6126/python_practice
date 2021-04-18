import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"Math":20, "EN": 40, "Art": 100}
for sbj, score in scores.items():
  print(sbj.ljust(4), str(score).rjust(3), sep=":")

for num in range(1, 21):
  print(f"number list: {str(num).zfill(3)}")

# keep empty place as blank & text align right, total 10space
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:+,}".format(-500000))

#text align left and fill the blank as _
print("{0:_<+10}".format(500))

#float
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))

#file in/output
score_file = open("score.txt", "w", encoding="utf8")
print("Math : 0", file= score_file)
print("EN : 30", file= score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") #append
score_file.write("science : 50")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") #read
#print(score_file.read()) #ALL
#print(score_file.readline()) #line by line
while True:
  line = score_file.readline()
  if not line:
    break
  print(line)

# lines = score_file.readlines()
# for line in lines:
#   print(line)
score_file.close()


#pickle
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"name":"A", "age": 30, "lang": ["EN", "KR", "CN"]}
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb") #read
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

with open("profile_file", "rb") as profile_file:
  print(pickle.load(profile_file))

with open("study.txt", "w",) as study_file:
  study_file.write("Study hard")
  
with open("study.txt", "r",) as study_file:
  print(study_file.read())