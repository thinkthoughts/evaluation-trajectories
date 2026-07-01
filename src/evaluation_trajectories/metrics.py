from .trajectory import EvaluationTrajectory

def trajectory_reliability_score(trajectory: EvaluationTrajectory) -> float:
    """Compute a simple first-pass reliability score from process steps."""
    if not trajectory.steps:
        return 0.0
    base = trajectory.final_score()
    failure_penalty = len(trajectory.failure_points()) / len(trajectory.steps)
    return max(0.0, min(1.0, base * (1.0 - 0.5 * failure_penalty)))

def regression_delta(current: float, baseline: float) -> float:
    return current - baseline
