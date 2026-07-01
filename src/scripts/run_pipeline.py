from pathlib import Path
import json
from evaluation_trajectories.evaluation import evaluate_toy_runs
from evaluation_trajectories.visualization import plot_scores
from evaluation_trajectories.reports import write_markdown_report

def main() -> None:
    root = Path(__file__).resolve().parents[2]
    rows = evaluate_toy_runs()
    metrics_path = root / "results" / "metrics" / "toy_metrics.json"
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(json.dumps(rows, indent=2))
    plot_scores(rows, root / "results" / "figures" / "toy_scores.png")
    write_markdown_report(rows, root / "results" / "reports" / "toy_report.md")
    print(f"Wrote {metrics_path}")

if __name__ == "__main__":
    main()
