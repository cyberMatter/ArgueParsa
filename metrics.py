"""Scoring helpers for the C-R-E-I-C evaluator.

Keeps the "how do we measure depth" logic separate from the
"how do we detect components" logic in parser.py.
"""

CAUSAL_KEYWORDS = [
    "because",
    "leads to",
    "forces",
    "results in",
    "therefore",
    "consequently",
    "this means",
    "as a result",
    "due to",
    "incentivizes",
]

MIN_CAUSAL_LINKS_FOR_DEPTH = 3


def count_causal_links(text: str) -> int:
    """Count occurrences of causal-chain language in the argument text."""
    lower_text = text.lower()
    return sum(lower_text.count(keyword) for keyword in CAUSAL_KEYWORDS)


def has_sufficient_depth(causal_link_count: int) -> bool:
    """An argument needs at least MIN_CAUSAL_LINKS_FOR_DEPTH causal links
    to count as having real mechanism depth, rather than a single
    unsupported assertion.
    """
    return causal_link_count >= MIN_CAUSAL_LINKS_FOR_DEPTH


def depth_recommendation(causal_link_count: int) -> str:
    """Return a plain-language note on what to fix, if anything."""
    if has_sufficient_depth(causal_link_count):
        return "Strong logic depth detected. Solid use of causal linkages."

    missing = MIN_CAUSAL_LINKS_FOR_DEPTH - causal_link_count
    return (
        f"Your argument lacks depth. Add at least {missing} more "
        "layer(s) of 'because' or explicit causal chains "
        "(e.g., 'X causes Y, which incentivizes Z')."
    )
