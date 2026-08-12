# Contributing

## One entry is one app, not one server

This is the thing to get right. The unit is a `ui://` resource and the tool that
opens it. A server shipping three UI resources becomes three entries that share a
`server` block, because someone browsing this list wants a chart or a form, not a
repository.

So `id` and `name` describe the app (`firebase-init-ui`, "Firebase Init UI"), and the
repo goes in `server.repo_url`. Two entries may share a `server.repo_url`. What must
be unique is the pair of repo and `ui_resource`.

## Adding an app

1. Copy `templates/app.template.json` to `apps/<your-id>.json`. The `id` must match
   the filename.
2. Fill it in.
3. `make install && make verify`
4. Open a pull request.

One file per app, so your pull request will not conflict with anyone else's.

If a UI does not render out of the box, say so in `availability`, for example
`behind experiment flag: mcpapps`. It shows in the list as ⚑ and saves the next
person wondering why nothing appeared.

## Be accurate about verification

`verification.status` is one of:

| Status | Use it when |
| --- | --- |
| `probed` | You connected to the server and saw the `ui://` resource served with mimeType `text/html;profile=mcp-app`. Requires `evidence`. |
| `source-inspected` | You read the source and found the resource declaration and a tool with `_meta.ui.resourceUri`. |
| `claimed` | The README says so and you have not checked. |

`claimed` is a perfectly good answer. An honest `claimed` is worth more here than an
optimistic `probed`, and the whole point of this list is that the difference is
visible.

## What does not belong

SDKs and frameworks that implement the extension, hosts and clients that render apps,
tutorial and course repositories, and forks of any of the above.

`ui://` on its own is not evidence. FairyGUI uses the same scheme for Unity UI
packages, and OpenAI's widget protocol uses it alongside `openai/outputTemplate`.
What identifies an MCP App is the mimeType plus the `_meta.ui.resourceUri` linkage.

## Generated files

`README.md` and `apps.json` are built from `apps/`. Do not edit them. CI fails if they
are stale, so run `make build` and commit the result.
