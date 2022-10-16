---
title: vault checklist
summary: check list for hashicorp vault
authors: ["ivan k"]
tags: ["checklist", "vault", "best practices", "readiness", "hashicorp"]
date: 8-Oct-2022
published: true
source: https://itrevolution.com/post-incident-review/
author: rockos.io
---

# Vault production checklist

Managing secrets is a challenge. When it comes to Vault, there are many options to design your security architecture. Along with the right secret management design in mind, you’ll also need to consider a properly configured Vault service.

Since Vault is a central point of truth for your credentials, it takes some effort to configure it rightly. Basically, in production, you’ll need to properly manage 2 main separate services: Vault and Vault’s Backend Storage. In this article, we’ll go through all requirements of the production-ready Vault deployment.

## Setting up & maintaining Vault

**TLS connection.** Regardless of your environment you always need to configure Vault to use SSL certificates. Moreover, if you’re using a load balancer or a proxy, you shouldn’t terminate the SSL connection to the Vault service. Make sure to provision and update Vault’s SSL certificates in time.

**High Availability.** In a production environment where microservices rely on a centralized secret store, it is critical to avoid downtime and make this store reliable. There are a number of backends that can be used in conjunction with Vault to create a Highly Available service.

**Auto-Unseal.** This requirement is strongly related to the previous one. Vault starts in a ‘sealed’ state. Since version 1.0, Vault has an auto-unseal feature that is based on cloud services: Amazon KMS, Azure Key Vault, AliCloud KMS, and Google Cloud KMS. Consider creating a proper cloud policy to grant Vault permissions to use the appropriate KMS.

**Load Balancer configuration.** It is important to note that you need to configure your Load Balancer to route traffic only to “healthy” Vault replicas. As we said earlier, once the Vault has started, it has a “sealed” state. You need to keep in mind that in HA mode your replicas will have separate states. And if one replica restarts, it would take some time for auto-unseal to perform. Make sure that your load balancer checks if the replica is in the “unsealed” state before routing the traffic to it.

**Vault upgrade strategy.** Vault is actively developed by the community and new versions are released frequently. It is critical to minimize the risks and upgrade Vault regularly along with new bug and security fixes. In the HA mode, you need to pay attention to the upgrade strategy. Each node must be stopped gracefully one-by-one starting from the active node. This will guarantee that the data won’t be corrupted or lost.

**Underlying infrastructure upgrade strategy.** Vault is always run on top of the operating system. The underlying infrastructure is run on Bare metal, VM or containers. Unfortunately, all of these options can have potential undiscovered vulnerabilities. Always have a strategy to upgrade your underlying software and avoid critical issues.

**Firewall configuration.** Regardless of the environments, one of the most powerful ways to secure your Vault service is to restrict traffic from untrusted sources. The outgoing Vault traffic must be restricted as well. If it is possible, configure your underlying firewall to allow traffic only from your applications and services that need to connect to Vault.

**Linux as the main OS.** While Vault can be run on different operating systems, the official Hashicorp recommendation is simple and straightforward: use Linux. The reason for this is that Vault’s source code is optimized to use Linux kernel API to manage memory access securely.

**SSH access.** The node that is running Vault must be only accessed by the Vault API. Avoid exposing any RPC access to the underlying infrastructure. The information about the Vault service can be accessed using the Audit and Telemetry data.

**Auditing.** Vault supports special audit logs that trace in detail how the service was queried. These logs are disabled by default for simplicity, but in production systems, it is highly recommended to enable it. Vault can be configured to write audit logs into multiple “audit devices”: File, Syslog, and Socket. There is one critical [pitfall](https://www.vaultproject.io/docs/audit/index.html#blocked-audit-devices) regarding Vault’s auditing mechanism that is often overlooked by newcomers:

> If you have only one audit device enabled, and it is blocking (network block, etc.), then Vault will be unresponsive. Vault will not complete any requests until the audit device can write.

In production, it is recommended to use multiple devices at once to mitigate the risks of unresponsive Vault service.

As we restrict the access to Vault nodes, it is a good practice to send audit logs into a separate log aggregation system, e.g. ELK.

**Isolated process.** Consider running Vault as a single process on the system. You can isolate your service using a VM or a container. The official Hashicorp infrastructure priority is the following: Bare metal > VMs > Containers. Make sure that there are no other separate processes that can be compromised to corrupt the Vault process.

**Disable Swap & Core Dumps.** Even the Vault is a stateless service — there is some sensitive data that is being kept in memory. Keeping this in mind, it is highly recommended to configure the underlying operating system to disable swap. This will reduce the risk of cashing sensitive data to disk. Along with swap, it is recommended to turn off core dumps to disable access to the Vault’s internal memory by users and processes.

**Telemetry.** Hashicorp products often expose the telemetry interface, and Vault is not an exception. Vault delivers a [variety of useful metrics](https://www.vaultproject.io/docs/internals/telemetry.html) about itself. In production, it is useful to track the performance of your Backend Storage operations. Vault can be configured to send the metrics to the particular upstream service, e.g. [StatsD](https://github.com/statsd/statsd).

## Setting up & maintaining Storage Backend

One of the underlying challenges in a production-ready Vault service is to manage the Vault’s storage backend. Regardless of your storage engine choice, there are requirements that must be fulfilled:

**Reliability.** If your storage backend crashes, the Vault service will be unreachable too. Along with Vault, the storage backend must implement the High Availability pattern.

**Security.** The data in backend storage is always encrypted by Vault but if the storage is compromised — the data can be corrupted. Make sure that the storage backend can only be accessed by Vault.

**Backup & Recovery.** Prevent situations of data corruption or loss. Implement the backup and recovery strategy for your storage.

**Upgrades.** Some supported storages are distributed as open source software. Along with Vault, this software should be upgraded to minimize potential risks.

# Rockos Managed Vault

If you’re struggling to implement the Vault production checklist then you can simply use the [Managed Vault](https://rockos.io/managed-vault) solution by the Rockos team. It takes a lot of effort to manage both Vault and Backend Storage properly. We believe that people should focus on **using** Vault but **not managing** it. With this goal in mind, we work hard to implement a secure, robust and battle-tested Vault service that can be utilized in production.
