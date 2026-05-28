def aggregator_node(state):

    final_report = {

        "study_design": state.get("study_type"),

        "population": state.get("population"),

        "intervention": state.get("intervention"),

        "recommended_statistical_test":
            state.get("statistical_test"),

        "estimated_effect_size":
            state.get("effect_size"),

        "estimated_sample_size":
            state.get("sample_size"),

        "confidence":
            round(state.get("consensus_confidence", 0), 2)
    }

    return {
        **state,
        "final_report": final_report
    }