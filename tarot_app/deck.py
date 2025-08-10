import json
import random
from typing import Any, Dict


class Deck:
    """Load and draw cards from a Tarot deck."""

    def __init__(self, cards: Dict[str, Dict[str, Any]]):
        self.cards = cards

    @classmethod
    def from_json(cls, path: str) -> "Deck":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(data)

    def draw(self) -> Dict[str, Any]:
        """Draw a random card with orientation and details."""
        name = random.choice(list(self.cards.keys()))
        orientation = random.choice(["upright", "reversed"])
        card_data = self.cards[name]
        return {
            "name": name,
            "orientation": orientation,
            "keywords": card_data[orientation],
            "summary": card_data.get("summary", ""),
            "actions": card_data.get("actions", []),
            "mantra": card_data.get("mantra", ""),
        }
