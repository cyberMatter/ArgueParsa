"""Component detection for the C-R-E-I-C framework.

This uses simple keyword heuristics, not a language model — it is meant
as a fast first-pass check while you're drafting, not a final judge.
"""

import re

from .metrics import count_causal_links, has_sufficient_depth

EXAMPLE_KEYWORDS = ["for instance", "for example", "e.g.", "such as", "case study", "in practice"]
IMPACT_KEYWORDS = ["impact", "harm", "benefit", "affected", "disproportionately", "vulnerable", "severity"]
COMPARISON_KEYWORDS = ["outweighs", "compared to", "rather than", "versus", "whereas", "more important than", "prioritize"]


class CREICEvaluator:
    """Evaluates a single drafted argument against the C-R-E-I-C structure."""

    def __init__(self, argument_text: str):
        self.text = argument_text.strip()
        self.sentences = [s.strip() for s in re.split(r"[.!?]+", self.text) if s.strip()]

    def analyze_reasoning_depth(self) -> dict:
        """Returns the causal link count and whether it meets the depth bar."""
        causal_count = count_causal_links(self.text)
        return {
            "causal_links_found": causal_count,
            "has_sufficient_depth": has_sufficient_depth(causal_count),
        }

    def detect_creic_components(self) -> dict:
        """Heuristically checks for each C-R-E-I-C component and returns a report."""
        lower_text = self.text.lower()

        has_claim = len(self.sentences) > 0
        has_example = any(kw in lower_text for kw in EXAMPLE_KEYWORDS)
        has_impact = any(kw in lower_text for kw in IMPACT_KEYWORDS)
        has_comparison = any(kw in lower_text for kw in COMPARISON_KEYWORDS)

        reasoning = self.analyze_reasoning_depth()

        return {
            "Claim": "Detected" if has_claim else "Missing",
            "Reasoning Depth": f"{reasoning['causal_links_found']} causal links (Target: 3+)",
            "Example": "Detected" if has_example else "Missing",
            "Impact": "Detected" if has_impact else "Missing",
            "Comparison": "Detected" if has_comparison else "Missing",
            "Sufficient Depth": reasoning["has_sufficient_depth"],
        }
