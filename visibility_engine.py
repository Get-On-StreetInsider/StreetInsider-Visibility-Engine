#!/usr/bin/env python3
"""
StreetInsider Visibility Engine
A lightweight content visibility and publication workflow tool designed
to help businesses, brands, and publishers organize, optimize, and monitor
their media content for greater online discoverability.
https://getonstreetinsider.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "content_readiness": "Content Readiness",
        "metadata_quality": "Metadata Quality",
        "distribution": "Distribution",
        "url_visibility": "URL Visibility",
        "ai_discoverability": "AI Discoverability",
        "workflow_efficiency": "Workflow Efficiency",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_distribution_channels(content: int, ai: int, dist: int, meta: int) -> dict:
    return {
        "StreetInsider": min(100, round(content * 1.0)),
        "Search Engines": min(100, round(meta * 1.04)),
        "AI Platforms": min(100, round(ai * 1.0)),
        "Financial Media": min(100, round(dist * 1.0)),
    }


def analyze_visibility(
    content: str,
    content_type: str = "press-release",
    content_readiness: int = 88,
    metadata_quality: int = 82,
    distribution: int = 85,
    url_visibility: int = 78,
    ai_discoverability: int = 90,
    workflow_efficiency: int = 80,
) -> dict:
    """
    Analyze content visibility and publication workflow signals.

    Args:
        content: Content title or identifier
        content_type: Type of content
        content_readiness: Content readiness score (0-100)
        metadata_quality: Metadata quality score (0-100)
        distribution: Distribution score (0-100)
        url_visibility: URL visibility score (0-100)
        ai_discoverability: AI discoverability score (0-100)
        workflow_efficiency: Workflow efficiency score (0-100)

    Returns:
        dict with individual signal scores, overall visibility index,
        and distribution channel breakdown
    """
    scores = {
        "content_readiness": content_readiness,
        "metadata_quality": metadata_quality,
        "distribution": distribution,
        "url_visibility": url_visibility,
        "ai_discoverability": ai_discoverability,
        "workflow_efficiency": workflow_efficiency,
    }
    overall_visibility_index = round(sum(scores.values()) / 6)

    return {
        "content": content,
        "content_type": " ".join(w.capitalize() for w in content_type.split("-")),
        "content_readiness_score": content_readiness,
        "metadata_quality_score": metadata_quality,
        "distribution_score": distribution,
        "url_visibility_score": url_visibility,
        "ai_discoverability_score": ai_discoverability,
        "workflow_efficiency_score": workflow_efficiency,
        "overall_visibility_index": overall_visibility_index,
        "priority_action": get_priority_action(scores),
        "distribution_channels": get_distribution_channels(content_readiness, ai_discoverability, distribution, metadata_quality),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    content = args[0] if len(args) > 0 else "content-title"
    content_type = args[1] if len(args) > 1 else "press-release"
    content_readiness = int(args[2]) if len(args) > 2 else 88
    metadata_quality = int(args[3]) if len(args) > 3 else 82
    distribution = int(args[4]) if len(args) > 4 else 85
    url_visibility = int(args[5]) if len(args) > 5 else 78
    ai_discoverability = int(args[6]) if len(args) > 6 else 90
    workflow_efficiency = int(args[7]) if len(args) > 7 else 80

    result = analyze_visibility(
        content, content_type, content_readiness, metadata_quality,
        distribution, url_visibility, ai_discoverability, workflow_efficiency
    )

    print(f"Content: {result['content']}")
    print(f"Content Type: {result['content_type']}")
    print("=" * 45)
    print(f"Content Readiness Score:       {result['content_readiness_score']}/100  [{get_status(result['content_readiness_score'])}]")
    print(f"Metadata Quality Score:        {result['metadata_quality_score']}/100  [{get_status(result['metadata_quality_score'])}]")
    print(f"Distribution Score:            {result['distribution_score']}/100  [{get_status(result['distribution_score'])}]")
    print(f"URL Visibility Score:          {result['url_visibility_score']}/100  [{get_status(result['url_visibility_score'])}]")
    print(f"AI Discoverability Score:      {result['ai_discoverability_score']}/100  [{get_status(result['ai_discoverability_score'])}]")
    print(f"Workflow Efficiency Score:     {result['workflow_efficiency_score']}/100  [{get_status(result['workflow_efficiency_score'])}]")
    print("=" * 45)
    print(f"Overall Visibility Index:      {result['overall_visibility_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nDistribution Channels:")
    for channel, score in result['distribution_channels'].items():
        print(f"  {channel:<26} {score}/100")


if __name__ == "__main__":
    main()
