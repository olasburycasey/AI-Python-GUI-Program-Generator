import google.generativeai as genai

with open("API_KEY", "r") as f:
    api_key = f.read()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

intent_actions = {
    "add_button": lambda label: print(f"Adding button with label: {label}"),
    "set_title": lambda title: print(f"Setting title: {title}")
}


def interpret_intent(user_input):
    prompt = f"""
You are a GUI code assistant. Your job is to extract the user's intent and parameters from natural language.

Available actions:
- add_button(label: string)
- set_title(title: string)

Respond in JSON like:
{{
  "intent": "add_button",
  "parameters": {{
    "label": "Submit"
  }}
}}

User input: "{user_input}"
"""

    response = model.generate_content(prompt)
    try:
        parsed = eval(response.text)  # Can replace with json.loads if output is valid JSON
        return parsed
    except Exception as e:
        print("Failed to parse response:", response.text)
        return None


def handle_user_input(user_input):
    result = interpret_intent(user_input)
    if result:
        intent = result["intent"]
        params = result["parameters"]
        if intent in intent_actions:
            intent_actions[intent](**params)
        else:
            print("Unknown intent:", intent)
    else:
        print("Could not understand input.")


handle_user_input("Add a button that says Submit")
handle_user_input("Set the title to My Cool App")
