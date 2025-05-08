import re


def get_game_type(model, game):
    prompt = f"Give me a list of versions of the game {game}"
    response = model.generate_content(prompt)
    text = response.text
    split_text = text.splitlines()

    game_list = []

    for line in split_text:
        match = re.match(r"^\*\s+\*\*(.+?):\*\*", line)
        if match:
            game_name = match.group(1).strip()
            game_list.append(game_name)

    if not game_list:
        return "default"

    for i, version in enumerate(game_list, 1):
        print(f"{i}. {version}")

    print(f"{len(game_list) + 1}. Other")

    user_input = input("Which version would you like? Enter name, number, or 'other': ").strip()

    # Try to interpret input as number
    if user_input.isdigit():
        index = int(user_input) - 1
        if 0 <= index < len(game_list):
            return game_list[index]
        elif index == len(game_list):
            other_option = input("Please type the other version: ").strip()
            return other_option
    elif user_input.lower() == "other":
        other_option = input("Please type the other version: ").strip()
        return other_option
    else:
        # Match by name (case-insensitive)
        for version in game_list:
            if user_input.lower() == version.lower():
                return version

    print("Invalid input. Using default option.")
    return "default"
