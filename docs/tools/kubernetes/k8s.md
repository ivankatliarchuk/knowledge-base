---
title: k8s tooling
summary: Kubernetes tooling
authors: ["ivan k"]
tags: ["tools", "k8s", "kubernetes", "k8s", "cis", "mitre", 'paas', 'security']
date: 08-03-2021
source:
published: true
---

## Kubernetes Tooling

- [Kubernetes: essentials](https://itnext.io/kubernetes-essential-tools-2021-def12e84c572)

## Workflow and Automation

- [KubeSeco Framework](https://github.com/appsecco/kubeseco)

## Cluster Management/Dashboards

- [Kubernetes instance calculator](https://learnk8s.io/kubernetes-instance-calculator)
- [Thanos](https://github.com/thanos-io/thanos)
- [DevSpace](https://devspace.cloud/)
- [Weave Scope Dashboard](https://github.com/weaveworks/scope)
- [Kubrics Dashboard](https://github.com/kubricksllc/Kubricks)
- [Kubernator Dashboard](https://github.com/smpio/kubernator)
- [Konstellate Dashboard](https://github.com/jeremykross/konstellate)
- [k8dash Dashboard](https://github.com/herbrandson/k8dash)
- [Octant Dashboard](https://github.com/vmware-tanzu/octant)
- [Pre Scaler](https://github.com/microsoft/k8s-cronjob-prescaler)
- [Node Problem Detector](https://github.com/kubernetes/node-problem-detector/blob/master/README.md)
- [GKE Monitoring](https://github.com/ik-kubernetes/gke-monitoring-tutorial)
- [Loghous/Papertrail](https://github.com/flant/loghouse)

## Logging & Monitoring command liners

- [Kube Dog. Monitor resoruces in cluster](https://github.com/flant/kubedog)
- [Stern Logs. Really Good](https://github.com/wercker/stern)
- [Kail](https://github.com/boz/kail)
- [K8s event exporter](https://github.com/opsgenie/kubernetes-event-exporter)

### Kubernetes Visualizers

- [KubeVious](https://github.com/kubevious/kubevious)
- [KubeView](https://github.com/benc-uk/kubeview)
- [KubeRicks](https://github.com/kubricksllc/Kubricks)
- [Weve Scope](https://github.com/weaveworks/scope)
- [Containerium](https://github.com/containerum/containerum)
- [Status Bay](https://github.com/similarweb/statusbay)
- [Helm Tenkai](https://github.com/softplan/tenkai)
- [Kiali Service Mesh UI](https://kiali.io/)

## Kubernetes Costs & Optimisation

- [K8s cost optimisation](https://github.com/ivankatliarchuk/kubetools?tab=readme-ov-file#cost-optimisation)
- [OpenCost](http://opencost.io/)
- [Krossboard: Centralized Multi-Cluster Kubernetes Usage Accounting](https://github.com/rchakode/kube-opex-analytics)
- [KubeCost: Cross-cloud cost allocation](https://github.com/kubecost/cost-model)
- [KubeGreen](https://kube-green.dev/docs/getting-started/)
- [Snorlax](https://github.com/moonbeam-nyc/snorlax)
- [K8s Cleaner](https://github.com/ik-infrastructure-testing/k8s-cleaner-fork)

## AWS Specific K8s Tooling

- [App Mesh Controller](https://hub.helm.sh/charts/aws/appmesh-controller)
- [Grafana](https://hub.helm.sh/charts/aws/appmesh-grafana)
- [Prometheus](https://hub.helm.sh/charts/aws/appmesh-prometheus)
- [Node Termination Handler](https://hub.helm.sh/charts/aws/aws-node-termination-handler)
- [Fluent Bit](https://hub.helm.sh/charts/aws/aws-for-fluent-bit)
- [VPC CNI](https://hub.helm.sh/charts/aws/aws-vpc-cni)

## Diagnostics

- [Kubernetes testing tools](https://github.com/ivankatliarchuk/kubetools#testing-tools)
- [Sonobuoy](https://github.com/vmware-tanzu/sonobuoy)
- [Jetstack Preflight](https://github.com/jetstack/preflight)
- [KuberHealthy](https://github.com/Comcast/kuberhealthy)
- [Canary checker](https://canarychecker.io/)
- [TestKube: dual license](https://docs.testkube.io/)

## Security

- [Security.info: Kubernetes Security](https://kubernetes-security.info/)
- [Kubernetes Attack Matrix](https://www.microsoft.com/en-us/security/blog/2020/04/02/attack-matrix-kubernetes/)
- [Kubernetes hardening(hardeneks)](https://github.com/aws-samples/hardeneks)
- [K8s cluster sanitizer](https://github.com/ik-kubernetes/popeye)
- [KubeHunter](https://github.com/aquasecurity/kube-hunter)
- [Kube Bench](https://github.com/aquasecurity/kube-bench)
- [TwistLock](https://www.twistlock.com/2018/06/21/securing-istio-twistlock/)
- [Kritis Supply Chain Software](https://github.com/grafeas/kritis)
- [Kubernetes Rules](https://github.com/circa10a/k8s-label-rules-webhook)
- [Scans live Kubernetes](https://github.com/derailed/popeye)
- [Kuberntes Inspection MKIT](https://github.com/darkbitio/mkit)
- [Policy Management](https://github.com/open-policy-agent/gatekeeper)
- [Kubi Scanner](https://github.com/cyberark/KubiScan)
- [Kube Scan](https://github.com/octarinesec/kube-scan)
- [Polaris](https://github.com/FairwindsOps/polaris)
- [StarBoard](https://github.com/aquasecurity/starboard)
- [Kubernetes Inspector](https://github.com/kinvolk/inspektor-gadget)
- [Docker Bench](https://github.com/docker/docker-bench-security)
- [K8s guard: Kubernetes Authentication & Authorization WebHook Server](https://github.com/appscode/guard)
- [Falco: runtime security](https://falco.org/docs/)
- [KubeScape: k8s security CIS](https://github.com/kubescape/kubescape)
- [InToto: supply chain security](https://in-toto.io/)
- [Capsule](https://capsule.clastix.io/docs/)

#### Networking

- [Kubeshark](https://github.com/kubeshark/kubeshark)

### Pod Security

- [Seccomp](https://kubesec.io/basics/metadata-annotations-seccomp-security-alpha-kubernetes-io-pod)
- [AppArmor](https://kubernetes.io/docs/tutorials/clusters/apparmor/)

### RBAC

- [Permission Manager](https://github.com/sighupio/permission-manager)
- [Krane](https://github.com/appvia/krane)

#### Keycloak and Authentic

- [Workshop](https://github.com/ibuetler/docker-keycloak-traefik-workshop)
- [SSO](https://www.slideshare.net/roidelapluie/single-sign-on-with-keycloak)
- [Authentic](https://charts.goauthentik.io)

## K8s manage Secrets

- [Workshop](https://github.com/aws-samples/aws-workshop-for-kubernetes/tree/master/04-path-security-and-networking/401-configmaps-and-secrets)
- [Go Daddy External Secrets](https://no.godaddy.com/engineering/2019/04/16/kubernetes-external-secrets/)
- [AWS Secret Operator](https://github.com/mumoshu/aws-secret-operator)
- [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets)
- [Helm Secrets](https://github.com/futuresimple/helm-secrets)
- [KubeSec](https://github.com/shyiko/kubesec)
- [Kamus](https://github.com/Soluto/kamus)

## K8s Terminal Tools

- [K9S](https://github.com/derailed/k9s)
- [Click Terminal](https://github.com/databricks/click)
- [KubeTop](https://github.com/LeastAuthority/kubetop)
- [Kubectl Starboard](https://github.com/aquasecurity/starboard#starboard-cli)
- [Inspector Gadget](https://github.com/kinvolk/inspektor-gadget/)

## K8s Bots

- [Bot Kube](https://github.com/kubeshop/botkube)

## Vendors to manage Clusters

- [Supergiant](https://supergiant.io/toolkit/)
- [GiantSwarm](https://www.giantswarm.io/)
- [OneInfra](https://github.com/ik-kubernetes/oneinfra)
- [Krucible](https://usekrucible.com/plans)
- [Digital.ai](https://docs.digital.ai/)

## Development

- [Transfer App To local machine. Telepresence](https://www.telepresence.io/)
- [Update Container from Local. KSync](https://vapor-ware.github.io/ksync/)
- [Debug Apps. KubectlDebug](https://github.com/aylei/kubectl-debug)
- [Debug. Squash](https://squash.solo.io/)
- [Sync](https://github.com/ksync/ksync)
- [Kube score](https://github.com/zegl/kube-score)

## Deployments

- [KubeCFG](https://github.com/bitnami/kubecfg)
- [Kustomize](https://github.com/kubernetes-sigs/kustomize)
- [Kapitan](https://github.com/deepmind/kapitan)
- [KubeZero](https://github.com/Zero-Down-Time/kubezero)
- [K8s at home](https://github.com/k8s-at-home/charts)
- [Klucctl](https://kluctl.io/)
- [Garden deploy](https://github.com/garden-io/garden)

## Multi Cloud

- [Crossplane](https://github.com/crossplane/crossplane)
- [Crossplane: UI(comoplane)](https://github.com/komodorio/komoplane)

## End of Life and Deprecations

- [End of life products](https://endoflife.date/amazon-eks)
- [Check Deprecation in k8s](https://github.com/FairwindsOps/pluto)
- [Kube Deprecations (kubent)](https://github.com/doitintl/kube-no-trouble)
- [Kube Deprecations (kubepug)](https://github.com/rikatz/kubepug)
- [Cluster Lint](https://github.com/digitalocean/clusterlint)

## Cluster Chores

- [Kubegrunt](https://github.com/gruntwork-io/kubergrunt#cleanup-security-group)
- [k8s scripts](https://github.com/ik-scripting/scripts/tree/master/k8s)

## Secrets

- [Infiscal: platform with secrets management](https://infisical.com)

## K8S Drainer

- [automatic-remediation-of-kubernetes-nodes](https://blog.cloudflare.com/automatic-remediation-of-kubernetes-nodes/)
- [Scurio: Alertmanager to Kubernetes Node conditions bridge ](https://github.com/cloudflare/sciuro)
- [Draino: drains nodes but does so based on Kubernetes node conditions](https://github.com/planetlabs/draino)
- [Node problem detector is a daemon that runs on each node that detects problems and reports them to the Kubernetes API.](https://github.com/kubernetes/node-problem-detector)
- [Kured: Kubernetes Reboot Daemon](https://github.com/kubereboot/kured)
