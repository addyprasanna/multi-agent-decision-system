from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

"""
Policies:
    min_sources: 5
    min_unique_domains = 3
    min_subsquestion_coverage = 0.7
    max_research_iterations = 2
"""

class ResearchBrief(BaseModel):
    decision_question: str
    subquestions: List[str]
    constraints: Dict[str, str] = Field(default_factory = dict)
    target_recency_days: Optional[int] = None

class EvidenceItem(BaseModel):
    url: str
    title: str
    domain: str
    snippet: str
    subquestion_ids: List[int] = Field(default_factory=list)

    allow: bool = False
    relevance_score: float = 0.0
    validity_score = float = 0.0
    retrieved_at: datetime = Field(default_factory=datetime.utcnow)

class ResearchMetrics(BaseModel):
    sources_total: int
    unique_domains: int
    coverage_ratio: float
    allowlist_share: float

class DecisionState(BaseModel):
    user_goal: str
    research_brief: Optional[ResearchBrief] = None
    evidence_pool: List[EvidenceItem] = Field(default_factory=list)
    research_metrics: Optional[ResearchMetrics] = None

    structured_decision: Optional[dict] = None
    critic_report: Optional[dict] = None
    final_answer: Optional[str] = None

    loop_count: int = 0
    tool_budget: int = 5
    logs: List[str] = Field(default_factory=list)
