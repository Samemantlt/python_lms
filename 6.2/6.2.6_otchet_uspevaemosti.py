def best(data):
    return data[data["maths"] >= 4][data["physics"] >= 4][data["computer science"] >= 4]
