# MCP Apps

A verified directory of MCP servers that ship an interactive UI.

### → Browse it at **[mcpapps.page](https://mcpapps.page)**

Only servers implementing the
[MCP Apps extension](https://modelcontextprotocol.io/extensions/apps/overview)
(SEP-1865). Every entry records how it was checked, and when.

**23 apps** across 19 servers. ✅ 1 probed, 🔍 22 source-inspected

## What qualifies

One entry is one **app**, not one server. A server shipping three UI resources
appears as three entries, because you are looking for a chart or a form, not for a
repository.

An app qualifies when both are true:

1. Its server declares a resource with a `ui://` URI and mimeType `text/html;profile=mcp-app`
2. A tool carries `_meta.ui.resourceUri` pointing at that resource

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

A status is never upgraded without re-running the check. A ⚑ marks an app that needs
something enabled before its UI renders, such as a feature flag.

### Data Visualization

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **Bag of Words Visualization** | View a generated data visualization and adjust how it is drawn. | [bagofwords](https://github.com/bagofwords1/bagofwords) | 🔍<br><sub>2026-08-11</sub> |  |
| **GKE Time-Series Chart** | Plot GKE monitoring metrics as an interactive time-series chart. | [gke-mcp](https://github.com/GoogleCloudPlatform/gke-mcp) | 🔍<br><sub>2026-08-11</sub> |  |
| **Lightdash Chart Renderer** | Render a Lightdash chart inline and explore the underlying data. | [lightdash](https://github.com/lightdash/lightdash) | 🔍<br><sub>2026-08-11</sub> |  |
| **Sidemantic Chart Builder** | Build a chart over a semantic layer and adjust the dimensions interactively. | [sidemantic](https://github.com/sidequery/sidemantic) | 🔍<br><sub>2026-08-11</sub> |  |

### Dashboards

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **Grafana Panel Viewer** | View a Grafana panel inline and change its time range without leaving the chat. | [mcp-grafana](https://github.com/grafana/mcp-grafana) | 🔍<br><sub>2026-08-11</sub> |  |

### Maps and Geo

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **Mapbox Map Viewer** | Pan and zoom a Mapbox map rendered inline, with a fullscreen toggle. | [mapbox-mcp-server](https://github.com/mapbox/mcp-server) | 🔍<br><sub>2026-08-11</sub> |  |
| **Mapbox Style Preview** | Preview a Mapbox style on a live map while editing it. | [mapbox-mcp-devkit-server](https://github.com/mapbox/mcp-devkit-server) | 🔍<br><sub>2026-08-11</sub> |  |

### Forms and Workflows

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **Data Factory Connection Form** | Create an Azure Data Factory connection through a form with validation. | [DataFactory.MCP](https://github.com/microsoft/DataFactory.MCP) | 🔍<br><sub>2026-08-11</sub> |  |
| **Firebase Deploy UI**<br><sub>⚑ behind experiment flag: mcpapps</sub> | Pick deploy targets and watch a Firebase deploy run from a panel in the chat. | [firebase-tools](https://github.com/firebase/firebase-tools) | 🔍<br><sub>2026-08-11</sub> |  |
| **Firebase Environment Editor**<br><sub>⚑ behind experiment flag: mcpapps</sub> | Edit Firebase environment variables in a form rather than one CLI call at a time. | [firebase-tools](https://github.com/firebase/firebase-tools) | 🔍<br><sub>2026-08-11</sub> |  |
| **Firebase Init UI**<br><sub>⚑ behind experiment flag: mcpapps</sub> | Set up a Firebase project through a visual form instead of answering CLI prompts. | [firebase-tools](https://github.com/firebase/firebase-tools) | 🔍<br><sub>2026-08-11</sub> |  |
| **GitHub Issue Composer** | Compose and edit a GitHub issue in a form before it is created. | [github-mcp-server](https://github.com/github/github-mcp-server) | 🔍<br><sub>2026-08-11</sub> |  |
| **GKE Dropdown Selector** | Choose a GKE cluster or resource from a dropdown instead of typing its name. | [gke-mcp](https://github.com/GoogleCloudPlatform/gke-mcp) | 🔍<br><sub>2026-08-11</sub> |  |
| **OpenRecord Setup** | Connect OpenRecord to your account through a setup form in the chat. | [openrecord](https://github.com/Fan-Pier-Labs/openrecord) | 🔍<br><sub>2026-08-11</sub> |  |

### Media

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **Blog2Video Setup Gallery** | Pick visual styles for a generated video from a gallery of options. | [blog2video](https://github.com/FireBird-Technologies/blog2video) | 🔍<br><sub>2026-08-11</sub> |  |
| **Sheet Music Viewer** | Render generated music as sheet music and play it back. | [mcp-music-studio](https://github.com/linxule/mcp-music-studio) | 🔍<br><sub>2026-08-11</sub> |  |
| **PDF Form Viewer** | Open a PDF and fill its form fields inline. | [PDF-Tools](https://github.com/Open-Document-Alliance/PDF-Tools) | 🔍<br><sub>2026-08-11</sub> |  |
| **Quran Mushaf Reader** | Read the Mushaf with page navigation rendered inline. | [quran-mcp](https://github.com/quran/quran-mcp) | 🔍<br><sub>2026-08-11</sub> |  |

### Productivity

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **Bag of Words Artifact Editor** | Edit a generated analysis artifact in place instead of regenerating it. | [bagofwords](https://github.com/bagofwords1/bagofwords) | 🔍<br><sub>2026-08-11</sub> |  |

### Finance

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **Receipt Matcher** | Match receipts to transactions by dragging them onto the right entry. | [gnubok](https://github.com/erp-mafia/gnubok) | 🔍<br><sub>2026-08-11</sub> |  |

### Science

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **FutureSearch Session View** | Follow a FutureSearch forecasting session as it runs. | [futuresearch-mcp](https://github.com/futuresearch/futuresearch-python) | 🔍<br><sub>2026-08-11</sub> |  |
| **nteract Notebook Output** | View rich notebook cell output rendered inline in the conversation. | [nteract](https://github.com/nteract/nteract) | 🔍<br><sub>2026-08-11</sub> |  |

### Other

| App | What it does | Server | Checked | Media |
| --- | --- | --- | :---: | --- |
| **FineRx Card Prices** | See dated card prices for a medicine at each US pharmacy chain, find nearby pharmacies, and show the free discount card at the counter. | [finerx-mcp](https://github.com/andrewfinerx/finerx-mcp) | ✅<br><sub>2026-11-24</sub> |  |


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

[mcpapps.page](https://mcpapps.page) is built from this file, so anything merged
here appears there on the next deploy.

## Support

Every entry here is checked by hand before it is listed. If that saved you time,
you can [buy me a coffee](https://buymeacoffee.com/kadoud).

MIT licensed.
