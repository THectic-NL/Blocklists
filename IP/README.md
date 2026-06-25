# IP Blocklists

IP and CIDR blocklists for **firewall-level** blocking — pfSense, OPNsense,
`iptables`/`nftables`, router ACLs — as opposed to the domain-based DNS lists
in [`../DNS/`](../DNS/).

## Why a separate folder?

DNS blocklists stop *name resolution*; IP blocklists drop *traffic* to specific
addresses or ranges regardless of DNS. They protect different layers, so they
are kept apart: a DNS resolver can't enforce an IP list, and a firewall can't
read a hosts file.

## Lists

| Folder | IPs | Notes |
|---|---|---|
| [datto-kaseya/](datto-kaseya/) | 18 | Datto RMM / Kaseya IP fallback addresses — companion to [`../DNS/datto-kaseya/`](../DNS/datto-kaseya/) |

These IPs resolve to cloud infrastructure (AWS Global Accelerator / EC2 /
CloudFront) and can rotate over time, so re-verify them periodically. They are
provided as a fallback for blocking traffic even when DNS is bypassed.

## Recommended public IP blocklists

Until curated lists land here, these reputable feeds are good IP-layer sources:

- **[abuse.ch Feodo Tracker](https://feodotracker.abuse.ch/blocklist/)** — active botnet C2 IP addresses
- **[Spamhaus DROP / EDROP](https://www.spamhaus.org/drop/)** — hijacked and malicious netblocks
- **[FireHOL IP lists](https://github.com/firehol/blocklist-ipsets)** — aggregated IP reputation feeds
