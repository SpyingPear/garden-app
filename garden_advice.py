"""
Garden Advice — quick CLI

Small script for a Git/GitHub workflow task.
Asks for a season + plant type and prints a short, friendly tip.

Notes:
- Keep I/O in main(); keep logic in get_advice() so it’s easy to test later.
- Inputs are case/space agnostic; unknown values get a polite fallback.
- Mappings live near the top so the tips are easy to tweak later.

Author: S. Minty
Date: 2025-08-31
"""
from typing import Dict

# Tip texts live here; tweak wording here rather than inside logic.
SEASON_ADVICE: Dict[str, str] = {
    "summer": "Water a bit more often and give delicate plants some afternoon shade.",
    "winter": "Protect from frost (old sheets/row covers) and avoid waterlogging.",
    "spring": "Light mulch helps keep moisture; start a mild feed as growth kicks off.",
    "autumn": "Ease off the watering; collect leaves for compost and protect tender stems.",
}

PLANT_ADVICE: Dict[str, str] = {
    "flower": "Pinch back spent blooms to encourage more flowers.",
    "vegetable": "Watch for pests; regular checks beat heavy sprays later.",
    "succulent": "Less is more—water deeply but infrequently; ensure sharp drainage.",
    # TODO: consider adding "herb" with a short pruning tip.
}


def _normalise(s: str) -> str:
    """Lowercase + trim. Avoids repeating .strip().lower() everywhere."""
    return (s or "").strip().lower()


def get_advice(season: str, plant_type: str) -> str:
    """
    Build an advice message for the given season and plant type.
    Unknown values get a friendly fallback so the CLI never crashes.
    """
    season_key = _normalise(season)
    plant_key = _normalise(plant_type)

    lines = []
    lines.append(SEASON_ADVICE.get(season_key, "No season-specific tip yet—add one in SEASON_ADVICE."))
    lines.append(PLANT_ADVICE.get(plant_key, "No plant-type tip yet—add one in PLANT_ADVICE."))
    return "\n".join(lines)


def main() -> None:
    try:
        season = input("Season (summer/winter/spring/autumn): ")
        plant_type = input("Plant type (flower/vegetable/succulent): ")
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        return

    # Single print keeps the CLI output tidy.
    print(get_advice(season, plant_type))


if __name__ == "__main__":
    main()
