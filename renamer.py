#!/usr/bin/env python3

import os

def Assets():
    assets = os.listdir()
    for i in assets:
        if "pic" not in i:
            assets.remove(i)
    return assets

currentid = int(open("./currentid", "r").read())
target = open("./target", "r").read()[:-1].split()
template = "others-%.png"

print(
    f"Current directory: {os.getcwd()}\n"
    f"Current ID is {currentid}"
)

if len(target) > 0:
    print("The following files will be renamed:")
    for i in target:
        print(f"pic{i}.png", end=" ")
    confirm = input(f"\nusing the template \"{template}\"\nDo you wish to continue? (Y to confirm) ")
    if confirm.lower() == "y":
        for i in target:
            os.rename(f"pic{i}.png", template.replace("%", f"{currentid:010}"))
            currentid += 1
        with open("./currentid", "w") as f:
            f.write(str(currentid))
        print(f"All {len(target)} files have been renamed.")
    else:
        print("Operation cancelled.")
else:
    print("Error: No target file.")
