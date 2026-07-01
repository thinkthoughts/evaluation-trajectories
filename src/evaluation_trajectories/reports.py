from pathlib import Path

def write_markdown_report(rows: list[dict], output_path: str | Path) -> Path:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Evaluation Trajectory Report", ""]
    for row in rows:
        lines.append(f"## {row['model_id']}")
        lines.append(f"- Final score: {row['final_score']:.3f}")
        lines.append(f"- Reliability: {row['reliability']:.3f}")
        lines.append(f"- Failure count: {row['failure_count']}")
        lines.append("")
    output_path.write_text("\n".join(lines))
    return output_path
