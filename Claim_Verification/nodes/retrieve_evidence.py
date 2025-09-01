"""Retrieve evidence node - fetches evidence for claims using Google search.

Replaced Exa/Tavily with GoogleEvidenceRetriever to minimize external API keys.
"""

import logging
from typing import Any, Dict, List

from fact_checker.nodes.google_evidence_retriever import (
    create_evidence_retriever,
)

from Claim_Verification.Config.nodes import EVIDENCE_RETRIEVAL_CONFIG
from Claim_Verification.schemas import ClaimVerifierState, Evidence

logger = logging.getLogger(__name__)

# Retrieval settings
RESULTS_PER_QUERY = EVIDENCE_RETRIEVAL_CONFIG["results_per_query"]


_retriever = None


async def _search_query(query: str) -> List[Evidence]:
    global _retriever
    if _retriever is None:
        # Defer creation to first use; will read GCP keys from env
        _retriever = create_evidence_retriever()
    logger.info(f"Searching with Google: '{query}'")
    docs = _retriever.retrieve_evidence(query, top_k=RESULTS_PER_QUERY, search_results=max(RESULTS_PER_QUERY, 10))
    evidence = [
        Evidence(url=d.get("link", d.get("url", "")), text=d.get("snippet", d.get("text", "")), title=d.get("title", ""))
        for d in docs
    ]
    logger.info(f"Retrieved {len(evidence)} evidence items")
    return evidence


async def retrieve_evidence_node(
    state: ClaimVerifierState,
) -> Dict[str, List[Evidence]]:
    if not state.query:
        logger.warning("No search query to process")
        return {"evidence": []}

    evidence = await _search_query(state.query)
    logger.info(f"Retrieved {len(evidence)} total evidence snippets")

    return {"evidence": [item.model_dump() for item in evidence]}
