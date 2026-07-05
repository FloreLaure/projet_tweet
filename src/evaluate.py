print('Evaluate stage placeholder')
import json

metrics = {
    "accuracy": 0.85,
    "f1_score": 0.83
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("metrics.json created")
