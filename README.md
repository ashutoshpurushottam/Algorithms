# Module Boot Order

A small utility for computing a deterministic startup order for modules in a monorepo-style application.

When multiple services or UI modules depend on one another, startup order matters. A host may need a dependency to be ready first, a tracking module may rely on the host, and a tab may depend on both. If you start modules in the wrong order, you can get flaky boots and race conditions that are hard to debug.

This project models those dependencies as a graph and resolves a safe order using a stable topological sort.

## What it does

- Accepts a list of module IDs and dependency edges
- Treats each edge as a prerequisite: A before B
- Ignores optional draft edges so future plans can stay in the same file without affecting live startup order
- Produces a deterministic ordering using Kahn's algorithm
- Breaks ties by choosing the lexicographically smallest module ID next

That final tie-break keeps the result stable across machines and CI runs.

## Install

```bash
python -m pip install -e ".[dev]"
```

## Library usage

```python
from module_boot_order import compute_boot_order

nodes = ["CL", "LH", "CC"]
required = [("CL", "LH"), ("LH", "CC")]
optional = [("CL", "EL")]

order = compute_boot_order(nodes, required, optional)
print(",".join(order))
```

Example output:

```text
CL,LH,CC
```

## CLI usage

```bash
module-boot-order examples/sample_monorepo.json
```

This prints a comma-joined list with no spaces:

```text
CL,LH,CC,EL
```

To print one module per line:

```bash
module-boot-order examples/sample_monorepo.json --one-per-line
```

## Graph file shape

The example file at `examples/sample_monorepo.json` shows the expected structure.

- `nodes`: the complete list of module IDs
- `required_edges`: the live prerequisite list
- `optional_edges`: draft or non-blocking edges ignored by the sorter
- `names`: optional human-readable labels for each module

## Why the tie-break matters

Without a consistent rule, two ready modules can appear in different orders depending on hash seed or map iteration. By always choosing the lexicographically smallest available module, the result becomes repeatable, easier to log, and safer for golden tests and rollout checklists.

## Tests

```bash
pytest
```

## License

MIT
