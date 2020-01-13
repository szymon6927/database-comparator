from src.core.common import uuid4


def test_uuid4():
    uuid = uuid4()

    assert isinstance(uuid, str)
    assert len(uuid) == 36
