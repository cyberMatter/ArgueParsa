# C-R-E-I-C Argument Evaluator

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

Automated structural parser for British Parliamentary debate. Checks speech drafts against the C-R-E-I-C framework (Claim, Reason, Example, Impact, Comparison), flags skipped logic, and enforces 3+ layers of causal depth before you speak.

## Why

Competitive debaters rarely lose a round because an idea was wrong — they lose because the idea was never finished. A claim with no mechanism. An impact with no comparison. A chain of reasoning that stops one "because" too early. This tool is a fast first-pass check for that: paste in a drafted argument, and it tells you which of the five C-R-E-I-C components are present, and whether your reasoning actually has depth or just length.

It is not a model of what makes an argument *good* — it's a heuristic keyword scanner, and it says so (see [Limitations](#limitations)). Treat it as a pre-flight checklist, not a judge.

## Features

- **Causal depth check** — scans for linkage language (`because`, `leads to`, `forces`, `incentivizes`, `therefore`, ...) and flags any argument with fewer than 3 causal links as under-developed.
- **Component detection** — heuristically checks for a Claim, Reason, Example, Impact, and Comparison across the submitted text.
- **Plain-language feedback** — tells you exactly what's missing and how many more reasoning steps to add, not just a pass/fail.
- **Clean terminal output** — a color-coded breakdown table via [`rich`](https://github.com/Textualize/rich).

## Example

```
$ python main.py

╭───────────────────────────────────────────────────────────────────╮
│ C-R-E-I-C Argument Evaluator                                      │
│ Paste your argument below to check its structure and logic depth. │
╰───────────────────────────────────────────────────────────────────╯

Enter argument text: Private healthcare should be banned because it
drains doctors from the public system, which forces understaffing...

              Evaluation Breakdown
┌─────────────────┬─────────────────────────────┐
│ Component       │ Status / Score              │
├─────────────────┼─────────────────────────────┤
│ Claim            │ Detected                    │
│ Reasoning Depth  │ 3 causal links (Target: 3+) │
│ Example          │ Detected                    │
│ Impact           │ Detected                    │
│ Comparison       │ Detected                    │
└─────────────────┴─────────────────────────────┘

Strong logic depth detected. Solid use of causal linkages.
```

## Quick start

Requires Python 3.8 or later.

```bash
git clone https://github.com/YOUR-USERNAME/creic-evaluator.git
cd creic-evaluator
pip install -r requirements.txt
python main.py
```

## Project structure

```
creic-evaluator/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── main.py                 # CLI entry point
└── evaluator/
    ├── __init__.py
    ├── parser.py            # component detection (Claim/Example/Impact/Comparison)
    └── metrics.py           # causal-depth scoring and recommendations
```

## Limitations

This is keyword-based, not semantic — it won't catch a well-reasoned argument that avoids its trigger words, and it can be fooled by an argument that uses the right words without the right logic behind them. It's built to catch the most common failure mode in debate prep (stopping too early), not to replace a coach's ear.

## Roadmap

- [ ] Streamlit web UI for live prep-time use
- [ ] Dependency-tree parsing (spaCy) instead of keyword matching, for genuine clause-level detection
- [ ] Exportable PDF breakdown for team debriefs

## Contributing

Issues and pull requests are welcome — this started as a personal debate-prep tool, so feedback from other debaters on what's actually useful in round is especially valuable.

## License

MIT — see [LICENSE](LICENSE).
