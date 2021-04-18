import pickle

for i in range(1, 11):
  with open(f"week {str(i)}.txt", "w",) as report_file:
    report_file.write(f"""
    - week {str(i)} weekly report -
  team:
  name:
  summary:
    """)
