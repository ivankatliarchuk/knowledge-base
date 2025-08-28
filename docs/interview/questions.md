---
title: interview questions
summary: interview questions
authors: ["ivan k"]
tags: ["interview", "questions"]
date: 16-aug-2025
published: true
---

# Interview Questions

## Netflix

Round 1 – Systems at Scale, K8s, Cloud & Linux (45 mins)
• How would you implement fine-grained service discovery across 1000+ microservices using Envoy or Istio?
• Explain how you’d leverage eBPF + Cilium to enforce network security policies at runtime, and what the advantages are over traditional CNIs?
• Netflix runs multi-cloud. Describe your approach to cross-cloud routing, IAM, and secret syncing.
• What happens when systemd units fail intermittently on EKS nodes? How do you detect and heal?
• Your app teams demand custom AMIs. What’s your pre-prod vetting strategy at kernel and runtime?
• Walk through advanced kube-probe configurations to detect business logic failures, not just HTTP 200.
• How do you handle DNS-level outages inside a service mesh without a full app redeploy?
• Terraform remote_state backend suddenly times out. What’s your recovery and damage containment strategy?

Round 2 – RCA, Fire Drills, and Netflix-Scale Chaos (75 mins)
• A new Envoy config rollout silently broke mTLS between edge and mesh. What’s your RCA trace?
• HPA refuses to scale even though Prometheus shows CPU > 80%. Diagnose with cloud + K8s metrics.
• You introduced a sidecar-based caching layer. Suddenly, tail latency spikes. What’s your debug path?
• 504 errors on the playback service. Cloud LB shows healthy, mesh sidecars pass, but users can’t stream. Triage?
• You notice surging NAT costs. No infra changes this week. What could silently trigger that?

Round 3 – Leadership, Chaos Culture & Engineering Influence (30 mins)
• How do you build an engineering culture where SLOs are owned, not ignored?
• You’re asked to ship a multi-region failover in 3 weeks no DNS layer allowed. Your plan?
• Describe how you’d test infra chaos and graceful degradation for a Netflix Originals release.
• How do you prove ROI of infra modernization to non-technical execs?

💡 TL;DR:
If you haven’t:
1. Used eBPF to trace a TCP reset at runtime
2. Investigated TLS outages across sidecars
3. Debugged Redis inconsistency under pressure
4. Simulated a kubelet crash mid-streaming session

## Nvidia

Senior DevOps Engineer Interview at NVIDIA

Round 1 – AI/HPC Scaling, K8s, Cloud & Linux
1. How would you auto-scale GPU nodes for training workloads without wasting GPU hours on idle pods?
2. A multi-cluster, multi-region AI training job fails halfway because one cluster runs out of GPU memory. How do you rebalance workloads live?
3. How do you configure Kubernetes taints and tolerations for GPU workloads?
4. How would you handle CUDA driver upgrades in K8s without disrupting thousands of running AI pods?
5. Explain how you’d pre-warm GPU nodes for massive AI inference traffic (e.g., ChatGPT-scale) with zero cold-start penalty.
6. How would you monitor GPU utilization in real-time in a Kubernetes cluster?

Round 2 – RCA, Fire Drills & GPU Chaos
1. How would you check if a GPU pod in Kubernetes is using the GPU assigned to it?
2. What are NCCL logs, and why are they important in distributed training?
3. Persistent storage for AI datasets starts showing 200ms+ latency. How do you pinpoint whether it’s the storage backend, the network, or the GPU node?
4. A Kubernetes GPU pod requests 16GB VRAM but only gets 12GB due to fragmentation. How do you detect and fix in real-time?
5. Your AI pipeline cost doubles in 24 hours with no infra change. Profiling shows a silent GPU resource leak. How do you hunt it down?

Round 3 – Leadership, Reliability Culture & Scaling Influence
1. How do you set up SLOs for both AI inference latency and batch training completion times without overprovisioning GPUs?
2. You’re told to implement multi-region AI inference failover without DNS-based routing. What’s your plan?
3. How do you justify infra cost for idle GPU pre-warming to leadership when each hour costs $30–$40 per GPU?

TL;DR:
If you haven’t:
Designed GPU-aware K8s schedulers for AI workloads
Debugged NCCL all-reduce failures in distributed training under pressure
Root-caused VRAM fragmentation mid-inference
Balanced batch + real-time AI workloads on the same fleet
…then an NVIDIA interview will show you exactly where your DevOps muscle memory ends.

## Kubernetes

Here’s what I ask senior engineers:
1. Walk me through what happens inside kube-proxy when IPVS rules vanish mid-traffic.
→ Where does service routing actually break?
2. You lose access to your Terraform remote state during a live deploy.
→ How do you rebuild infra trust without downtime?
3. Latency doubles for 15% of users post-canary. Logs and metrics are green.
→ What is your first triage step, and why?
4. How do you secure GitHub Actions pipelines against secret leaks and supply chain attacks?
→ Be precise, not generic.
5. Your HPA scales to max, but pods remain Pending despite node capacity.
→ Where do you start debugging, cluster vs scheduler vs CNI?
6. What is the blast radius if etcd suffers corruption in a multi-master control plane?
→ Walk through recovery steps.
7. Tell me about the last time you wrote or read a real RCA.
→ If it ends with “we restarted the pod,” it isn’t one.
