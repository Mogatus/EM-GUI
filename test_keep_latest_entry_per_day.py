import pytest

from DBFunctions import keep_latest_entry_per_day


def test_none_is_returned_unchanged():
    assert keep_latest_entry_per_day(None) is None

def test_empty_list_and_tuple_keep_type():
    assert keep_latest_entry_per_day([]) == []
    assert keep_latest_entry_per_day(()) == ()

def test_keeps_latest_row_per_day():
    data = [
        (1, 0, 0, 0, 0, "2026-04-03 08:00:00"),
        (2, 0, 0, 0, 0, "2026-04-03 12:00:00"),
        (3, 0, 0, 0, 0, "2026-04-04 09:00:00"),
        (4, 0, 0, 0, 0, "2026-04-04 07:00:00"),
    ]

    result = keep_latest_entry_per_day(data, timestamp_index=5)

    assert result == [
        (2, 0, 0, 0, 0, "2026-04-03 12:00:00"),
        (3, 0, 0, 0, 0, "2026-04-04 09:00:00"),
    ]

def test_tuple_input_returns_tuple():
    data = (
        (1, "2026-04-03 08:00:00"),
        (2, "2026-04-03 10:00:00"),
        (3, "2026-04-04 09:00:00"),
    )

    result = keep_latest_entry_per_day(data, timestamp_index=1)

    assert isinstance(result, tuple)
    assert result[0] == (2, "2026-04-03 10:00:00")
    assert result[1] == (3, "2026-04-04 09:00:00")

def test_same_timestamp_keeps_last_occurrence():
    data = [
        (10, "2026-04-03 12:00:00"),
        (11, "2026-04-03 12:00:00"),
    ]

    result = keep_latest_entry_per_day(data, timestamp_index=1)

    assert result == [(11, "2026-04-03 12:00:00")]

def test_invalid_data_type_raises_type_error():
    with pytest.raises(TypeError):
        keep_latest_entry_per_day({"a": 1})


