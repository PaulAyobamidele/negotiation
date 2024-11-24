# Negotiation styles and scores
styles = {
    "A": 14,  # Avoidance
    "B": 12,  # Aggression
    "C": 19,  # Accommodation
    "D": 19,  # Compromise
    "E": 19,  # Collaboration
}


# Define thresholds
def determine_style(scores):
    styles_ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary_styles = [
        style for style, score in styles_ranked if score == styles_ranked[0][1]
    ]
    return primary_styles


# Display results
dominant_styles = determine_style(styles)
print("Your dominant negotiation styles are:", dominant_styles)

# Suggestions
if "E" in dominant_styles:
    print("To achieve WIN-WIN, continue leveraging Collaboration.")
elif "D" in dominant_styles:
    print(
        "Compromise is good for moderate gains, but aim for Collaboration for best results."
    )
