import pytest

from module_boot_order import CycleError, compute_boot_order
from module_boot_order.order import order_to_csv


def test_simple_chain():
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C")]
    assert compute_boot_order(nodes, edges) == ["A", "B", "C"]


def test_diamond():
    nodes = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    assert compute_boot_order(nodes, edges) == ["A", "B", "C", "D"]


def test_lex_tie_break_two_roots():
    nodes = ["CC", "CL", "LH"]
    edges = [("CL", "LH")]
    assert compute_boot_order(nodes, edges) == ["CC", "CL", "LH"]


def test_optional_edges_ignored():
    nodes = ["A", "B", "C"]
    required = [("A", "B")]
    optional = [("C", "A"), ("B", "C")]
    # Optional edges are ignored so only A before B remains.
    # Ready starts as A and C. Lex picks A then C then B.
    # After A, ready is B and C. Lex picks B before C.
    assert compute_boot_order(nodes, required, optional) == ["A", "B", "C"]


def test_sample_monorepo_shape():
    nodes = ["CL", "LH", "CC", "PD", "ID", "RD", "EL", "FC", "TE", "QP", "SW", "MP"]
    required = [
        ("CL", "LH"),
        ("LH", "CC"),
        ("CC", "PD"),
        ("PD", "ID"),
        ("ID", "RD"),
        ("RD", "EL"),
        ("RD", "FC"),
        ("LH", "TE"),
        ("TE", "QP"),
        ("QP", "SW"),
        ("TE", "MP"),
        ("SW", "MP"),
    ]
    optional = [("CL", "EL"), ("CC", "EL"), ("FC", "EL")]
    order = compute_boot_order(nodes, required, optional)
    assert order == [
        "CL",
        "LH",
        "CC",
        "PD",
        "ID",
        "RD",
        "EL",
        "FC",
        "TE",
        "QP",
        "SW",
        "MP",
    ]
    assert order_to_csv(order) == "CL,LH,CC,PD,ID,RD,EL,FC,TE,QP,SW,MP"


def test_cycle_raises():
    nodes = ["A", "B"]
    edges = [("A", "B"), ("B", "A")]
    with pytest.raises(CycleError):
        compute_boot_order(nodes, edges)
