from typing import Dict, Any

from graph.chains.generation import generation_chain
from graph.state import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    documents = state["documents"]
    #estamos usando context porque no LLM o ChatPromptTemplate.from_messages
    #passamos context
    #Question: {question} \nContext: {context} \nAnswer:
    generation = generation_chain.invoke({"question": question, "context": documents})

    return {"question": question, "generation": generation, "documents": documents}