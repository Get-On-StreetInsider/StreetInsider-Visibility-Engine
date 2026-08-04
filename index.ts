#!/usr/bin/env node

interface VisibilityInput {
  content: string;
  contentType: string;
  contentReadiness: number;
  metadataQuality: number;
  distribution: number;
  urlVisibility: number;
  aiDiscoverability: number;
  workflowEfficiency: number;
}

interface VisibilityOutput {
  content: string;
  contentType: string;
  contentReadinessScore: number;
  metadataQualityScore: number;
  distributionScore: number;
  urlVisibilityScore: number;
  aiDiscoverabilityScore: number;
  workflowEfficiencyScore: number;
  overallVisibilityIndex: number;
  priorityAction: string;
  distributionChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    contentReadiness: "Content Readiness",
    metadataQuality: "Metadata Quality",
    distribution: "Distribution",
    urlVisibility: "URL Visibility",
    aiDiscoverability: "AI Discoverability",
    workflowEfficiency: "Workflow Efficiency",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getDistributionChannels(content: number, ai: number, dist: number, meta: number): Record<string, number> {
  return {
    "StreetInsider": Math.min(100, Math.round(content * 1.0)),
    "Search Engines": Math.min(100, Math.round(meta * 1.04)),
    "AI Platforms": Math.min(100, Math.round(ai * 1.0)),
    "Financial Media": Math.min(100, Math.round(dist * 1.0)),
  };
}

export function analyzeVisibility(input: VisibilityInput): VisibilityOutput {
  const scores = {
    contentReadiness: input.contentReadiness,
    metadataQuality: input.metadataQuality,
    distribution: input.distribution,
    urlVisibility: input.urlVisibility,
    aiDiscoverability: input.aiDiscoverability,
    workflowEfficiency: input.workflowEfficiency,
  };
  const overallVisibilityIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    content: input.content,
    contentType: input.contentType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" "),
    contentReadinessScore: input.contentReadiness,
    metadataQualityScore: input.metadataQuality,
    distributionScore: input.distribution,
    urlVisibilityScore: input.urlVisibility,
    aiDiscoverabilityScore: input.aiDiscoverability,
    workflowEfficiencyScore: input.workflowEfficiency,
    overallVisibilityIndex,
    priorityAction: getPriorityAction(scores),
    distributionChannels: getDistributionChannels(input.contentReadiness, input.aiDiscoverability, input.distribution, input.metadataQuality),
  };
}

const args = process.argv.slice(2);
const content = args[0] || "content-title";
const contentType = args[1] || "press-release";
const contentReadiness = parseInt(args[2]) || 88;
const metadataQuality = parseInt(args[3]) || 82;
const distribution = parseInt(args[4]) || 85;
const urlVisibility = parseInt(args[5]) || 78;
const aiDiscoverability = parseInt(args[6]) || 90;
const workflowEfficiency = parseInt(args[7]) || 80;

const result = analyzeVisibility({
  content, contentType, contentReadiness, metadataQuality,
  distribution, urlVisibility, aiDiscoverability, workflowEfficiency,
});

console.log(`Content: ${result.content}`);
console.log(`Content Type: ${result.contentType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Content Readiness Score:       ${result.contentReadinessScore}/100  [${getStatus(result.contentReadinessScore)}]`);
console.log(`Metadata Quality Score:        ${result.metadataQualityScore}/100  [${getStatus(result.metadataQualityScore)}]`);
console.log(`Distribution Score:            ${result.distributionScore}/100  [${getStatus(result.distributionScore)}]`);
console.log(`URL Visibility Score:          ${result.urlVisibilityScore}/100  [${getStatus(result.urlVisibilityScore)}]`);
console.log(`AI Discoverability Score:      ${result.aiDiscoverabilityScore}/100  [${getStatus(result.aiDiscoverabilityScore)}]`);
console.log(`Workflow Efficiency Score:     ${result.workflowEfficiencyScore}/100  [${getStatus(result.workflowEfficiencyScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Visibility Index:      ${result.overallVisibilityIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nDistribution Channels:");
Object.entries(result.distributionChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(24)} ${score}/100`);
});
