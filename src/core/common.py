import uuid


def uuid4():
    return str(uuid.uuid4())


def generate_uuid4(size: int):
    for i in range(size):
        yield uuid4()
