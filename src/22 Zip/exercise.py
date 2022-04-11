first_names = ["Albert", "Isaac"]
last_names = ["Einstein", "Newton"]

for physicist in zip(first_names, last_names):
    print(f"Hi! I'm {physicist[0]} {physicist[1]}.")
