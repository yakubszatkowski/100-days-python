import pandas as pd
from test import output


def save_to_csv(save_path):
    cards = "\n\n".join(output).split("\n\n")
    flashcard_df = (pd.DataFrame([c.split(";", 1) for c in cards], columns=["front", "note"]))
    flashcard_df.to_csv(save_path)

