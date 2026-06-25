# IP Blocklists

IP and CIDR lists for blocking at the firewall, so pfSense, OPNsense, iptables or
nftables, or a router ACL. The domain based DNS lists are in [../DNS/](../DNS/).

## Why this is separate from DNS

A DNS blocklist stops a name from resolving. An IP list drops traffic to an
address whatever DNS says. They work at different layers. A resolver cannot read
an IP list and a firewall cannot read a hosts file, so it is cleaner to keep them
apart.

## Lists

| Folder | IPs | Notes |
|---|---|---|
| [datto-kaseya/](datto-kaseya/) | 73 | Datto RMM and Kaseya, the IP side of [../DNS/datto-kaseya/](../DNS/datto-kaseya/) |

A good number of these addresses sit on shared CDNs like Cloudflare, Akamai and
AWS CloudFront, so they change over time and can also front unrelated sites. The
DNS list is the more reliable way to block Datto and Kaseya. Treat the IPs as a
backstop and re-check them now and then.

## Other IP lists worth running

If you want broader coverage at the IP layer, these are solid public feeds.

- abuse.ch Feodo Tracker for active botnet C2 addresses
- Spamhaus DROP and EDROP for hijacked and malicious netblocks
- FireHOL IP lists for aggregated reputation feeds
