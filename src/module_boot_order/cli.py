"""Command line entry for module boot order."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .order import CycleError, BootOrderError, compute_boot_order, order_to_csv


def _load_graph(path: Path) -> tuple[list[str], list[tuple[str, str]], list[tuple[str, str]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    nodes = list(data.get("nodes") or [])
    required = [tuple(e) for e in data.get("required_edges") or []]
    optional = [tuple(e) for e in data.get("optional_edges") or []]
    if not nodes:
        inferred = set()
        for a, b in required + optional:
            inferred.add(a)
            inferred.add(b)
        nodes = sorted(inferred)
    return nodes, required, optional


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print a deterministic module boot order from a JSON graph."
    )
    parser.add_argument(
        "graph",
        type=Path,
        help="Path to a JSON graph file with nodes, required_edges, optional_edges.",
    )
    parser.add_argument(
        "--one-per-line",
        action="store_true",
        help="Print one module id per line instead of a comma joined list.",
    )
    args = parser.parse_args(argv)

    try:
        nodes, required, optional = _load_graph(args.graph)
        order = compute_boot_order(nodes, required, optional)
    except (OSError, json.JSONDecodeError, BootOrderError, CycleError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.one_per_line:
        print("\n".join(order))
    else:
        print(order_to_csv(order))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
