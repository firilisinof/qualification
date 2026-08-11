# Qualification

This is the repository for my qualification project. It holds the source code for the document and the presentation.

# Where to find more information

In order:

- The `artifacts/` directory.
- The `experimental-artifacts` repository.
    - Local repository at `/Users/lucas/Documents/`.
    - Remote repository at `https://github.com/Lucas-Doctorate-Project/experimental-artifacts`.
- The `/Users/lucas/Documents/` directory.

# Bibliography pipeline

References are managed in Zotero, not in the .bib file. Never hand-edit bibliografia.bib, it is exported from Zotero and manual edits will be lost.

To add a reference:
1. Search the Zotero library for the item (zotero_search_items). If it is missing, add it via zotero_add_item, preferring a DOI as the source.
2. Put the item in the "Thesis" collection (key 6BM2B46K).
3. bibliografia.bib is exported from that collection with Better BibTeX. After the export, check the generated citation key in bibliografia.bib before citing it (pattern: lowercase author + year + Capitalized first title word, e.g. casanova2014Versatile).

If the Zotero MCP server is in local-only mode, writes fail. Report the missing items to me instead of editing the .bib file directly.