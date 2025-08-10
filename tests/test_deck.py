import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tarot_app.deck import Deck


def test_draw_returns_card():
    deck_path = os.path.join(os.path.dirname(__file__), "..", "deck_rws.json")
    deck_path = os.path.abspath(deck_path)
    deck = Deck.from_json(deck_path)
    card = deck.draw()
    assert card["name"] in deck.cards
    assert card["orientation"] in ("upright", "reversed")
    assert isinstance(card["keywords"], list)
