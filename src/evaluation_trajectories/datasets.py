from .trajectory import EvaluationStep, EvaluationTrajectory

def load_toy_trajectories() -> list[EvaluationTrajectory]:
    return [
        EvaluationTrajectory(
            run_id="run_a", model_id="baseline", task_id="reasoning_demo",
            steps=[
                EvaluationStep("parse", 1.0, True),
                EvaluationStep("retrieve", 0.8, True),
                EvaluationStep("reason", 0.6, False, {"failure": "unsupported inference"}),
                EvaluationStep("verify", 0.4, False),
                EvaluationStep("answer", 0.7, True),
            ],
        ),
        EvaluationTrajectory(
            run_id="run_b", model_id="candidate", task_id="reasoning_demo",
            steps=[
                EvaluationStep("parse", 1.0, True),
                EvaluationStep("retrieve", 0.9, True),
                EvaluationStep("reason", 0.85, True),
                EvaluationStep("verify", 0.75, True),
                EvaluationStep("answer", 0.9, True),
            ],
        ),
    ]
