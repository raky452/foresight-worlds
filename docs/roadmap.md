# Roadmap

Plans change as we learn. Dates are targets, not promises.

## Stage 1: Converters (now)
- Browser-based image and PDF converters on technoforesight.in
- Next: video (compress, trim, MP4 to GIF), text and Indic script converters, document exports

## Stage 2: Converter packages
- Extract converters into reusable JavaScript packages under `packages/`
- Define a behaviour-trace format (JSON) and converters from traces to CSV, PDF reports and replays

## Stage 3: First worlds
- A small simulated document-and-inbox world with scripted scenarios
- Failure injection: lost responses, timeouts, conflicting data
- Trace viewer in the browser

## Stage 4: Connectors
- MCP server so agents can enter worlds through a standard protocol
- Scoring: outcome checks per scenario, comparable across agents
