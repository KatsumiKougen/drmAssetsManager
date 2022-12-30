import json, os

if __name__ == "__main__":
    with os.scandir("/home/katsumi/drmAssetsManager/assets") as cwd:
        for category in cwd:
            print(category.path)
            keys = ["["]
            with os.scandir(category.path) as dir_:
                for entry in dir_:
                    entryname = entry.name
                    entrycat = entryname.split("-")[:-1]
                    entrycat = ", ".join([i.center(len(i)+2, "\"") for i in entrycat])
                    entryid = entryname.split("-")[-1].split(".")[0]
                    entrypath = entry.path
                    
                    key = f"    {{\n        \"asset_name\": \"{entryname}\",\n        \"asset_path\": \"{entrypath}\",\n        \"id\": {entryid},\n        \"category\": [\n            {entrycat}\n        ],\n        \"attributes\": {{\n            \"characters\": [\n                null\n            ],\n            \"details\": [\n                null\n            ]\n        }}\n    }},"
                    print(key)
                    keys.append(key)
            keys[-1] = keys[-1][:-1]
            keys.append("]")
            with open(f"descriptor-{category.name}.json", "w") as f:
                f.write("\n".join(keys))
