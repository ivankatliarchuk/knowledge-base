---
title: oreilly readiness checklist
summary: https://www.oreilly.com/library/view/production-ready-microservices/9781491965962/app01.html
authors: ["ivan k", "oreilly"]
tags: ["checklist", "best practices", "production", "readiness"]
date: 8-Oct-2022
source:
published: true
---

This will be a checklist to run over all microservices—manually or in an automated way.

# A Production-Ready Service Is Stable and Reliable

- It has a standardized development cycle.
- Its code is thoroughly tested through lint, unit, integration, and end-to-end testing.
- Its test, packaging, build, and release process is completely automated.
- It has a standardized deployment pipeline, containing staging, canary, and production phases.
- Its clients are known.
- Its dependencies are known, and there are backups, alternatives, fallbacks, and caching in place in case of failures.
- It has stable and reliable routing and discovery in place.

# A Production-Ready Service Is Scalable and Performant

- Its qualitative and quantitative growth scales are known.
- It uses hardware resources efficiently.
- Its resource bottlenecks and requirements have been identified.
- Capacity planning is automated and performed on a scheduled basis.
- Its dependencies will scale with it.
- It will scale with its clients.
- Its traffic patterns are understood.
- Traffic can be re-routed in case of failures.
- It is written in a programming language that allows it to be scalable and performant.
- It handles and processes tasks in a performant manner.
- It handles and stores data in a scalable and performant way.

# A Production-Ready Service Is Fault Tolerant and Prepared for Any Catastrophe

- It has no single point of failure.
- All failure scenarios and ...
