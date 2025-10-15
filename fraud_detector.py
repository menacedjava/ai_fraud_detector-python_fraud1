# AI Fraud Detection (basic skeleton)
import random

def detect(transaction):
    risk = random.random()
    return "FRAUD" if risk > 0.8 else "OK"

if __name__ == "__main__":
    for i in range(5):
        print(f"Txn {i+1}:", detect({"amount": random.randint(10, 5000)}))
