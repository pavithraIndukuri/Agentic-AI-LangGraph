from graph import graph

print("========== Agentic AI ==========")

query = input("Enter your task: ")

response = graph.invoke({
    "query": query
})

print("\nFinal Output")
print("---------------------------")
print(response["result"])
