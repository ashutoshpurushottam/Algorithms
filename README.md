# Module Boot Order

This project helps you decide the order in which modules should start in a monorepo style app.

Mobile products often have many pieces that depend on each other. A lead funnel host may need create lead to finish first. Tracking may need the host. A map tab may need both tracking and a sync worker. If you start things in the wrong order you get flaky boots and hard to debug races.

## What it does

You describe modules and required before links.

An edge from A to B means A must start before B.

You can also pass optional draft links. Those are ignored on purpose so you can keep future plans in the same file without changing the live order.

The tool then prints one deterministic boot order using Kahn topological sort. When several modules are ready at once it always picks the lexicographically smallest module id next. That keeps the result stable across machines and CI runs.

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

## CLI usage

```bash
module-boot-order examples/sample_monorepo.json
```

That prints a comma joined list with no spaces.

```bash
module-boot-order examples/sample_monorepo.json --one-per-line
```

That prints one id per line.

## Graph file shape

`examples/sample_monorepo.json` shows the expected JSON.

- `nodes` is the full module id list
- `required_edges` is the live prerequisite list
- `optional_edges` is ignored by the sorter
- `names` is optional human labels for reading

## Tests

```bash
pytest
```

## Why the tie break matters

Without a rule two ready modules can be ordered differently depending on hash seed or map iteration. A fixed lexicographic rule makes the order repeatable. That is useful for logs, rollout checklists, and golden tests.

## License

MIT
