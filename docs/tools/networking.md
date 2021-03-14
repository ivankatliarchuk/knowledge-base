---
title: networking
summary: network tooling
authors: ["Ivan K"]
tags: ["tools", "network", "tcp", "dns", "lookup", "performance"]
date: 2021-03-8
published: true
---

!!! note "tcp ip udp"
    All sorts of networking tooling

- [Duck DNS: free dynamic DNS](https://www.duckdns.org/why.jsp){:target="_blank"}
- [Free DNS: static DNS subdomain and domain hosting](https://freedns.afraid.org){:target="_blank"}
- [Reverse IP: reverse IP Lookup tool will show you all of the domains currently hosted](http://reverseip.domaintools.com){:target="_blank"}

???+ summary "iPerf"
    [iPerf](https://iperf.fr/){:target="_blank"}
    iPerf3 is a tool for active measurements of the maximum achievable bandwidth(performance) on IP networks.

    ???+ success
        Install on first server
        ```
        yum --enablerepo=epel install iperf iperf3
        iperf3 -s -p 80
        ```

        Install on second server
        ```
        yum --enablerepo=epel install iperf iperf3
        iperf3 -c <ip> -i 1 -t 10 -p 80
        ```
