---
title: secrets management
summary: Tools related to secrets management
authors: ["ivan k"]
tags: ["tools", "secrets", "secrets management", "python", "go"]
date: 2021-03-08
published: true
---

!!! note "secrets"
    Managing secrets

## Secrets realated to AWS cloud

??? summary "aws-vault"
    [AWS Vault][aws-vault]
    a vault for securely storing and accessing AWS credentials in development environments
        : lanugage **Go**
        : clouds **aws**

??? summary "Chamber"
    [Chamber][chamber]
    is a tool for managing secrets. Currently it does so by storing secrets in SSM Parameter Store, an AWS service for storing secrets.
    ???+ warning "meta"
        : lanugage **Go**
        : clouds **aws**
        : supported **terraform**

??? summary "aws secrets summon"
    [AWS Secrets Summon][aws-secrets-summon]
    is a [summon provider][summon-provider] for AWS Secrets Manager
    ???+ warning "meta"
        : lanugage **Go**
        : clouds **aws**

??? summary "side credentials"
    [Sidecred][sidecred]
    handles the lifecycle of your credentials "on the side". It supports multiple credential providers and secret stores, and handles the lifecycle from creation, to rotations and eventual deletion.
    ???+ warning "meta"
        : lanugage **Go**
        : clouds **aws**

[chamber]: https://github.com/segmentio/chamber
[summon-provider]: https://github.com/cyberark/summon
[aws-secrets-summon]: https://github.com/cyberark/summon-aws-secrets
[aws-vault]: https://github.com/99designs/aws-vault
[sidecred]: https://github.com/telia-oss/sidecred
