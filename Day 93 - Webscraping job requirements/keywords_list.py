keywords_lower_case = [
    'opportunity', 'develop', 'stable company', 'established position', 'international', 'atmosphere', 
    'team', 'friendly', 'casual', 'close-knit', 'positive energy', 'flexible work environment', 'from home', 
    'remote', 'training', 'courses', 'development programs', 'medical care', 'health benefits', 'well-being', 
    'gym', 'fitness', 'snacks', 'food', 'massage', 'recreation', 'work world programs', 'bonuses', 'stock', 
    'compensation', 'salary', 'in return', 'why work with us', 'enthusiasts', 'location',
    'extremely flexible cooperation', 'convenient', 'devote time', 'part-time', 'contract', 
    'benefits', 'equipment', 'relocation package', 'bonus plan', 'b2b', 'B2B', 'full-time', 'Full-time'
    'szansa', 'rozwój', 'stabilnej firmie', 'ugruntowana pozycja', 'międzynarodowa', 'atmosfera', 'sprzęt',
    'zespół', 'przyjazny', 'swobodny', 'zgrany', 'z domu', 'zdalne', 'szkolenia', 'kursy', 'programy rozwojowe', 
    'opieka medyczna', 'świadczenia zdrowotne', 'relokacyjny', 'b2b', 'B2B', 'zdalnie', 'pełen etat'
    'siłownia', 'przekąski', 'jedzenie', 'masaż', 'rekreacja', 'bonusy', 'wynagrodzenie', 'komunikacja', 
    'w zamian', 'dlaczego warto', 'lokalizacja', 'elastyczna ', 'wygodna', 'poświęć czas', 'pełny etat', 
    'pół etatu', 'umowa', 'benefity'
]

keywords_title_case = [keyword.title() for keyword in keywords_lower_case]

negative_keywords = keywords_lower_case + keywords_title_case
