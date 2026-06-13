from config import KEYWORDS

def is_match(job):

    text = (
        job.get("title", "") + " " +
        job.get("company", "")
    ).lower()

    return any(
        keyword.lower() in text
        for keyword in KEYWORDS
    )