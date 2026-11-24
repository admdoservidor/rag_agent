from deepagents import create_deep_agent
from ragda.core.prompts import RAG_WORKFLOW_INSTRUCTIONS, CHUNK_ANALYST_INSTRUCTIONS, SUBAGENT_DELEGATION_INSTRUCTIONS
from ragda.tools.search_doc import search_documentation 
from ragda.llm.provider import llm
from deepagents.backends import StateBackend
from langchain_core.messages import HumanMessage

backend = StateBackend()
max_concurrent_analysts = 3

INSTRUCTIONS = (
    RAG_WORKFLOW_INSTRUCTIONS
    + "\n\n"
    + "=" * 80
    + "\n\n"
    + SUBAGENT_DELEGATION_INSTRUCTIONS.format(
        max_concurrent_analysts=max_concurrent_analysts,
    )
)

chunk_analyst_subagent = {
    "name": "chunk-analyst",
    "description": (
        "Analyze one retrieved documentation chunk file. "
        "Pass the user question and a single file path under /retrieved/."
    ),
    "system_prompt": CHUNK_ANALYST_INSTRUCTIONS,
}

agent = create_deep_agent(
    model=llm,
    tools=[search_documentation],
    backend=backend,
    system_prompt=INSTRUCTIONS,
    subagents=[chunk_analyst_subagent],
)
