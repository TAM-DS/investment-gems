"""Fixture universe. Figures are synthetic and are not prices to trade."""

UNIVERSE = [
    {"ticker": "NGRD", "name": "Nova Grid", "book": "us-equities", "quality": 78, "stretch": 22, "as_of": "2026-10-01", "note": "Contracted backlog, no live quote."},
    {"ticker": "HLNG", "name": "Harbor LNG", "book": "commodity-linked", "quality": 74, "stretch": 18, "as_of": "2026-10-01", "note": "Gas-linked cash flow. Henry Hub is a separate fixture."},
    {"ticker": "PPIPE", "name": "Prairie Pipe", "book": "commodity-linked", "quality": 70, "stretch": 15, "as_of": "2026-10-01", "note": "Midstream volume, not a commodity position."},
    {"ticker": "ERUT", "name": "ERCOT Utility", "book": "power", "quality": 64, "stretch": 28, "as_of": "2026-10-01", "note": "Power exposure. Hub price is not the equity."},
    {"ticker": "STALE", "name": "Old Chemical", "book": "us-equities", "quality": 80, "stretch": 10, "as_of": "2026-01-15", "note": "Stale filing. Do not promote."},
    {"ticker": "MEME", "name": "Headline Metals", "book": "commodity-linked", "quality": 40, "stretch": 55, "as_of": "2026-10-01", "note": "Story without a filing fact."},
]
