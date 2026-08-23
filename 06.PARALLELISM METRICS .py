# ================================================================
# CELL 6 — PARALLELISM METRICS
#
# FUNCTIONALITY:
# This cell calculates scheduling metrics for OGS and DAPS.
#
# PRIMARY METRIC:
#
# Parallelism Ratio (%) =
#
#       Average Gates Executed Per Layer
#       -------------------------------- × 100
#              Number of Qubits
#
# Where:
#
# Average Gates Per Layer =
#       Total Gates / Number of Schedule Levels
#
# A higher Parallelism Ratio indicates that a larger proportion
# of the available qubit execution capacity is being utilized
# concurrently.
#
# SUPPORTING METRICS:
#   • Dependency Levels
#   • Ready Gate Count
#   • Parallel Gate Groups
# ================================================================

def calculate_schedule_metrics(schedule, num_qubits):
    """
    Calculate scheduling metrics for a given schedule.
    """

    total_gates = sum(
        len(layer)
        for layer in schedule
    )

    dependency_levels = len(schedule)

    # ------------------------------------------------
    # Number of layers containing more than one gate.
    # ------------------------------------------------

    parallel_gate_groups = sum(
        1
        for layer in schedule
        if len(layer) > 1
    )

    # ------------------------------------------------
    # Maximum number of simultaneously executable gates.
    # ------------------------------------------------

    ready_gate_count = max(
        (len(layer) for layer in schedule),
        default=0
    )

    # ------------------------------------------------
    # Average number of gates executed per layer.
    # ------------------------------------------------

    average_parallelism = (
        total_gates / dependency_levels
        if dependency_levels > 0
        else 0
    )

    # ------------------------------------------------
    # Primary research metric.
    # ------------------------------------------------

    parallelism_ratio = (
        average_parallelism / num_qubits
    ) * 100

    return {
        "Total Gates": total_gates,
        "Dependency Levels": dependency_levels,
        "Ready Gate Count": ready_gate_count,
        "Parallel Gate Groups": parallel_gate_groups,
        "Parallelism Ratio (%)": parallelism_ratio
    }


# ------------------------------------------------
# Calculate OGS and DAPS metrics.
# ------------------------------------------------

ogs_metrics = []
daps_metrics = []

for n in QUBIT_SIZES:

    ogs_metrics.append({
        "Qubits": n,
        **calculate_schedule_metrics(
            ogs_results[n],
            n
        )
    })

    daps_metrics.append({
        "Qubits": n,
        **calculate_schedule_metrics(
            daps_results[n],
            n
        )
    })


ogs_df = pd.DataFrame(ogs_metrics)
daps_df = pd.DataFrame(daps_metrics)

print("OGS Metrics")
display(ogs_df)

print("\nDAPS Metrics")
display(daps_df)
