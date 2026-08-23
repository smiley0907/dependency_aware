# ================================================================
# CELL 9 — SAVE PRIMARY RESULT FIGURE
#
# FUNCTIONALITY:
# This cell saves the primary OGS vs DAPS Parallelism Ratio
# figure as a high-resolution PNG for use in the research paper
# and GitHub repository.
# ================================================================

figure_file = "ogs_vs_daps_parallelism_ratio.png"

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

plt.savefig(
    figure_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Figure saved to: {figure_file}")
