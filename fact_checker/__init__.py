"""Fact Checker - Orchestration system for fact-checking pipelines.

Designed to be import-light so module tools/tests don't pull heavy deps.
"""

# Export names lazily to avoid importing optional/heavy modules at package import time
__all__ = ["create_graph", "graph", "State", "FactCheckReport"]


def __getattr__(name):
    if name in ("create_graph", "graph"):
        from fact_checker.agent import create_graph, graph  # type: ignore
        return {"create_graph": create_graph, "graph": graph}[name]
    if name in ("State", "FactCheckReport"):
        from fact_checker.schemas import State, FactCheckReport  # type: ignore
        return {"State": State, "FactCheckReport": FactCheckReport}[name]
    raise AttributeError(name)
