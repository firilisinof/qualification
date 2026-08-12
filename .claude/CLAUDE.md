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
2. Put the item in the "Thesis" collection.

What happens after:

1. bibliografia.bib is manually exported from that collection with Better BibTeX.
2. The generated citation key pattern is `lowercase author + year + capitalized first title word` (e.g., casanova2014Versatile). The citation key can have a letter appended in the end of the word (e.g., casanova2014Versatilea) if the library contains more references clashing he citation key.

If the Zotero MCP server is in local-only mode, writes fail. Report the missing items to me instead of editing the .bib file directly.

# Others

You'll find `% TODO:` commentaries along the files. I'll tell you when to handle each TODO, but you can solve them if they match the current task. You can also add TODO for later.