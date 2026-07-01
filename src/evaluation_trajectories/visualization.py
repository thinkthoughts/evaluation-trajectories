from pathlib import Path
import matplotlib.pyplot as plt

def plot_scores(rows: list[dict], output_path: str | Path) -> Path:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    labels = [r["model_id"] for r in rows]
    values = [r["reliability"] for r in rows]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(labels, values)
    ax.set_ylim(0, 1)
    ax.set_ylabel("trajectory reliability")
    ax.set_title("Toy evaluation trajectory comparison")
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    plt.close(fig)
    return output_path
