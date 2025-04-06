def process_symptoms(message):
    """Basic AI Logic for mapping symptoms to conditions."""
    
    # Pre-defined symptoms mapping (to keep it simple)
    symptom_to_condition = {
        "fever": "You might have the flu or a viral infection.",
        "headache": "Could be tension or a sign of dehydration.",
        "sore throat": "Could be viral or bacterial infection.",
        "fatigue": "May indicate stress, dehydration, or early-stage viral infection.",
        "nausea": "Could be food poisoning, viral infection, or stomach upset.",
    }
    
    # Check if any known symptom is present in the user input
    for symptom, advice in symptom_to_condition.items():
        if symptom in message:
            return advice
    
    # Default message if no known symptom is detected
    return "I'm not sure about that symptom, please consult a doctor or provide more details."

