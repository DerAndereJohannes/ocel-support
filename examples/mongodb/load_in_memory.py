from examples.mongodb import log_generation


def execute_script():
    events = {}
    objects = {}
    while True:
        eve, objs = log_generation.generate_events_objects()
        for ev in eve:
            events[ev["ocel:id"]] = ev
        for obj in objs:
            objects[obj["ocel:id"]] = obj
        print(len(events))


if __name__ == "__main__":
    execute_script()
