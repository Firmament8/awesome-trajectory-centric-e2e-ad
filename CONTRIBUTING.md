# Contributing

Thanks for helping keep this literature list useful and accurate.

## Accuracy Rules

- Do not add guessed project pages, code repositories, datasets, or leaderboards.
- Prefer links from the paper PDF, author homepage, official project page, conference page, DOI page, arXiv page, or official organization repository.
- If a paper has no verified direct link, keep a Scholar search link or leave the direct-link field empty.
- Keep titles, authors, years, and venues consistent with the BibTeX source unless you are correcting a clear metadata error.

## Suggested Entry Fields

For new papers, update `bibliography/references.bib` first. Then regenerate:

```bash
python tools/generate_papers.py
```

Optional verified links can be tracked in a future `papers/links.tsv` file using these fields:

```text
bib_key	code_url	project_url,dataset_url,notes,verified_source
```

## Scope

Relevant topics include trajectory-centric end-to-end autonomous driving, planning-oriented evaluation, NAVSIM-style protocols, BEV and occupancy representations, VLM/VLA driving systems, world models, rollout-based planning, generative simulation, and related benchmarks.
