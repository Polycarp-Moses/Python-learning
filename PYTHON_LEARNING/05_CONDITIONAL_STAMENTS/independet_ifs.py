#Independent ifs
#each if is checked separately
#All conditions are tested- even if one is already True

score = 90
submitted_project = False

if score >= 90:
    print("High score")
else:
    print("Low score")

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")