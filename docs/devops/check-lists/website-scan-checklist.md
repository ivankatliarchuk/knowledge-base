---
title: website scan checklist
created: 2021-03-26
tags: ["checklist", "website", "site", "scan"]
source:
author: ik
---

# The Complete Security Vulnerability Assessment Checklist

> ## Excerpt
> Our essential security vulnerability assessment checklist is your playbook for comprehensively security testing a web application for vulnerabilities.

### Automated dynamic scanning

- [X] **Choose automated scanning method.** Select an appropriate commercial or open source security scanning tool, depending on the application framework, that ensures maximum coverage (e.g., Burp Suite Pro, [Zap](https://www.zaproxy.org/), etc.).
- [X] **Scan the application.** Reveal many common security vulnerabilities with this form of testing.

### Manual testing

- [X] **Conduct injection and XSS testing.** Check for the presence of injection flaws like SQL, JSON, XML, and [LDAP injections](). Test for [cross-site scripting (XSS)]() through all input points for the application. Determine whether forms are submitted securely, without tamper.
- [X] **Administer authentication and authorization tests.** Inspect for inadequate authentication methods, improper access control definitions, and broken login processes.
- [X] **Audit session management.** Review for secure session IDs/cookies. Search for instances of [cross-site request forgery (CSRF)]().
- [X] **Investigate sensitive information exposure.** Confirm that no sensitive information is revealed due to improper storage of NPI data, broken error handling, insecure direct object references, and comments in source code.
- [X] **Examine secure configuration.** Guarantee that security configurations aren’t defined and deployed with default settings.
- [X] **Run transport layer security testing.** Ensure that there aren’t any broken encryption algorithms and that ciphers are used to secure the communication channels.
- [X] **Carry out application spidering.** Explore the application for unconventional ways to bypass security controls.
