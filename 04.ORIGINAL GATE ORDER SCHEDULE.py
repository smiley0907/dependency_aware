# ================================================================
# CELL 4 — ORIGINAL GATE ORDER SCHEDULE (OGS)
#
# FUNCTIONALITY:
# This cell creates the BEFORE schedule by preserving the original
# ordering of the gates in the quantum circuit.
#
# OGS does not perform global dependency based reordering.
#
# Consecutive gates that do not conflict on their qubits may share
# the current layer, but once a conflicting gate is encountered,
# the current layer is closed and the next layer begins.
#
# This represents the natural scheduling behavior associated with
# the original gate ordering.
#
# OUTPUT:
# Original Gate Order Schedule (OGS)
# ================================================================

def create_ogs_schedule(gates):
    """
    Create the Original Gate Order Schedule (OGS).

    Parameters
    ----------
    gates : list
        Gates in original circuit order.

    Returns
    -------
    list
        OGS scheduling layers.
    """

    schedule = []

    current_layer = []
    used_qubits = set()

    # ------------------------------------------------
    # Process gates strictly in their original order.
    # ------------------------------------------------

    for gate in gates:

        gate_qubits = set(gate["qubits"])

        # ------------------------------------------------
        # If the gate does not conflict with the current
        # layer, keep it in that layer.
        # ------------------------------------------------

        if gate_qubits.isdisjoint(used_qubits):

            current_layer.append(gate)
            used_qubits.update(gate_qubits)

        else:

            # ------------------------------------------------
            # Close the current layer before starting another.
            # ------------------------------------------------

            if current_layer:
                schedule.append(current_layer)

            current_layer = [gate]
            used_qubits = set(gate_qubits)

    # ------------------------------------------------
    # Add the final layer.
    # ------------------------------------------------

    if current_layer:
        schedule.append(current_layer)

    return schedule


# ------------------------------------------------
# Generate OGS schedules.
# ------------------------------------------------

ogs_results = {}

for n in QUBIT_SIZES:

    ogs_results[n] = create_ogs_schedule(
        gate_data[n]
    )

    print(
        f"{n} qubits -> "
        f"OGS dependency levels: "
        f"{len(ogs_results[n])}"
    )

print("\nOGS scheduling completed.")
