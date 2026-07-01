from dataclasses import dataclass, field
from typing import Any

@dataclass
class EvaluationStep:
    name: str
    score: float
    passed: bool
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class EvaluationTrajectory:
    run_id: str
    model_id: str
    task_id: str
    steps: list[EvaluationStep]

    def final_score(self) -> float:
        if not self.steps:
            return 0.0
        return float(sum(step.score for step in self.steps) / len(self.steps))

    def failure_points(self) -> list[EvaluationStep]:
        return [step for step in self.steps if not step.passed]
