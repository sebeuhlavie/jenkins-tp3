import pytest

from app.history import History

pytestmark = pytest.mark.integration


def test_record_and_read_back(tmp_path):
    db_file = tmp_path / "history.db"

    history = History(str(db_file))
    history.record("1+1", 2.0)
    history.record("2*3", 6.0)
    history.close()

    reopened = History(str(db_file))
    assert reopened.all() == [("1+1", 2.0), ("2*3", 6.0)]
    reopened.close()