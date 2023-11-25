import json

analytical_program= "input.json"
def task() -> float:
    with open(analytical_program) as f:
        data = json.load(f)
        list_values = [item["score"] * item["weight"] for item in data]
        return round(sum(list_values), 3)
        
print(task())
