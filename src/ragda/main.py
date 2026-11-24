from ragda.agents.agent import agent
from langchain_core.messages import HumanMessage

def main() -> None:
    result = agent.invoke(
        {"messages": [HumanMessage(content="How do I stream intermediate tool results from a subagent?")]}
    )

    for msg in result.get("messages", []):
        if msg.content:
            print(msg.content)


if __name__ == "__main__":
    main()

