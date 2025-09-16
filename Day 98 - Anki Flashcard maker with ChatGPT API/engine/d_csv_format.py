import pandas as pd


def save_to_csv(results, save_path):
    cards = "\n\n".join(results).split("\n\n")
    flashcard_df = (pd.DataFrame([c.split(";", 1) for c in cards], columns=["front", "note"]))
    flashcard_df.to_csv(save_path)

