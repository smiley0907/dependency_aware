# ================================================================
# CELL 8 — PRIMARY PARALLELISM RATIO GRAPH
#
# FUNCTIONALITY:
# This cell visualizes the primary experimental result.
#
# The graph compares the Parallelism Ratio (%) obtained from:
#
#   OGS  — Original Gate Order Schedule
#   DAPS — Dependency Aware Parallel Schedule
#
# across 3, 5, 7, 9, and 11 qubit configurations.
#
# INTERPRETATION:
# A higher DAPS curve compared with OGS indicates that dependency
# aware scheduling exposes additional opportunities for concurrent
# quantum gate execution.
# ================================================================

plt.figure(figsize=(9, 5))

plt.plot(
    comparison_df["Qubits"],
    comparison_df["OGS Parallelism Ratio (%)"],
    marker="o",
    linewidth=2,
    label="OGS"
)

plt.plot(
    comparison_df["Qubits"],
    comparison_df["DAPS Parallelism Ratio (%)"],
    marker="s",
    linewidth=2,
    label="DAPS"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Parallelism Ratio (%)")
plt.title("OGS vs DAPS Parallelism Ratio")

plt.xticks(QUBIT_SIZES)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
