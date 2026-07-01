from evaluation_trajectories.evaluation import evaluate_toy_runs
from evaluation_trajectories.reports import write_markdown_report

if __name__ == "__main__":
    write_markdown_report(evaluate_toy_runs(), "results/reports/toy_report.md")
