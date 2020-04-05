def main():
    import json
    import random
    with open("/Users/truemac/Desktop/menu/menu.json", 'r') as f:
        data = json.load(f)
    print("Meat dish today", random.choice(list(data["meat"])))
    print("Vegetable dish today", random.choice(list(data["veg"])))
    print("Soup dish today", random.choice(list(data["soup"])))
main()
