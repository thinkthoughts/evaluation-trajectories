def classify_regression(delta: float, tolerance: float = -0.05) -> str:
    if delta < tolerance:
        return "regression"
    if delta > abs(tolerance):
        return "improvement"
    return "stable"
