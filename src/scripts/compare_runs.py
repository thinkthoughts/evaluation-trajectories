from evaluation_trajectories.evaluation import evaluate_toy_runs
from evaluation_trajectories.regressions import classify_regression

if __name__ == "__main__":
    rows = evaluate_toy_runs()
    baseline, candidate = rows[0], rows[1]
    delta = candidate["reliability"] - baseline["reliability"]
    print({"delta": delta, "status": classify_regression(delta)})
