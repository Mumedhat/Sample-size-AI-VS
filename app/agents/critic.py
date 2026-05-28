from app.core.validator import validate_study


def critic_node(state):

    validation = validate_study(state)

    return {
        **state,
        "bias_risk": validation["bias_risk"],
        "validity_score": validation["validity_score"],
        "validation_issues": validation["validation_issues"]
    }