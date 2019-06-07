"""Kahn topological sort with lexicographic tie break for module boot order."""

from __future__ import annotations

from collections import defaultdict
from typing import Iterable, Mapping, Sequence


class BootOrderError(ValueError):
    """Base error for boot order computation."""


class CycleError(BootOrderError):
    """Raised when the solid dependency graph contains a cycle."""


def compute_boot_order(
    nodes: Sequence[str],
    required_edges: Iterable[tuple[str, str]],
    optional_edges: Iterable[tuple[str, str]] | None = None,
) -> list[str]:
    """Return a deterministic initialization order for ``nodes``.

    Each required edge ``(a, b)`` means ``a`` must boot before ``b``.
    Optional edges are ignored. They exist so callers can pass draft or
    future edges without changing the order.

    When several modules are ready (indegree zero), the lexicographically
    smallest module id is chosen next.
    """
    if optional_edges is None:
        optional_edges = ()

    node_set = set(nodes)
    if len(node_set) != len(nodes):
        raise BootOrderError("duplicate module ids in nodes list")

    for edge_set_name, edge_set in (
        ("required_edges", required_edges),
        ("optional_edges", optional_edges),
    ):
        for edge in edge_set:
            if len(edge) != 2:
                raise BootOrderError(f"bad edge in {edge_set_name}: {edge!r}")
            a, b = edge
            if a not in node_set or b not in node_set:
                raise BootOrderError(
                    f"edge {a!r} -> {b!r} references an unknown module id"
                )

    successors: dict[str, list[str]] = defaultdict(list)
    indegree: dict[str, int] = {n: 0 for n in nodes}

    for a, b in required_edges:
        successors[a].append(b)
        indegree[b] += 1

    ready = sorted(n for n, d in indegree.items() if d == 0)
    order: list[str] = []

    while ready:
        current = ready.pop(0)
        order.append(current)
        for nxt in successors[current]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                ready.append(nxt)
                ready.sort()

    if len(order) != len(nodes):
        stuck = sorted(n for n, d in indegree.items() if d > 0)
        raise CycleError(
            "dependency cycle detected. modules still blocked: "
            + ", ".join(stuck)
        )

    return order


def order_to_csv(order: Sequence[str]) -> str:
    """Join ids with commas and no spaces."""
    return ",".join(order)


def graph_from_mapping(
    required: Mapping[str, Sequence[str]],
    optional: Mapping[str, Sequence[str]] | None = None,
) -> tuple[list[str], list[tuple[str, str]], list[tuple[str, str]]]:
    """Build nodes and edge lists from adjacency maps.

    Keys are prerequisites. Values are modules that depend on the key.
    """
    optional = optional or {}
    nodes = sorted(set(required) | set(optional) | {m for deps in required.values() for m in deps} | {m for deps in optional.values() for m in deps})
    req_edges = [(a, b) for a, deps in required.items() for b in deps]
    opt_edges = [(a, b) for a, deps in optional.items() for b in deps]
    return nodes, req_edges, opt_edges
