from kvstore_lib.network import Network
from kvstore_lib.message import Message
from collections import deque
import asyncio
import logging

EMPTY_OBJECT = object()


def test_network():
    n1 = Network(1)
    n2 = Network(2)
    n3 = Network(3)

    assert (n1.inbox == deque())
    assert (n2.inbox == deque())
    assert (n3.inbox == deque())

    n1.send(2, Message(1, 2, EMPTY_OBJECT))
    n1.send(3, Message(1, 3, EMPTY_OBJECT))
    n2.send(3, Message(2, 3, EMPTY_OBJECT))

    logging.warning(n2.inbox)
    logging.warning(n3.inbox)

    assert (n2.recv() == (1, Message(1, 2, EMPTY_OBJECT)))
    assert (n3.recv() == (1, Message(1, 3, EMPTY_OBJECT)))
    assert (n3.recv() == (2, Message(2, 3, EMPTY_OBJECT)))
    assert (n2.inbox == deque())
    assert (n3.inbox == deque())

    async def send_to_one():
        await asyncio.sleep(0.5)
        n2.send(1, Message(2, 1, EMPTY_OBJECT))

    logging.warning("sending message... (arriving in 0.5 secs)")
    asyncio.run(send_to_one())
    assert (n1.recv() == (2, Message(2, 1, EMPTY_OBJECT)))  # should block for 5 seconds
