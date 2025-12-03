import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        print(self.user_message)
        if self.usecase == "Basic Chatbot":
            for event in self.graph.stream({"messages": {"role": "user", "content": self.user_message}}):
                print(event.values())
                for value in event.values():
                    print(value["messages"])
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
        elif self.usecase == "Chatbot with Web":
            # Prepare state and invoke the graph
            initial_state = {"messages": [self.user_message]}
            res = self.graph.invoke(initial_state)

            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool call started")
                        st.write(message.content)
                        st.write("Tool call ended")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
