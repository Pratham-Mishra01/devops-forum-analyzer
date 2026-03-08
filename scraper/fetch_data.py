import requests #interactions of python with internet
import json
import os   #interacts with computers folders

def fetch_devops_questions():
    print("Fetching DevOps questions from Stack Overflow...")

    url = "https://api.stackexchange.com/2.3/questions"     # Public API to fetch "questions"

    params = {                  # Query params sent to API (attached to URL)
        "order": "desc",
        "sort": "activity",
        "tagged": "devops",
        "site": "stackoverflow",
        "pagesize": 50
    }

    response = requests.get(url, params=params)     # HTTP GET request
    data = response.json()      # Server responds with JSON

    questions = []
    for item in data["items"]:      # picking only what we need.
        questions.append({
            "title": item["title"],     # can be used for keyword analysis
            "tags": item["tags"],       #trending devops topics
            "score": item["score"],     # no. of upvotes
            "answer_count": item["answer_count"],       # no of people that answered
            "is_answered": item["is_answered"],         # True/False
            "link": item["link"],        # link to the actual question

            "view_count": item["view_count"],
            # Unix creation timestamp
            "creation_date": item["creation_date"],

            # Latest activity timestamp
            "last_activity_date": item["last_activity_date"],

            # Accepted answer presence (None if absent)
            "accepted_answer_id": item.get("accepted_answer_id"),

            # Reputation of question author
            "owner_reputation": item.get("owner", {}).get("reputation", 0)

        })

    os.makedirs("data", exist_ok=True)
    with open("data/questions.json", "w") as f:
        json.dump(questions, f, indent=2)

    print(f"Done! Saved {len(questions)} questions to data/questions.json")

fetch_devops_questions()