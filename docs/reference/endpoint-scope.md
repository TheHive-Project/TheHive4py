# Endpoint Scope

`thehive4py` intentionally exposes the parts of TheHive's API that are useful for
automation, integrations, and backend workflows. Some documented TheHive routes are
browser-oriented or duplicate an existing library method with different response
semantics, so they are intentionally kept out of the public client surface.

## Browser-only endpoints that are intentionally excluded

The following routes should not be added to `thehive4py` as direct endpoint methods:

- `POST /api/v1/user/{id}/attachment/temporary`
  Creates temporary draft attachments for the web UI while a user is editing content.
  It is not part of a stable automation workflow.
- `GET /api/v1/user/{id}/avatar/{hash}`
  Returns avatar content for browser display. It is UI-oriented rather than
  integration-oriented.
- `POST /api/v1/user/{id}/login/set`
  Changes a user's login. This is an administrative UI operation that is intentionally
  not part of the client surface.
- `GET /api/v1/attachment/{id}`
  Serves attachment content for inline browser rendering. Library consumers should use
  `organisation.download_attachment()` instead, which models the file download
  workflow explicitly.

## How to decide whether a new route belongs in the client

Before adding a new endpoint wrapper, prefer the route when it satisfies all of the
following:

- It supports automation or backend integrations.
- It has stable request and response semantics outside the browser.
- It is not only a UI convenience wrapper around another supported route.

If a route is primarily meant for browser rendering or transient editing workflows,
document the rationale instead of adding it to `thehive4py`.
