statements = [
    {
        "text": "If the other party’s position seems very important to him or her, I may sacrifice my own position.",
        "style": "C",
    },
    {
        "text": "I address problems and concerns directly without blame or judgment.",
        "style": "E",
    },
    {
        "text": "I try to win by convincing the other party of the logic and benefits of my position.",
        "style": "B",
    },
    {
        "text": "I tell the other person my ideas for and ask for his or hers in return.",
        "style": "E",
    },
    {"text": "I try to find a compromise solution.", "style": "D"},
    {
        "text": "I try to postpone discussions until I have had some time to think.",
        "style": "A",
    },
    {
        "text": "I see achievement as more important than relational issues.",
        "style": "B",
    },
    {
        "text": "I use body language that might be perceived as condescending or arrogant.",
        "style": "B",
    },
    {
        "text": "Confronting someone about a problem is very uncomfortable for me.",
        "style": "A",
    },
    {"text": "I give up some points in exchange for others.", "style": "D"},
    {"text": "I propose a middle ground.", "style": "D"},
    {
        "text": "I am likely to take a comment back or try to soften it if I realize that it hurt someone’s feelings.",
        "style": "C",
    },
    {
        "text": "I think it is all right to ask for what I want or to explain how I feel.",
        "style": "E",
    },
    {
        "text": "I find conflict stressful and will avoid it any way I can.",
        "style": "A",
    },
    {
        "text": "I have been described as impatient, controlling, insensitive or emotionally detached.",
        "style": "B",
    },
    {
        "text": "If asked to do something I don’t agree with or don’t want to do, I’ll do it but deliberately won’t do it as well as I could have.",
        "style": "A",
    },
    {
        "text": "I let my body language communicate my feelings rather than telling people directly how I feel.",
        "style": "A",
    },
    {
        "text": "I remain calm and confident when faced with aggression or criticism.",
        "style": "E",
    },
    {"text": "I may overextend myself trying to meet everyone’s needs.", "style": "C"},
    {
        "text": "I try to find a fair combination of gains and losses for both of us.",
        "style": "E",
    },
    {"text": "I look for and acknowledge common ground.", "style": "E"},
    {
        "text": "I have a hard time being clear about what I want and need for fear of appearing demanding or selfish.",
        "style": "C",
    },
    {"text": "I can overlook valuable ideas in favor of action.", "style": "D"},
    {"text": "I may not be open to hear other points of view.", "style": "B"},
    {"text": "I avoid taking positions that would create controversy.", "style": "A"},
]

scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

print("Negotiation Self-Assessment\n")
print(
    "Rate each statement on a scale of 0–5:\n0 = Never, 1 = Rarely, 2 = Sometimes, 3 = Occasionally, 4 = Frequently, 5 = Always\n"
)

for i, statement in enumerate(statements, 1):
    while True:
        try:
            score = int(input(f"{i}. {statement['text']} "))
            if 0 <= score <= 5:
                scores[statement["style"]] += score
                break
            else:
                print("Please enter a valid score between 0 and 5.")
        except ValueError:
            print("Please enter a number.")

print("\nYour Negotiation Style Scores:")
for style, score in scores.items():
    print(f"{style}: {score}")

print("\nInterpretation of Results:")
for style, score in scores.items():
    if score <= 10:
        reliance = "slight reliance"
    elif 11 <= score <= 19:
        reliance = "moderate reliance"
    else:
        reliance = "strong reliance"
    print(f"Style {style}: {reliance}")

max_score = max(scores.values())
dominant_styles = [style for style, score in scores.items() if score == max_score]

print("\nYour dominant negotiation style(s):", ", ".join(dominant_styles))

print("\nSuggestions:")
for style in dominant_styles:
    if style == "A":
        print(
            "Avoidance: Use this when the issue is trivial, or you need time to cool down. Avoid overusing as it can harm relationships and outcomes."
        )
    elif style == "B":
        print(
            "Aggression: Effective for quick decisions or enforcing rules, but risks damaging trust and long-term relationships."
        )
    elif style == "C":
        print(
            "Accommodation: Great for preserving harmony, but ensure your own needs are not neglected."
        )
    elif style == "D":
        print(
            "Compromise: Useful for temporary agreements, but explore collaborative solutions for better outcomes."
        )
    elif style == "E":
        print(
            "Collaboration: Ideal for WIN-WIN results; invest time and energy to build sustainable and satisfying solutions."
        )

print("\nThank you for completing the self-assessment!")
