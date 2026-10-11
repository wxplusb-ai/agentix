# Plugin Update Scripts

These scripts update an installed Agentix plugin to the latest published version. They run in the client environment: the project folder where the plugin is installed and the planning engagement takes place, on Windows or on Linux and WSL2. They do not run in the Agentix repository itself.

## Scripts

| Script | Environment | Plugin |
|---|---|---|
| `ai-ddp-planning-update.sh` | Linux, macOS and WSL2 (bash) | `ai-ddp-planning` |
| `ai-ddp-planning-update.ps1` | Windows (PowerShell) | `ai-ddp-planning` |

Both scripts run the same two commands:

```
claude plugin marketplace update agentix
claude plugin update ai-ddp-planning@agentix --scope project
```

The first refreshes the Agentix marketplace from GitHub. The second updates the plugin installed in the current project folder to the version the marketplace now lists.

## Before you run them

- The plugin must already be installed in the project folder. See "Installing the plugin" in [plugins/ai-ddp-planning/README.md](../../plugins/ai-ddp-planning/README.md).
- Run the script from the project folder. The update applies to the folder you run it in.
- Each installation is separate. If you plan in both Windows and WSL2, run the matching script in each.

## Running them

Change to the project folder, then run the script by its full path.

**Linux, macOS and WSL2:**

```bash
cd <path-to-project>
bash <path-to-agentix>/scripts/plugins/ai-ddp-planning-update.sh
```

**Windows:**

```powershell
cd <path-to-project>
& "<path-to-agentix>\scripts\plugins\ai-ddp-planning-update.ps1"
```

If PowerShell refuses with a message that running scripts is disabled or that the file is not digitally signed, run it for this one time with the policy bypassed:

```powershell
powershell -ExecutionPolicy Bypass -File "<path-to-agentix>\scripts\plugins\ai-ddp-planning-update.ps1"
```

This is common when the Agentix repository is in WSL2 and the script is run from a `\\wsl$\` path.

## After updating

Start a new Claude Code session. A session that was already open keeps the old version. In VS Code, run **Developer: Reload Window** from the Command Palette, then open a new conversation in the Claude panel.

## If nothing updates

- **"Marketplace 'agentix' not found" or "Plugin not found":** the plugin is not installed in this environment or folder. Install it first.
- **"Already up to date" when a change was published:** the plugin's version number was probably not raised when the change was published. The update can treat an unchanged version as nothing new, so the plugin's `version` in `.claude-plugin/plugin.json` should be increased with every release.
