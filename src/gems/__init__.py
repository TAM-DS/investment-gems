"""Suggestion crew. CrewAI is optional. The decision rule is local."""

from __future__ import annotations

from gems.universe import UNIVERSE

FRESH = "2026-09-01"


def _score(row: dict) -> int:
    return row["quality"] - row["stretch"]


def screen(limit: int = 3) -> dict:
    ranked = []
    for row in UNIVERSE:
        item = {**row, "score": _score(row), "action": "watch"}
        if row["as_of"] < FRESH:
            item["status"] = "rejected"
            item["reason"] = "stale-filing"
        elif item["score"] < 45:
            item["status"] = "rejected"
            item["reason"] = "below-hurdle"
        else:
            item["status"] = "suggestion"
            item["reason"] = "cleared-local-hurdle"
            item["invalidation"] = "Drop if the next filing misses the fixture fact or the as-of date goes stale."
        ranked.append(item)
    ranked.sort(key=lambda row: row["score"], reverse=True)
    suggestions = [row for row in ranked if row["status"] == "suggestion"][:limit]
    return {
        "title": "Automate your search for investment gems",
        "order_authority": False,
        "suggestions": suggestions,
        "rejected": [row for row in ranked if row["status"] == "rejected"],
    }


def crewai_agents():
    """Return CrewAI agents when the package is installed. Tests do not require it."""
    try:
        from crewai import Agent
    except ImportError:
        return None
    return [
        Agent(role="Quality analyst", goal="Score filing quality", backstory="Suggestion only."),
        Agent(role="Commodity linker", goal="Separate the equity from the commodity", backstory="No order path."),
        Agent(role="Invalidation editor", goal="State what would kill the idea", backstory="No price target."),
    ]
