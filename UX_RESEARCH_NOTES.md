# UX Insights for Overlord Search & Ingestion

## Ingestion Friction Points
- **The "Wait" Problem:** Designers hate waiting for uploads. 
    - *Solution:* Implement local-first indexing. Show the file in the UI immediately using a temporary local path while the AI processes in the background.
- **Tag Overload:** Too many tags make a UI messy.
    - *Solution:* Use "Ghost Tags" (searchable but invisible until the user clicks 'Details').

## Semantic Search Breakthroughs
- **Natural Language over Booleans:** Freelancers don't use `AND` / `OR` logic. They use descriptive language.
    - *Example:* Instead of `blue + texture`, they search for `cracked blue paint background`. 
- **The "I'll know it when I see it" behavior:**
    - *Feature:* Implement a "Scrubbable Timeline" search. If they remember they downloaded it "last Tuesday when it was raining," they should be able to filter by temporal context.

## Success Metrics (KPIs)
1. **Time to Find:** Reduce average search time from 120 seconds (manual folder digging) to <5 seconds.
2. **Zero-Result Rate:** Aim for <2% zero-result queries by utilizing semantic fallback (showing "related" items even if exact matches aren't found).