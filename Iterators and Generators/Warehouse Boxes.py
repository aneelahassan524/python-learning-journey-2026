def warehouse_boxes():
    for box in range(1,21):
        yield box

boxes = warehouse_boxes()
print(f"BOX-00{next(boxes)}")
print(f"BOX-00{next(boxes)}")
print(f"BOX-00{next(boxes)}")
print(f"BOX-00{next(boxes)}")
print(f"BOX-00{next(boxes)}")
print(f"BOX-00{next(boxes)}")
print(f"BOX-00{next(boxes)}")
print(f"BOX-00{next(boxes)}")
print(f"BOX-00{next(boxes)}")

    