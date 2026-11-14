from langgraph.constants import END
from langgraph.graph import StateGraph

from graph.consts import WEB_SEARCH, GENERATE, RETRIEVE, GRADE_DOCUMENTS
from graph.nodes import web_search, retrieve, grade_documents, generate
from graph.state import GraphState


def should_continue(state: GraphState) -> str:
    is_web_search = state["web_search"]

    if is_web_search:
        return WEB_SEARCH
    else:
        return GENERATE


workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(WEB_SEARCH, web_search)
workflow.add_node(GENERATE, generate)

workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    should_continue,
    path_map= {
        WEB_SEARCH: WEB_SEARCH,
        GENERATE: GENERATE
    }
)
workflow.add_edge(WEB_SEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()
# app.get_graph().draw_mermaid_png(output_file_path="graph.png")
