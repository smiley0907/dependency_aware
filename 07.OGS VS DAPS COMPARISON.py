# ================================================================
# CELL 7 — OGS VS DAPS COMPARISON
#
# FUNCTIONALITY:
# This cell combines the OGS and DAPS results and calculates the
# improvement achieved by dependency aware scheduling.
#
# PRIMARY COMPARISON:
#
#       OGS Parallelism Ratio
#                    VS
#       DAPS Parallelism Ratio
#
# IMPROVEMENT FORMULA:
#
# Parallelism Improvement (%) =
#
#   ((DAPS Ratio - OGS Ratio) / OGS Ratio) × 100
#
# Positive values indicate increased parallel execution capability.
# ================================================================

comparison_df = pd.DataFrame({
    "Qubits": QUBIT_SIZES,

    "OGS Dependency Levels":
        ogs_df["Dependency Levels"],

    "DAPS Dependency Levels":
        daps_df["Dependency Levels"],

    "OGS Ready Gate Count":
        ogs_df["Ready Gate Count"],

    "DAPS Ready Gate Count":
        daps_df["Ready Gate Count"],

    "OGS Parallel Gate Groups":
        ogs_df["Parallel Gate Groups"],

    "DAPS Parallel Gate Groups":
        daps_df["Parallel Gate Groups"],

    "OGS Parallelism Ratio (%)":
        ogs_df["Parallelism Ratio (%)"],

    "DAPS Parallelism Ratio (%)":
        daps_df["Parallelism Ratio (%)"]
})


# ------------------------------------------------
# Calculate relative improvement in Parallelism Ratio.
# ------------------------------------------------

comparison_df["Parallelism Improvement (%)"] = (

    (
        comparison_df["DAPS Parallelism Ratio (%)"]
        -
        comparison_df["OGS Parallelism Ratio (%)"]
    )

    /

    comparison_df["OGS Parallelism Ratio (%)"]

) * 100


print("FINAL OGS VS DAPS COMPARISON")
print("=" * 60)

display(comparison_df)
