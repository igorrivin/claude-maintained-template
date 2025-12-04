# Claude-Maintained Python Package Template

**Self-healing Python packages powered by Claude AI.**

This template provides GitHub Actions workflows that automatically detect and fix compatibility issues when dependencies update. No more bitrot!

## The Problem

Scientific and mathematical Python packages frequently break because:
- NumPy/SciPy/etc. change APIs
- Deprecation warnings become errors
- Transitive dependencies conflict
- Maintainers move on, packages rot

## The Solution

This template includes a **monthly maintenance workflow** that:

1. Tests your package with the **latest versions** of all dependencies
2. If tests fail, **invokes Claude AI** to diagnose and fix the issues
3. **Creates a PR** with the fixes for your review
4. If Claude can't fix it, **creates an issue** for manual intervention

Your package essentially maintains itself.

## Quick Start

### 1. Use this template

Click "Use this template" on GitHub, or:

```bash
gh repo create my-package --template igorrivin/claude-maintained-template
```

### 2. Add your Anthropic API key

```bash
# Get a key from https://console.anthropic.com/
gh secret set ANTHROPIC_API_KEY --repo your-username/my-package
```

### 3. Customize for your package

1. Rename `src/my_package/` to your package name
2. Update `pyproject.toml` with your package info
3. Write your tests in `tests/`
4. Update dependencies in `pyproject.toml`

### 4. That's it!

The workflows will:
- Run CI on every push/PR
- Run monthly maintenance on the 1st of each month
- Auto-fix issues and create PRs

## How It Works

### Regular CI (`.github/workflows/ci.yml`)

Standard CI that runs on pushes and PRs:
- Tests multiple Python versions (3.10, 3.11, 3.12)
- Uses pinned dependencies from your `pyproject.toml`

### Monthly Maintenance (`.github/workflows/monthly-maintenance.yml`)

The magic happens here:

```
┌─────────────────────────────────────────────────────────────┐
│  1st of Month: Scheduled Run                                │
├─────────────────────────────────────────────────────────────┤
│  1. Install LATEST versions of all dependencies             │
│  2. Run test suite                                          │
│                                                             │
│  Tests Pass?                                                │
│  ├─ YES → Log success, done                                 │
│  └─ NO  → Continue to Claude fix                            │
│                                                             │
│  3. Install Claude Code CLI                                 │
│  4. Give Claude the test output + codebase                  │
│  5. Claude diagnoses and fixes issues                       │
│  6. Run tests again                                         │
│                                                             │
│  Fixed?                                                     │
│  ├─ YES → Create PR with fixes                              │
│  └─ NO  → Create Issue for manual review                    │
└─────────────────────────────────────────────────────────────┘
```

## Customization

### Adjusting the schedule

Edit `.github/workflows/monthly-maintenance.yml`:

```yaml
on:
  schedule:
    # Run weekly instead of monthly
    - cron: '0 0 * * 0'  # Every Sunday at midnight
```

### Adding dependencies

Update `pyproject.toml`:

```toml
dependencies = [
    "numpy",
    "scipy",
    "your-dependency",
]
```

### Custom test commands

Edit the test step in the workflows:

```yaml
- name: Run tests
  run: |
    pytest tests/ -v --tb=long
    # Add more test commands here
```

### Rust dependencies

If your package needs Rust (like many modern Python packages), the template includes Rust installation. See the commented sections in `ci.yml`.

## Best Practices

### 1. Write good tests

The better your tests, the better Claude can diagnose issues:
- Test core functionality
- Test edge cases
- Test with various input types
- Include integration tests

### 2. Keep dependencies minimal

Fewer dependencies = fewer potential breakages:
- Only add dependencies you truly need
- Prefer standard library when possible
- Consider vendoring stable, small dependencies

### 3. Pin major versions (optional)

In `pyproject.toml`, you can set bounds:

```toml
dependencies = [
    "numpy>=1.20,<3",  # Allow minor updates, not major
]
```

### 4. Review auto-generated PRs

Claude's fixes are usually correct, but always review:
- Check the changes make sense
- Ensure no unintended modifications
- Run additional manual tests if needed

## FAQ

### How much does this cost?

The Claude API calls are minimal (only when tests fail). Typical cost: < $1/month for most packages.

### What if Claude can't fix it?

The workflow creates a GitHub Issue with the full test output, so you can diagnose manually.

### Can I trigger maintenance manually?

Yes:
```bash
gh workflow run monthly-maintenance.yml
```

Or click "Run workflow" in the GitHub Actions UI.

### Does this work for non-Python packages?

The pattern can be adapted for any language. The key components are:
1. Test with latest dependencies
2. Capture failure output
3. Give output to Claude
4. Apply fixes

## Examples

Packages using this pattern:
- [tl-tensor-examples](https://github.com/igorrivin/tl-tensor-examples) - Knot theory computations

## Contributing

Improvements welcome! Ideas:
- Support for other languages
- Smarter dependency update strategies
- Integration with Dependabot/Renovate
- Notification systems (Slack, Discord, email)

## License

MIT - Use freely, maintain effortlessly.

---

*"The best code is code that maintains itself."*
