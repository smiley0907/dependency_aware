# ================================================================
# CELL 3 — GATE EXTRACTION AND DEPENDENCY GRAPH CONSTRUCTION
#
# FUNCTIONALITY:
# This cell extracts all executable gates and constructs a
# dependency graph based on qubit usage.
#
# DEPENDENCY RULE:
# If two consecutive operations use the same qubit, the later
# operation depends on the earlier operation.
#
# Each gate stores:
#
#   • Gate ID
#   • Gate name
#   • Qubits used
#   • Predecessor gates
#   • Original circuit position
#
# The resulting dependency graph is used by DAPS to determine
# which gates are ready for execution.
# ================================================================

def extract_gate_dependencies(qc):
    """
    Extract gates and construct their dependency relationships.

    Returns
    -------
    list
        Gate information containing predecessor relationships.
    """

    gates = []

    # ------------------------------------------------
    # Track the most recent gate using each qubit.
    # ------------------------------------------------

    last_gate_on_qubit = {}

    for instruction, qargs, _ in qc.data:

        # Measurements are not part of gate scheduling.
        if instruction.name == "measure":
            continue

        gate_id = len(gates)

        qubits = [q._index for q in qargs]

        # ------------------------------------------------
        # Identify predecessor gates.
        # ------------------------------------------------

        predecessors = set()

        for q in qubits:

            if q in last_gate_on_qubit:
                predecessors.add(
                    last_gate_on_qubit[q]
                )

        # ------------------------------------------------
        # Store gate information.
        # ------------------------------------------------

        gates.append({
            "gate_id": gate_id,
            "gate_name": instruction.name,
            "qubits": qubits,
            "predecessors": predecessors
        })

        # ------------------------------------------------
        # This gate becomes the most recent operation
        # on every qubit it uses.
        # ------------------------------------------------

        for q in qubits:
            last_gate_on_qubit[q] = gate_id

    return gates


# ------------------------------------------------
# Build dependency information for every circuit.
# ------------------------------------------------

gate_data = {}

for n in QUBIT_SIZES:

    gate_data[n] = extract_gate_dependencies(
        circuits[n]
    )

    dependency_count = sum(
        len(gate["predecessors"])
        for gate in gate_data[n]
    )

    print(
        f"{n} qubits -> "
        f"{len(gate_data[n])} gates, "
        f"{dependency_count} dependencies"
    )

print("\nDependency graph construction completed.")
