# MCP Apps

A verified directory of MCP servers that ship an interactive UI.

Only servers implementing the
[MCP Apps extension](https://modelcontextprotocol.io/extensions/apps/overview)
(SEP-1865). Every entry records how it was checked, and when.

**{{COUNT}} apps.** {{VERIFICATION_COUNTS}}

## What qualifies

A server belongs here when both are true:

1. It declares a resource with a `ui://` URI and mimeType `text/html;profile=mcp-app`
2. At least one tool carries `_meta.ui.resourceUri` pointing at it

| | |
| --- | --- |
| Extension ID | `io.modelcontextprotocol/ui` |
| Extension spec | `2026-01-26` |
| Core MCP spec | `2026-07-28` |

Two things that trip people up: the extension ID is `/ui`, not `/apps`, despite the
repo being named `ext-apps`. And there is no `type: "app"` field in the protocol.

Not listed: SDKs and frameworks, hosts and clients that render apps, tutorials, and
forks. Note that `ui://` alone does not identify an MCP App, since FairyGUI and
OpenAI's widget protocol both use the same scheme.

## Checked

| | | |
| :---: | --- | --- |
| ✅ | `probed` | A live probe saw the `ui://` resource with the correct mimeType |
| 🔍 | `source-inspected` | A human read the source and confirmed the declaration |
| 📋 | `claimed` | The author says so, nobody has checked |

A status is never upgraded without re-running the check.

{{APPS_TABLE}}

## Contributing

Add one file, `apps/<id>.json`, then run `make verify`. See
[CONTRIBUTING.md](CONTRIBUTING.md).

`README.md` and `apps.json` are generated. Run `make build` rather than editing them.

## Building an MCP App

Start with the official
[examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples),
which include starter templates for React, Vue, Svelte, Preact, Solid, and vanilla
JavaScript. Then the [build guide](https://modelcontextprotocol.io/extensions/apps/build)
and the [spec](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx).

## Data

[`apps.json`](apps.json) is a flat array of every entry, validated against
[`schema/app.schema.json`](schema/app.schema.json).

```
https://raw.githubusercontent.com/khalid-tounoussi-1/mcp-apps/main/apps.json
```

MIT licensed.
