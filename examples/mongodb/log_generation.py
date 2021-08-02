from random import randrange
import datetime
import random
import uuid


def generate_events_objects():
    orders = ["O"+str(uuid.uuid4()) for i in range(randrange(5000, 15000))]
    resb = ["R"+str(uuid.uuid4()) for i in range(randrange(5000, 15000))]
    invoices = ["I"+str(uuid.uuid4()) for i in range(randrange(5000, 15000))]
    payments = ["P"+str(uuid.uuid4()) for i in range(randrange(5000, 15000))]
    payments1 = []
    payments2 = []
    payments3 = []
    for p in payments:
        r = random.random()
        if r <= 0.4:
            payments1.append(p)
        elif r <= 0.75:
            payments2.append(p)
        else:
            payments3.append(p)
    payments124 = sorted(list(set(payments1).union(set(payments2))))
    list_events = []
    list_objects = []
    count = 0
    for o in orders:
        all_objects = [o]
        event_id = "EV"+str(uuid.uuid4())
        all_obj_w_vmap = [x+"_"+event_id for x in all_objects]
        rec = {"ocel:id": event_id, "ocel:activity": "Create document (EKKO)", "ocel:timestamp": datetime.datetime.fromtimestamp(1000000 + count), "ocel:omap": all_objects, "ocel:vmap": {}, "ocel:omapWId": all_obj_w_vmap}
        list_events.append(rec)
        count = count + 1
        list_objects.append({"ocel:id": o, "ocel:type": "EBELN-EBELN", "ocel:vmap": {}})
    for rr in resb:
        order_items = {orders[randrange(0, len(orders))]}
        r = random.random()
        while r > 0.8:
            order_items.add(orders[randrange(0, len(orders))])
            r = random.random()
        all_objects = [rr] + list(order_items)
        event_id = "EV"+str(uuid.uuid4())
        all_obj_w_vmap = [x+"_"+event_id for x in all_objects]
        rec = {"ocel:id": event_id, "ocel:activity": "Create document (RESB)", "ocel:timestamp": datetime.datetime.fromtimestamp(1000000 + count), "ocel:omap": all_objects, "ocel:vmap": {}, "ocel:omapWId": all_obj_w_vmap}
        list_events.append(rec)
        count = count + 1
        list_objects.append({"ocel:id": rr, "ocel:type": "RSNUM-RSNUM", "ocel:vmap": {}})
    for i in invoices:
        order_items = {orders[randrange(0, len(orders))]}
        r = random.random()
        while r > 0.8:
            order_items.add(orders[randrange(0, len(orders))])
            r = random.random()
        all_objects = [i] + list(order_items)
        event_id = "EV"+str(uuid.uuid4())
        all_obj_w_vmap = [x+"_"+event_id for x in all_objects]
        rec = {"ocel:id": event_id, "ocel:activity": "Enter incoming invoice", "ocel:timestamp": datetime.datetime.fromtimestamp(1000000 + count), "ocel:omap": all_objects, "ocel:vmap": {}, "ocel:omapWId": all_obj_w_vmap}
        list_events.append(rec)
        count = count + 1
        list_objects.append({"ocel:id": i, "ocel:type": "BELNR-RE_BELNR", "ocel:vmap": {}})
    for p in payments1:
        order_items = {orders[randrange(0, len(orders))]}
        r = random.random()
        while r > 0.8:
            order_items.add(orders[randrange(0, len(orders))])
            r = random.random()
        r = random.random()
        invoice_items = {invoices[randrange(0, len(invoices))]}
        while r > 0.8:
            invoice_items.add(invoices[randrange(0, len(invoices))])
            r = random.random()
        all_objects = [p] + list(order_items)
        event_id = "EV"+str(uuid.uuid4())
        all_obj_w_vmap = [x+"_"+event_id for x in all_objects]
        rec = {"ocel:id": event_id, "ocel:activity": "Vendor invoice posting", "ocel:timestamp": datetime.datetime.fromtimestamp(1000000 + count), "ocel:omap": all_objects, "ocel:vmap": {}, "ocel:omapWId": all_obj_w_vmap}
        list_events.append(rec)
        count = count + 1
        list_objects.append({"ocel:id": p, "ocel:type": "BELNR-BELNR_D", "ocel:vmap": {}})
        r = random.random()
        if r > 0.8:
            all_objects = [p+"R"] + list(order_items)
            event_id = "EV" + str(uuid.uuid4())
            all_obj_w_vmap = [x + "_" + event_id for x in all_objects]
            rec = {"ocel:id": event_id, "ocel:activity": "Revert Document",
                   "ocel:timestamp": datetime.datetime.fromtimestamp(1000000 + count), "ocel:omap": all_objects, "ocel:vmap": {}, "ocel:omapWId": all_obj_w_vmap}
            list_objects.append({"ocel:id": p+"R", "ocel:type": "BELNR-BELNR_D", "ocel:vmap": {}})
            list_events.append(rec)
            count = count + 1
    for p in payments2:
        order_items = {orders[randrange(0, len(orders))]}
        r = random.random()
        while r > 0.8:
            order_items.add(orders[randrange(0, len(orders))])
            r = random.random()
        all_objects = [p] + list(order_items)
        event_id = "EV"+str(uuid.uuid4())
        all_obj_w_vmap = [x + "_" + event_id for x in all_objects]
        rec = {"ocel:id": event_id, "ocel:activity": "Post Outgoing Payment", "ocel:timestamp": datetime.datetime.fromtimestamp(1000000 + count), "ocel:omap": all_objects, "ocel:vmap": {}, "ocel:omapWId": all_obj_w_vmap}
        list_events.append(rec)
        count = count + 1
        list_objects.append({"ocel:id": p, "ocel:type": "BELNR-BELNR_D", "ocel:vmap": {}})
    for p in payments3:
        all_objects = [p]
        event_id = "EV"+str(uuid.uuid4())
        all_obj_w_vmap = [x + "_" + event_id for x in all_objects]
        rec = {"ocel:id": event_id, "ocel:activity": "Enter Incoming Payment", "ocel:timestamp": datetime.datetime.fromtimestamp(1000000 + count), "ocel:vmap": {}, "ocel:omapWId": all_obj_w_vmap}
        list_events.append(rec)
        count = count + 1
        list_objects.append({"ocel:id": p, "ocel:type": "BELNR-BELNR_D", "ocel:vmap": {}})
    return list_events, list_objects


if __name__ == "__main__":
    list_events, list_objects = generate_events_objects()
    print(len(list_events))
    print(len(list_objects))
