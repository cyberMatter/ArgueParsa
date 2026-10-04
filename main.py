from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from evaluator.parser import CREICEvaluator
from evaluator.metrics import depth_recommendation

console = Console()


def run_cli() -> None:
    console.print(
        Panel.fit(
            "[bold blue]C-R-E-I-C Argument Evaluator[/bold blue]\n"
            "Paste your argument below to check its structure and logic depth."
        )
    )

    argument = input("\nEnter argument text: ")
    if not argument.strip():
        console.print("[red]Error: argument text cannot be empty.[/red]")
        return

    evaluator = CREICEvaluator(argument)
    results = evaluator.detect_creic_components()

    table = Table(title="Evaluation Breakdown")
    table.add_column("Component", style="cyan", no_wrap=True)
    table.add_column("Status / Score", style="magenta")

    for key, value in results.items():
        if key == "Sufficient Depth":
            continue
        table.add_row(key, str(value))

    console.print("\n", table)

    causal_count = evaluator.analyze_reasoning_depth()["causal_links_found"]
    console.print(f"\n{depth_recommendation(causal_count)}")


if __name__ == "__main__":
    run_cli()
