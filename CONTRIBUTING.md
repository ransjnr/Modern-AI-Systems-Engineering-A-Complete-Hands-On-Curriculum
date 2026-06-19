# Contributing

Thanks for helping improve the 10-Day Tech Giants Sprint!

## Ways to contribute
- 🐛 Fix bugs in project code or docs
- 📝 Improve a project README or add clarifying comments
- ✨ Add a new **bonus challenge** solution under a project's `bonus/` folder
- 🌍 Translate a day's README

## Workflow
1. Fork the repo and create a branch: `git checkout -b fix/day-02-typo`
2. Make your change. Keep each project self-contained and runnable.
3. Run formatting and tests:
   ```bash
   make lint
   make test
   ```
4. Open a pull request describing the change and which day/project it affects.

## Style
- Python formatted with `black`, linted with `ruff`.
- Every new project must include a `README.md`, a dependency file, and at least one test.
- Never commit secrets or large data/model files (they belong in `.gitignore` / DVC).
