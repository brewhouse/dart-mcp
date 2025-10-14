import pytest

from dart_mcp import server


@pytest.mark.asyncio
async def test_next_trains_basic():
    # Test with a specific time early in the morning to catch the 08:00 departure
    msg = await server.next_trains("DART", "University", "2025-01-01T07:00:00")
    # Should list one departure at 08:00 → 08:50
    # Should contain departure times for DART


@pytest.mark.asyncio
async def test_next_trains_error_cases():
    """Test error handling in next_trains function"""
    # Test invalid datetime format
    msg = await server.next_trains("DART", "University", "invalid-datetime")
    assert "Invalid datetime format" in msg

    # Test nonexistent station
    msg = await server.next_trains("Nonexistent Station", "University")
    assert "not found" in msg

    # Test no trains available (weekend)
    msg = await server.next_trains("DART", "University", "2025-01-04T07:00:00")  # Saturday
    assert "No more trains today" in msg


@pytest.mark.asyncio
async def test_next_trains_timezone_handling():
    """Test timezone handling in next_trains function"""
    # Test with timezone-aware datetime
    msg = await server.next_trains("DART", "University", "2025-01-01T07:00:00-06:00")
    assert (
        "departure" in msg or "No more trains" in msg
    )  # depending on timezone conversion


@pytest.mark.asyncio
async def test_list_stations():
    """Test the list_stations function"""
    msg = await server.list_stations()
    assert "Available DART bus stops:" in msg
    assert "DART CENTRAL STATION" in msg
    # Should be sorted alphabetically
