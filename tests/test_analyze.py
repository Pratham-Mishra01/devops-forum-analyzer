# Unit test: we are testing if the compute_statistics function gives the correct results
import sys
import os

# Add project root folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from analyzer.analyze import compute_statistics

def test_compute_statistics():
    # sample data
    sample_questions=[
         {
            "score": 4,
            "answer_count": 2,
            "is_answered": True,
            "tags": ["docker"]
        },

        {
            "score": 6,
            "answer_count": 0,
            "is_answered": False,
            "tags": ["kubernetes"]
        }
    ]

    # running the function from analyze.py

    result=compute_statistics(sample_questions)

    # throw an AssertionError if the "==" is not satisfied
    assert result["average_score"] == 5.0
    assert result["average_answer_count"] == 1.0
    assert result["resolved_percentage"] == 50.0