# CLI tool readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Command contract
- Define supported commands, exit codes, stdout/stderr behavior, structured output schema, config/env/flag precedence, and compatibility promises.
- Test help/version, invalid arguments, missing input, empty results, stdin/pipes, non-TTY operation, broken pipes, Unicode, and paths with spaces or leading dashes.
- Ensure progress/prompts do not corrupt machine-readable stdout. Test no-color behavior and secret redaction in verbose/error modes.

## Side effects and safety
- Verify destructive operations target only intended resources and provide the documented dry-run/confirmation behavior. Dry-run must avoid side effects, including remote writes.
- Test path traversal, symlink escape, shell injection, unsafe temporary files, untrusted config, and command argument boundaries using isolated fixtures.
- Exercise timeout, Ctrl-C/signals, child-process cleanup, partial downloads/writes, disk full, and interrupted multi-step operations. Keep original files recoverable until replacements are safely committed.
- Validate credential storage, env leakage, logs, scoped network access, TLS verification, and retry/idempotency behavior.

## Packaging and compatibility
- Install the built artifact into a clean environment outside the source checkout; verify command entrypoint, executable bits, shebang/runtime, bundled assets, and native dependencies.
- Run supported OS/shell/runtime combinations and ensure path/home/config locations follow platform behavior. Do not silently require an interactive shell in automation.
- Check versioned release assets, checksums/signatures where used, dependency/license metadata, and upgrade/uninstall behavior.

## Release evidence
- Test core commands against controlled local/remote fixtures, including failure exits and structured-output consumers. Avoid testing remote mutation commands against production by default.
- Measure large-input memory/streaming and completion time against intended workload. Verify docs match the installed command's behavior and provide repair/recovery guidance.
- Confirm artifact identity, release/install instructions, support ownership, and update compatibility. Keep telemetry optional unless explicitly part of the product contract.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [POSIX utility conventions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html)
- [Python packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
