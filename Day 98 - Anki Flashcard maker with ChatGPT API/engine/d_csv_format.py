import pandas as pd


def save_to_csv(results, save_path):
    raw_cards_list = "\n".join(results).split("\n")
    strip_cards_list = [card.strip() for card in raw_cards_list if card.strip()]
    dirty_flashcard_df = (pd.DataFrame([c.split(";", 1) for c in strip_cards_list], columns=["front", "note"]))
    clean_flashcard_df = dirty_flashcard_df.reset_index(drop='index')
    clean_flashcard_df.to_csv(save_path, index=False)

