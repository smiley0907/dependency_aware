# ================================================================
# CELL 5 — DEPENDENCY AWARE PARALLEL SCHEDULE (DAPS)
#
# FUNCTIONALITY:
# This cell implements the proposed DAPS scheduling algorithm.
#
# DAPS operates using the dependency graph created in Cell 3.
#
# PROCESS:
#
#   1. Identify all currently ready gates.
#   2. Select ready gates that do not share qubits.
#   3. Place those gates into the same parallel layer.
#   4. Mark the selected gates as completed.
#   5. Recalculate the ready gate set.
#   6. Continue until every gate is scheduled.
#
# This is different from OGS because DAPS is allowed to select
# independent ready gates from different positions in the original
# circuit order.
#
# IMPORTANT:
# No gate operations are removed or modified.
# Only their execution schedule is reorganized.
# ================================================================

def create_daps_schedule(gates):
    """
    Create the Dependency Aware Parallel Schedule (DAPS).

    Parameters
    ----------
    gates : list
        Gates containing predecessor information.

    Returns
    -------
    list
        DAPS scheduling layers.
    """

    completed = set()
    schedule = []

    total_gates = len(gates)

    # ------------------------------------------------
    # Continue until every gate has been scheduled.
    # ------------------------------------------------

    while len(completed) < total_gates:

        # ------------------------------------------------
        # Identify gates whose predecessors have all
        # already been completed.
        # ------------------------------------------------

        ready_gates = []

        for gate in gates:

            gate_id = gate["gate_id"]

            if gate_id in completed:
                continue

            if gate["predecessors"].issubset(completed):

                ready_gates.append(gate)

        # ------------------------------------------------
        # Select mutually nonconflicting ready gates.
        # ------------------------------------------------

        current_layer = []
        used_qubits = set()

        for gate in ready_gates:

            gate_qubits = set(gate["qubits"])

            # ------------------------------------------------
            # A gate can join the current layer only when
            # none of its qubits are already occupied.
            # ------------------------------------------------

            if gate_qubits.isdisjoint(used_qubits):

                current_layer.append(gate)
                used_qubits.update(gate_qubits)

        # ------------------------------------------------
        # Safety check to prevent an infinite scheduling loop.
        # ------------------------------------------------

        if not current_layer:

            raise RuntimeError(
                "DAPS could not identify a schedulable gate."
            )

        # ------------------------------------------------
        # Add the parallel layer to the schedule.
        # ------------------------------------------------

        schedule.append(current_layer)

        # ------------------------------------------------
        # Mark all selected gates as completed.
        # ------------------------------------------------

        for gate in current_layer:

            completed.add(
                gate["gate_id"]
            )

    return schedule


# ------------------------------------------------
# Generate DAPS schedules.
# ------------------------------------------------

daps_results = {}

for n in QUBIT_SIZES:

    daps_results[n] = create_daps_schedule(
        gate_data[n]
    )

    print(
        f"{n} qubits -> "
        f"DAPS dependency levels: "
        f"{len(daps_results[n])}"
    )

print("\nDAPS scheduling completed successfully.")
