import random
import typing


def gen_event() -> typing.Generator:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "use", "release"
    ]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(event_list: list) -> typing.Generator:
    while event_list:
        idx = random.randrange(len(event_list))
        event = event_list.pop(idx)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    event_list = []
    stream = gen_event()
    for _ in range(10):
        event_list.append(next(stream))

    print(f"Built list of 10 events: {event_list}")

    consumer = consume_event(event_list)
    for event in consumer:
        name, action = event
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
