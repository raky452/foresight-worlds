# Contributing

Thanks for helping build Foresight Worlds.

## Ground rules
- Open an issue before large changes, so we can agree on the approach.
- Keep pull requests focused: one feature or fix per PR.
- No user data leaves the device in the tools site. New tools must process files locally unless the issue explicitly agrees otherwise.
- Pin exact versions of any third-party library and check its license is compatible with MIT.
- Never commit secrets, API keys or service-account files.

## Adding a converter to the tools site
Read [apps/tools-site/ARCHITECTURE.md](apps/tools-site/ARCHITECTURE.md). In short: add a handler in a module under `src/scripts/`, map it in `src/content/handlers.py`, add a page entry under `src/content/tools/`, then run `python3 build.py` and test in Chrome, Firefox and Safari, including on a phone.

## Reporting problems
Include the tool, browser and device, what you expected and what happened. Use a sample file rather than private documents.
