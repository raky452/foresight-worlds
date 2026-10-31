# Foresight Worlds

**Digital world simulators to test AI agents before they reach the real world.**

AI agents are starting to act on real systems: they send messages, edit records, move money and operate tools. Foresight Worlds is an open-source effort to give those agents a place to practise first: simulated digital worlds where you can run an agent, watch what it does, introduce failures, and decide whether it is ready, before anything real is affected.

> Simulate the behaviour. Inspect the trace. Export the evidence. Then launch.

## How it fits together

```
 agent ──▶ simulated world ──▶ behaviour trace ──▶ converters ──▶ JSON · CSV · PDF report · images · video
                 ▲                                                 │
                 └──────────── scenarios and failure injection ◀───┘
```

- **Worlds**: simulated environments with their own state and rules (documents, inboxes, files, services).
- **Scenarios**: repeatable tasks and injected failures that test how an agent behaves under pressure.
- **Traces**: a full record of what the agent saw, decided and changed.
- **Converters**: turn traces and world state into the formats people already use for analysis, review and replay.

## What is here today

The project starts with the converter layer, because every simulation ends with something to export.

| Path | What it is | Status |
|---|---|---|
| [`apps/tools-site`](apps/tools-site) | Browser-based converters for images and PDFs (HEIC, WebP, AVIF, PNG, JPG, compress to exact size, merge, split, rotate, PDF ⇄ images). Everything runs on the user's device; nothing is uploaded. Live at [technoforesight.in](https://technoforesight.in). | Live |
| `packages/` | Reusable converter and trace libraries for use inside simulations | Planned |
| `worlds/` | First simulated worlds and scenarios | Planned |
| `connectors/` | MCP servers so any AI agent can enter a world through a standard protocol | Planned |

See [docs/vision.md](docs/vision.md) and [docs/roadmap.md](docs/roadmap.md).

## Run the tools site locally

Requires Python 3.9+.

```bash
cd apps/tools-site
python3 build.py              # generates public/
python3 -m http.server -d public 8080
```

Open http://localhost:8080. Deploy with `firebase deploy` (the build runs automatically before deploying).

## Principles

- **Local first.** Processing happens on the user's device wherever possible. Private data stays private.
- **Inspectable.** Every run should leave a trace a human can read and replay.
- **Open formats.** Outputs use widely supported formats, never a lock-in format.
- **Small, composable pieces.** Converters, worlds and connectors are separate parts with clear interfaces.

## Contributing

Issues and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

[MIT](LICENSE). Third-party libraries used by the tools site (pdf-lib, PDF.js, heic2any, JSZip) are loaded at runtime from public CDNs and keep their own licenses.
