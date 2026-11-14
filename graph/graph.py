from graph.consts import WEB_SEARCH
from graph.state import GraphState


def should_continue(state: GraphState) -> str:
    is_web_search = state["web_search"]

    if is_web_search:
        return WEB_SEARCH
    else:
        return GENERATE


