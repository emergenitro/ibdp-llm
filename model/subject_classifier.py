# A trivial keyword-based classifier to demonstrate the concept of "only respond if relevant".
# You can extend this using a fine-tuned classifier or semantic similarity approach.

SUBJECT_KEYWORDS = {
    "mathematics_aa": [
        "integral",
        "derivative",
        "function",
        "algebra",
        "matrices",
        "vector",
        "math",
        "mathematics",
    ],
    "physics": [
        "force",
        "energy",
        "magnetic",
        "electric",
        "quantum",
        "physics",
    ],
    "chemistry": [
        "mole",
        "titration",
        "bonding",
        "chemistry",
        "organic",
        "acid",
        "base",
        "equilibrium",
    ],
    "biology": [
        "cell",
        "ecosystem",
        "photosynthesis",
        "enzyme",
        "biology",
        "genetics",
        "DNA",
        "bilayer",
    ],
    "computer_science": [
        "programming",
        "algorithm",
        "data structure",
        "computer science",
        "java",
        "python",
    ],
    "economics": [
        "supply",
        "demand",
        "macro",
        "micro",
        "trade",
        "economics",
        "inflation",
        "CPI",
    ],
    "english_lit": [
        "literary",
        "theme",
        "character",
        "language",
        "literature",
        "metaphor",
        "symbolism",
        "plot",
    ],
}


def subject_guard(user_query):
    """
    Checks if user_query contains any known keywords for the included subjects.
    If none are found, we say it's not relevant.
    """
    lower_query = user_query.lower()
    for subject, keywords in SUBJECT_KEYWORDS.items():
        for kw in keywords:
            if kw in lower_query:
                return True  # relevant
    return False  # we consider it not relevant if no match found
