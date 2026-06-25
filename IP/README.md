# IP Blocklists

IP and CIDR blocklists for **firewall-level** blocking — pfSense, OPNsense,
`iptables`/`nftables`, router ACLs — as opposed to the domain-based DNS lists
in [`../DNS/`](../DNS/).

## Why a separate folder?

DNS blocklists stop *name resolution*; IP blocklists drop *traffic* to specific
addresses or ranges regardless of DNS. They protect different layers, so they
are kept apart: a DNS resolver can't enforce an IP list, and a firewall can't
read a hosts file.

## Status

No curated IP lists are published here yet.

The Datto / Kaseya entry is **domain-based** and lives in
[`../DNS/datto-kaseya/`](../DNS/datto-kaseya/). Reliable fallback-IP data for it
was not available to include here — those domains sit behind shared cloud
infrastructure (AWS / CloudFront), whose addresses rotate and are reused by
unrelated services, so blocking them by IP causes collateral damage. If you have
a trustworthy source of dedicated IPs, open an issue or PR and they'll be added.

## Recommended public IP blocklists

Until curated lists land here, these reputable feeds are good IP-layer sources:

- **[abuse.ch Feodo Tracker](https://feodotracker.abuse.ch/blocklist/)** — active botnet C2 IP addresses
- **[Spamhaus DROP / EDROP](https://www.spamhaus.org/drop/)** — hijacked and malicious netblocks
- **[FireHOL IP lists](https://github.com/firehol/blocklist-ipsets)** — aggregated IP reputation feeds
