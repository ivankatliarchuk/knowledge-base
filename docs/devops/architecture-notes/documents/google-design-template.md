---
title: google's design document template
summary: desing document template
authors: ["Ivan K"]
tags: ["architecture", "design", "template"]
date: 2021-06-27
source:
published: true
---

# Google's Design Document Template

Here are the reliability- and security-related sections of the Google design document template:

## Scalability

> How does your system scale? Consider both data size increase (if applicable) and traffic increase (if applicable).

Consider the current hardware situation: adding more resources might take much longer than you think, or might be too expensive for your project. What initial resources will you need? You should plan for high utilization, but be aware that using more resources than you need will block expansion of your service.

## Redundancy and reliability

Discuss how the system will handle local data loss and transient errors (e.g., tem‐ porary outages), and how each affects your system

> Which systems or components require data backup? How is the data backed up? How is it restored? What happens between the time data is lost and the time it’s restored?

## Dependency considerations

> What happens if your dependencies on other services are unavailable for a period of time?

> Which services must be running in order for your application to start? Don’t for‐ get subtle dependencies like resolving names using DNS or checking the local time.

> Are you introducing any dependency cycles, such as blocking on a system that can’t run if your application isn’t already up? If you have doubts, discuss your use case with the team that owns the system you depend on.

## Data integrity

> How will you find out about data corruption or loss in your data stores?

> What sources of data loss are detected (user error, application bugs, storage plat‐ form bugs, site/replica disasters)?

> How long will it take to notice each of these types of losses?

> What is your plan to recover from each of these types of losses?

## SLA requirements

> What mechanisms are in place for auditing and monitoring the service level guarantees of your application?

> How can you guarantee the stated level of reliability?

## Security and privacy considerations

Our systems get attacked regularly. Think about potential attacks relevant for this design and describe the worst-case impact it would have, along with the countermeasures you have in place to prevent or mitigate each attack.

List any known vulnerabilities or potentially insecure dependencies.

If, for some reason, your application doesn’t have security or privacy considerations, explicitly state so and why.


