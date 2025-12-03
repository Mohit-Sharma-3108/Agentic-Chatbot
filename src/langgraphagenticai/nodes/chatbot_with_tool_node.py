from src.langgraphagenticai.state.state import State


class ChatbotWithToolNode:
    """
        Chatbot logic enhances with tool integration
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """Processes the input and generates a response with tool integration

        Args:
            state (State): Current state of the graph

        Returns:
            dict: dictionary with messages as key and a list with llm response and tool response as values
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        # Simulatae tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}
    
    def create_chatbot(self, tools: list):
        """Return a chatbot with node function

        Args:
            tools (list): list of tools
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """Chatbot logic for processing the input state and returning a response

            Args:
                state (State): Current state of the graph
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node