from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
        Basic Chatbot logic implementaion
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """Processes the input state and generates a chatbot response

        Args:
            state (State): Current state of the graph

        Returns:
            dict: State of graph after function has been implemented
        """
        return {"messages": self.llm.invoke(state['messages'])}