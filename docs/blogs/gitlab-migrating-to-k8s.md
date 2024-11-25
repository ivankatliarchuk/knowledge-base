---
title: gitlab migration
summary: migrate from docker+machine to kubernetes
authors: ["ivan k"]
tags: ["blog", "gitlab", "migration", "runners"]
date: 23-11-2024
published: true
published:
-
---

**Migrating GitLab CI from Docker+Machine to Kubernetes: Lessons Learned**

GitLab's decision to deprecate the Docker+Machine executor has left many teams scrambling for alternatives. Migrating to Kubernetes for running CI jobs feels like the natural choice for scalability, but the path isn’t as straightforward as it seems. In this post, we’ll focus on a specific part of our migration journey where we got stuck, struggled, and eventually found a way forward. Along the way, we hope to highlight gaps in GitLab’s guidance and suggest ways to improve the developer experience for teams like ours.

### **The Reality of Using GitLab SaaS at Scale**

GitLab is, without question, a great product. Its potential to streamline development workflows is undeniable. However, the experience for teams using its SaaS offering is  often falls short of its potential.

As platform engineers, our primary goal is to empower developers by improving workflows, enabling faster delivery, and reducing friction. Instead, we find ourselves spending an outsized amount of time navigating vague documentation, guessing configuration best practices, and dealing with frequent breaking changes. Setting up runners at scale, in particular, can feel more like trial and error than a well-defined engineering process.

This isn’t what platform engineering should be about. Platform engineering should be about empowering developers, not wrestling with foundational infrastructure that could be more intuitive especially when you pay for a product. GitLab has the potential to be the enabler we need—but the gap between that vision and our current reality needs addressing.

### **A Bit of History**

GitLab Docker+Machine is a fork of Docker Machine, a technology deprecated by Docker in 2021. You can read more about Docker's decision [here](https://github.com/docker/roadmap/issues/245). The Gitlab team understand the complexity of supporting a technology that noone else uses, GitLab announced plans to discontinue Docker+Machine maintenance by 2027, giving teams a few years to migrate away.

As a replacement, GitLab recommends using the [autoscaler](https://docs.gitlab.com/runner/runner_autoscale/) as a drop-in solution. While this seems straightforward on paper, the migration process introduces its own set of complexities—especially for teams operating at scale.

### **About Us and Our Use Cases**

We are an e-commerce retailer with a strong presence both online and in high-street shops. Our tech department consists of around 1,000 colleagues, with over 400 active GitLab users. On average, we run just under 1,000,000 CI jobs per month.

Currently, we use GitLab primarily for CI and CD, though we’re exploring ways to enhance our CD workflows for greater efficiency and scalability. Our setup isn’t massive by enterprise standards, but it’s large enough that inefficiencies in tooling and workflows have a noticeable impact.

___

### **Why We Migrated**

GitLab’s Docker+Machine executor served us well. It was easy to set up, worked reliably, and scaled efficiently with auto-provisioned machines. But the deprecation forced our shift to something else. Kubernetes emerged as a natural fit, especially since our infrastructure was already Kubernetes-centric. The challenge, however, wasn’t deciding _what_ to migrate to—it was figuring out _how_. Each GitLab version brought breaking changes, leaving us in a continuos cycle of adaptation and state of rework.

While we successfully navigated the transition by making different architectural choices, it was still a significant effort. Given this, we'd prefer to focus our resources on other high-priority initiatives.

___

### **The Core Challenge**

- No official guide.
- No consistent workflow provided anywhere on the internet.
- No single source of truth.

That’s the reality we faced. While GitLab does provide documentation, it’s fragmented, often high-level, and rarely dives deep enough to address real-world, edge-case scenarios. Key questions—like how to scale runners, securely manage tokens, or structure configurations for large teams—were left unanswered.

Transitioning from Docker+Machine, which “just worked,” to a Kubernetes-based CI system felt like diving into the deep end without a life jacket. What once was a straightforward setup became a maze of trial and error, compounded by breaking changes in every major GitLab release, that somehow affects the way things works. Rather than focusing on improving developer workflows, we were forced to spend significant time understanding the underlying complexities of a migration that should have been smoother.

___

### **Where We Got Stuck**

1.  **Runner Registration and Management**
    In Docker+Machine, the runners auto-registered themselves, but most recent Gitlab changes adds complexity in every major release. How the registration workflow should looks like? Why there are multiple tokens required? Should we use one runner per namespace? Per team? Or one global runner? Should runner managers be mutable or immutable? With little guidance, we experimented with several configurations before finding what worked for us, and it is still not the end of the journey.

2.  **Handling Runner Tokens**
    Kubernetes requires Helm charts for deploying runners. But where do we securely store and retrieve registration tokens? AWS Systems Manager (SSM) Parameter Store became our solution, though it wasn’t immediately obvious this was the right approach. It could be a great source of true if we would like to keep runners ids or any other metadata.

3.  **Helm Chart Updates**
    Each GitLab upgrade broke our Helm deployment process. Runner configurations changed subtly, forcing us to rewrite parts of our pipeline after almost every version bump. The lack of more guided approach was frustrating.

___

### **Our Approach**

We tackled these challenges methodically:

1.  **Dynamic Runner Configuration**
    We designed a system where GitLab CI checks for existing runner managers and registers new ones when necessary. This does reduce complexity of a solution and ensured some level of scalability.

2.  **Token Retrieval Workflow**
    Tokens are fetched dynamically from AWS SSM during deployment. When a new runner manager is created, the token is generated automatically and securely stored for reuse.

3.  **Pipeline Resilience**
    We wrapped our Helm chart logic in scripts that validate configuration changes before applying them with [helm unit test](https://github.com/helm-unittest/helm-unittest). And more important we have a suite of end-2-end tests for all the runners on each pull change. This helped us catch breaking changes from GitLab upgrades early.

4.  **Custom helper image**
    Custom GitLab helper images are a potent tool, often overlooked, that can significantly enhance CI/CD pipelines. By creating tailored images, teams can bolster security, streamline workflows, and consolidate solutions to common challenges. For teams managing large-scale or extensive CI pipelines, this approach ensures consistency and reduces repetitive troubleshooting, making it a powerful tool to improve both efficiency and the developer experience.

___

### **What GitLab Can Do Better**

1.  Provide migration-specific documentation.
2.  Offer clear examples of Kubernetes-based workflows.
3.  Ensure version upgrades don’t break runner registrations and other workflows unnecessarily.

___

### **Final Thoughts**

Moving to Kubernetes for GitLab CI has been a rewarding challenge. It gave us scalability and aligned with our infrastructure goals. But the journey was unnecessarily painful due to poor guidance and frequent breaking changes. For teams planning this migration, know that it’s possible—but be ready to adapt and experiment.

For GitLab: the developer experience matters. Clearer documentation with how-to real world public examples and fewer breaking changes would help teams like ours thrive.

Let’s build better workflows together.


## Resources

- https://docs.gitlab.com/ee/ci/runners/new_creation_workflow.html
- https://gitlab.com/gitlab-org/ci-cd/docker-machine
- https://docs.gitlab.com/runner/runner_autoscale/
- https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/runner_scaling/


Custom GitLab helper images are a potent tool, often overlooked, that can significantly enhance CI/CD pipelines. By creating tailored images, teams can bolster security, streamline workflows, and consolidate solutions to common challenges.

For teams managing large-scale or extensive CI pipelines, this approach ensures consistency and reduces repetitive troubleshooting, making it a powerful tool to improve both efficiency and the developer experience.

### **Custom Helper Images**

Using custom GitLab helper images is an often underrated and overlooked, yet it can significantly enhance CI/CD experience. By tailoring the helper image, you can enhance security, streamline developer workflows, and consolidate solutions to common challenges.

For teams managing large-scale CI pipelines, this approach ensures consistency and reduces repetitive troubleshooting, making it a powerful tool to improve both efficiency and the developer experience.
