def get_user_data(intent):
    if intent == "weight_trend":
        return {
            "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "weights": [80, 79, 78.5, 77, 75.5, 74],
            "goal_weight": 70
        }
    return None
