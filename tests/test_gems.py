from gems import crewai_agents, screen


def test_watchlist_is_not_an_order():
    result = screen()
    assert result["order_authority"] is False
    assert result["suggestions"]
    assert all(row["action"] == "watch" for row in result["suggestions"])
    assert all("invalidation" in row for row in result["suggestions"])


def test_stale_and_weak_names_are_rejected():
    result = screen()
    reasons = {row["ticker"]: row["reason"] for row in result["rejected"]}
    assert reasons["STALE"] == "stale-filing"
    assert reasons["MEME"] == "below-hurdle"


def test_energy_linked_names_can_be_suggested_without_a_commodity_order():
    result = screen()
    books = {row["book"] for row in result["suggestions"]}
    assert "commodity-linked" in books or "power" in books
    assert result["order_authority"] is False


def test_crewai_adapter_is_optional():
    agents = crewai_agents()
    assert agents is None or len(agents) == 3
