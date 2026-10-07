# Automate your search for investment gems

Suggestion-only screen for a small synthetic universe of equities, midstream, LNG, and a power name. A watchlist item is not an order, a price target, or a commodity position.

The crew has three seats: quality, commodity link, and invalidation. The hurdle runs locally, so the evidence does not depend on an API key. If CrewAI is installed, `crewai_agents()` returns the same seats for a live run.

## What it does not do

- It does not place a trade or call a broker.
- It does not claim the scores are forecasts.
- Stale filings and weak stories are rejected, not averaged away.

## Run

```bash
python -m pytest
```

Related: [capital-markets-research-desk](https://github.com/TAM-DS/capital-markets-research-desk) writes the memo. [paper-trading-floor](https://github.com/TAM-DS/paper-trading-floor) is the only paper fill path, and it does not read this watchlist as an order.
