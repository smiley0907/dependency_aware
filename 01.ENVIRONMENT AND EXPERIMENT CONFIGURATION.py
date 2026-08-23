# ================================================================
# CELL 1 — ENVIRONMENT AND EXPERIMENT CONFIGURATION
#
# FUNCTIONALITY:
# This cell imports the required Python libraries and defines the
# experimental configurations used throughout the study.
#
# RESEARCH OBJECTIVE:
# Evaluate whether dependency aware scheduling can increase the
# parallel execution capability of quantum circuits.
#
# BEFORE METHOD:
# OGS — Original Gate Order Schedule
#
# AFTER METHOD:
# DAPS — Dependency Aware Parallel Schedule
#
# PRIMARY PARAMETER:
# Parallelism Ratio (%)
#
# QUBIT CONFIGURATIONS:
# 3, 5, 7, 9, and 11 qubits
# ================================================================

import pandas as pd
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit


# ------------------------------------------------
# Qubit configurations used in the experiment.
# ------------------------------------------------

QUBIT_SIZES = [3, 5, 7, 9, 11]


# ------------------------------------------------
# Primary research parameter.
# ------------------------------------------------

PRIMARY_METRIC = "Parallelism Ratio (%)"


# ------------------------------------------------
# Display experiment configuration.
# ------------------------------------------------

print("Dependency Aware Quantum Gate Scheduling")
print("=" * 60)
print(f"Qubit configurations : {QUBIT_SIZES}")
print(f"Primary parameter    : {PRIMARY_METRIC}")
print("Before method        : OGS")
print("After method         : DAPS")
print("=" * 60)
