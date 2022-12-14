#!/usr/bin/env python3

import os

def Assets():
    assets = os.listdir()
    for i in assets:
        if "doremonche" not in i:
            assets.remove(i)
    return assets

currentid = int(open("./currentid", "r").read())
target = Assets()
template = "others-%.jpg"

print(
    f"Current directory: {os.getcwd()}\n"
    f"Current ID is {currentid}"
)

if len(target) > 0:
    print(f"The following {len(target)} files will be renamed:")
    for i in target:
        print(i, end=" ")
    confirm = input(f"\nusing the template \"{template}\"\nDo you wish to continue? (Y to confirm) ")
    if confirm.lower() == "y":
        for i in target:
            os.rename(f"{i}", template.replace("%", f"{currentid:010}"))
            currentid += 1
        with open("./currentid", "w") as f:
            f.write(str(currentid))
        print(f"All {len(target)} files have been renamed.")
    else:
        print("Operation cancelled.")
else:
    print("Error: No target file.")
