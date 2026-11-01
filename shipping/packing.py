"""
A deterministic, heuristic 3D packing algorithm.

Assumptions:
- Products are rectangular cuboids and may be rotated in any of the 6 axis-aligned
  orientations (no tilting or deformation).
- Products cannot overlap and must remain fully inside the box.
- The algorithm uses a finite set of candidate positions derived from the origin
  and the far faces of already placed items (an extreme-point heuristic).
- This is a practical heuristic, not a proof of globally optimal 3D bin packing.
"""
from dataclasses import dataclass
from decimal import Decimal
from itertools import permutations


@dataclass(frozen=True)
class Item:
    label: str
    length: Decimal
    width: Decimal
    height: Decimal
    weight: Decimal


@dataclass(frozen=True)
class Placement:
    item: Item
    x: Decimal
    y: Decimal
    z: Decimal
    length: Decimal
    width: Decimal
    height: Decimal


def _overlap(a, b):
    return (
        a.x < b.x + b.length and a.x + a.length > b.x
        and a.y < b.y + b.width and a.y + a.width > b.y
        and a.z < b.z + b.height and a.z + a.height > b.z
    )


def pack_items(items, box_length, box_width, box_height):
    """Return placements when the heuristic fits all items, otherwise None."""
    # Largest-volume items first improves the heuristic for common order shapes.
    items = sorted(items, key=lambda i: i.length * i.width * i.height, reverse=True)
    placed = []

    for item in items:
        orientations = sorted(set(permutations((item.length, item.width, item.height))))
        candidates = {(Decimal("0"), Decimal("0"), Decimal("0"))}
        for p in placed:
            candidates.add((p.x + p.length, p.y, p.z))
            candidates.add((p.x, p.y + p.width, p.z))
            candidates.add((p.x, p.y, p.z + p.height))
            candidates.add((p.x + p.length, p.y + p.width, p.z))
            candidates.add((p.x + p.length, p.y, p.z + p.height))
            candidates.add((p.x, p.y + p.width, p.z + p.height))

        chosen = None
        # Prefer low z, then y, then x; orientation order is deterministic.
        for x, y, z in sorted(candidates, key=lambda c: (c[2], c[1], c[0])):
            for length, width, height in orientations:
                if x + length > box_length or y + width > box_width or z + height > box_height:
                    continue
                trial = Placement(item, x, y, z, length, width, height)
                if not any(_overlap(trial, old) for old in placed):
                    chosen = trial
                    break
            if chosen:
                break

        if chosen is None:
            return None
        placed.append(chosen)

    return placed


def recommend_box(order_items, boxes):
    """
    order_items: iterable of (product, quantity)
    boxes: iterable of Box model instances
    Returns (best_box, details). Cheapest eligible box wins; ties use lower
    internal volume and then name. No eligible box returns (None, details).
    """
    expanded = []
    total_weight = Decimal("0")
    for product, quantity in order_items:
        total_weight += product.weight_kg * quantity
        for index in range(quantity):
            expanded.append(Item(
                label=f"{product.name} #{index + 1}",
                length=product.length_cm,
                width=product.width_cm,
                height=product.height_cm,
                weight=product.weight_kg,
            ))

    details = []
    eligible = []
    for box in boxes:
        reasons = []
        if total_weight > box.max_weight_kg:
            reasons.append(
                f"Total order weight ({total_weight} kg) exceeds capacity ({box.max_weight_kg} kg)."
            )
        if not reasons:
            placements = pack_items(
                expanded, box.length_cm, box.width_cm, box.height_cm
            )
            if placements is None:
                reasons.append("Items could not be packed within the internal dimensions.")
            else:
                eligible.append((box, placements))
        details.append({"box": box, "eligible": not reasons, "reasons": reasons})

    if not eligible:
        return None, details

    eligible.sort(key=lambda pair: (
        pair[0].cost,
        pair[0].length_cm * pair[0].width_cm * pair[0].height_cm,
        pair[0].name.lower(),
    ))
    return eligible[0][0], details
