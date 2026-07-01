from .datasets import load_toy_trajectories
from .metrics import trajectory_reliability_score

def evaluate_toy_runs() -> list[dict]:
    rows = []
    for traj in load_toy_trajectories():
        rows.append({
            "run_id": traj.run_id,
            "model_id": traj.model_id,
            "task_id": traj.task_id,
            "final_score": traj.final_score(),
            "reliability": trajectory_reliability_score(traj),
            "failure_count": len(traj.failure_points()),
        })
    return rows
