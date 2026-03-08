import json
from collections import Counter
import os


def load_questions(file_path):
    """
    Load questions from the JSON file.
    Handles file errors safely.
    """

    try:
        with open(file_path, "r") as f:
            questions = json.load(f)

        return questions

    except FileNotFoundError:
        print("ERROR: questions.json not found. Run fetch_data.py first.")
        return []

    except json.JSONDecodeError:
        print("ERROR: questions.json is corrupted or invalid JSON.")
        return []


def compute_statistics(questions):
    """
    Compute engagement statistics from the dataset.
    """

    total_questions = len(questions)

    # Prevent division errors
    if total_questions == 0:
        return None

    total_score = 0
    total_answers = 0
    answered_count = 0
    total_views = 0
    accepted_count = 0
    highest_views = 0
    most_viewed_question = ""
    top_reputation = 0

    # This list will contain every tag from every question
    all_tags = []

    for q in questions:

        # Accumulate scores
        total_score += q.get("score", 0)

        # Accumulate answers
        total_answers += q.get("answer_count", 0)

        # Count resolved questions
        if q.get("is_answered"):
            answered_count += 1

        # Collect tags
        tags = q.get("tags", [])
        all_tags.extend(tags)

        # Add total views
        total_views += q.get("view_count", 0)

        # Count accepted answers
        if q.get("accepted_answer_id"):
            accepted_count += 1

        # Track most viewed question
        if q.get("view_count", 0) > highest_views:
            highest_views = q["view_count"]
            most_viewed_question = q["title"]

        # Track highest contributor reputation
        if q.get("owner_reputation", 0) > top_reputation:
            top_reputation = q["owner_reputation"]

    # Remove the forced "devops" tag since every question contains it
    filtered_tags = [tag for tag in all_tags if tag != "devops"]

    # Count tag frequency
    tag_counter = Counter(filtered_tags)

    # Get top 10 tags
    top_tags = tag_counter.most_common(10)

    # Compute averages
    avg_score = total_score / total_questions
    avg_answers = total_answers / total_questions
    resolved_percentage = (answered_count / total_questions) * 100
    avg_views = total_views / total_questions
    accepted_rate = (accepted_count / total_questions) * 100

    category_map = {
    "docker": "Containers",
    "kubernetes": "Containers",
    "azure": "Cloud",
    "amazon-web-services": "Cloud",
    "azure-devops": "CI/CD",
    "cicd": "CI/CD",
    "continuous-integration": "CI/CD"
    }

    category_counter = Counter()

    for tag in filtered_tags:
        if tag in category_map:
            category_counter[category_map[tag]] += 1

    dominant_category = category_counter.most_common(1)[0][0] if category_counter else "Unknown"

    # Round values for cleaner dashboard display
    results = {
       
    "total_questions": total_questions,

    "top_tags": top_tags,

    "average_score": round(avg_score, 2),

    "average_answer_count": round(avg_answers, 2),

    "resolved_percentage": round(resolved_percentage, 2),

    "average_views": round(avg_views, 2),

    "highest_view_count": highest_views,

    "accepted_resolution_rate": round(accepted_rate, 2),

    "top_contributor_reputation": top_reputation,

    "most_viewed_question": most_viewed_question,

    "dominant_category": dominant_category

    }

    return results


def save_results(results, output_path):
    """
    Save the analysis results to a JSON file.
    """

    os.makedirs("data", exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Analysis saved to {output_path}")


def analyze_questions():
    """
    Main pipeline function.
    """

    print("Starting DevOps forum analysis...")

    questions = load_questions("data/questions.json")

    if not questions:
        return

    results = compute_statistics(questions)

    if results:
        save_results(results, "data/analysis.json")

    print("Analysis completed successfully.")


# Standard Python entry point
# Ensures this script only runs when executed directly
if __name__ == "__main__":
    analyze_questions()