# ================================================================
# CELL 2 — BENCHMARK QUANTUM CIRCUIT GENERATION
#
# FUNCTIONALITY:
# This cell creates interleaved quantum circuits for the selected
# qubit configurations.
#
# DESIGN PRINCIPLE:
# The circuit contains:
#
#   • Independent single qubit operations
#   • Qubit dependent operations
#   • Multi qubit dependency forming operations
#
# The operations are deliberately interleaved in their original
# order. This creates opportunities for DAPS to identify gates
# that can be executed concurrently.
#
# IMPORTANT:
# The gate set is identical for OGS and DAPS.
# No gates are removed, duplicated, or replaced.
# Only the execution schedule is changed.
# ================================================================

def create_benchmark_circuit(num_qubits):
    """
    Create an interleaved quantum scheduling benchmark.

    Parameters
    ----------
    num_qubits : int
        Number of qubits in the circuit.

    Returns
    -------
    QuantumCircuit
        Generated benchmark circuit.
    """

    qc = QuantumCircuit(num_qubits)

    # ------------------------------------------------
    # Interleaved single qubit operations.
    #
    # The alternating operations deliberately place
    # independent gates at different positions in the
    # original circuit sequence.
    # ------------------------------------------------

    for q in range(num_qubits):

        qc.h(q)

        # Apply an operation to the next qubit.
        if q + 1 < num_qubits:
            qc.x(q + 1)

    # ------------------------------------------------
    # Dependency forming two qubit operations.
    #
    # Adjacent pairs create explicit dependencies that
    # must be respected by the scheduler.
    # ------------------------------------------------

    for q in range(0, num_qubits - 1, 2):
        qc.cx(q, q + 1)

    # ------------------------------------------------
    # Final single qubit operations.
    #
    # These operations depend on earlier operations
    # involving the same qubits.
    # ------------------------------------------------

    for q in range(num_qubits):
        qc.h(q)

    return qc


# ------------------------------------------------
# Generate benchmark circuits.
# ------------------------------------------------

circuits = {}

for n in QUBIT_SIZES:

    circuits[n] = create_benchmark_circuit(n)

    print(
        f"{n} qubits -> "
        f"{len(circuits[n].data)} circuit operations"
    )

print("\nBenchmark circuit generation completed.")
