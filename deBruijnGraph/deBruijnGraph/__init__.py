"""
De Bruijn Graph library
"""
__version__ = "0.1.0"

def create(sequence: str, k: int) -> dict:
    """
    Create a De Bruijn Graph from a sequence and k-mer length
    """
    graph = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer[:-1] not in graph:
            graph[kmer[:-1]] = [kmer[1:]]
        else:
            graph[kmer[:-1]].append(kmer[1:])
    return graph

def to_mermaid(graph: dict) -> str:
    """
    Convert a De Bruijn Graph to a Mermaid string
    """
    mermaid = "graph TD\n"
    for node in graph:
        mermaid += f"    {node}({node})\n"
        for neighbor in graph[node]:
            mermaid += f"    {node} -->|{neighbor[-1]}| {neighbor}\n"
    mermaid += "end\n"
    return mermaid

