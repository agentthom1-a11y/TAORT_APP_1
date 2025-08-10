import os
from .deck import Deck


def main() -> None:
    deck_path = os.path.join(os.path.dirname(__file__), "..", "deck_rws.json")
    deck_path = os.path.abspath(deck_path)
    deck = Deck.from_json(deck_path)
    input("When you're ready, press Enter to draw a card...")
    card = deck.draw()
    print(f"You drew {card['name']} ({card['orientation']}).")
    print("Keywords:", ", ".join(card["keywords"]))
    if card["summary"]:
        print("Summary:", card["summary"])
    if card["actions"]:
        print("Actions:")
        for action in card["actions"]:
            print("-", action)
    if card["mantra"]:
        print("Mantra:", card["mantra"])


if __name__ == "__main__":
    main()
