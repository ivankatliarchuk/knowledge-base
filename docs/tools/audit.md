---
title: audit tooling
summary: Tools related to audit
authors: ["Ivan K"]
tags: ["tools", "audit", "hardening", "forensic", "python", "security", "cyber-sec"]
date: 2021-03-08
published: true
---

!!! note "audit"
    Audit, hardening and forensics

## Audit tooling for different clouds

??? summary "Cloud Security Suite"
    [Cloud Security Suite][1]{:target="_blank"}
    one stop tool for auditing the security posture of AWS/GCP/Azure infrastructure.
    ???+ warning "meta"
        : lanugage **Python**
        : clouds **aws,gcp,azure**

??? summary "Prowler"
    [Prowler][2]{:target="_blank"}
    is a command line tool for AWS Security Best Practices Assessment, Auditing, Hardening and Forensics Readiness Tool.
    ???+ warning "meta"
        : lanugage **Python**
        : clouds **aws**

??? summary "CS Suite"
    [CloudTracker][3]
    helps you find over-privileged IAM users and roles by comparing CloudTrail logs with current IAM policies.
    ???+ warning "meta"
        : lanugage **Python**
        : clouds **aws**

??? summary "Principal Mapper"
    [principalmapper][pmapper]
    (PMapper) is a script and library for identifying risks in the configuration of AWS Identity and Access Management (IAM) in an AWS account.
    ???+ warning "meta"
        : lanugage **Python**
        : clouds **aws**

??? summary "SkyArk cloud security"
    [SkyArk][skyark]
    currently focuses on mitigating the new threat of Cloud Shadow Admins, and helps organizations to discover, assess and protect cloud privileged entities. Stealthy and undercover cloud admins may reside in every public cloud platform and SkyArk helps mitigating the risk in AWS and Azure.
    ???+ warning "meta"
        : lanugage **.Net**
        : clouds **aws,azure**

[1]: https://github.com/SecurityFTW/cs-suite
[2]: https://github.com/ik-security/prowler
[3]: https://github.com/duo-labs/cloudtracker
[pmapper]: https://github.com/nccgroup/PMapper
[skyark]: https://github.com/cyberark/SkyArk

