# Evaluation Trajectories

**Leads specify trails.**

<img src="figures/2606-24155.png" />

Open evaluation infrastructure for frontier AI research, inspired by process-oriented evaluation in MedBench v5, hidden-state diagnostics, behavioral regression testing, and foundational work on implicit regularization and capacity control.

## Core question

How do we know a frontier model actually improved?

A single benchmark score can hide unstable reasoning, hallucination propagation, degraded calibration, brittle recovery, or regressions in adjacent capabilities. This repository treats evaluation as a trajectory: a structured record of model behavior across prompts, reasoning steps, stress conditions, tool-use states, and repeated runs.

## Research anchors

- arXiv:2606.24155 — MedBench v5: dynamic, process-oriented, hallucination-aware evaluation.
- arXiv:1709.01953 — implicit regularization and generalization in deep learning.
- arXiv:1503.00036 — norm-based capacity control in neural networks.
- arXiv:2007.13657 — learning inductive biases from data via description-length principles.

## Notebook roadmap

| Notebook | Question |
|---|---|
| `00_context.ipynb` | Why are benchmark scores insufficient? |
| `07_process_evaluation.ipynb` | What is an evaluation trajectory? |
| `13_behavioral_invariants.ipynb` | What behaviors remain stable across perturbations? |
| `17_representation_trajectories.ipynb` | How do model representations drift across runs or checkpoints? |
| `23_capability_profiles.ipynb` | How do capability profiles expose strengths and weaknesses? |
| `29_regression_detection.ipynb` | How do we detect regressions automatically? |
| `37_hidden_state_metrics.ipynb` | Which internal metrics could support observability? |
| `43_dashboard.ipynb` | How should humans inspect model behavior efficiently? |
| `47_open_evaluation_pipeline.ipynb` | What should a reproducible evaluation pipeline provide? |

## Initial architecture

```text
evaluate -> analyze -> prioritize -> train -> re-evaluate -> deploy
```

## Conceptual specification

```math
R = F(T, C, S, H, U)
```

Reliability depends on trajectory quality, capability profile, stress robustness, hallucination control, and uncertainty calibration.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/scripts/run_pipeline.py
```

Outputs are written to `results/metrics/`, `results/figures/`, and `results/reports/`.
