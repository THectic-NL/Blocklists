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
| [smart-tv/](smart-tv/) | 310 | Smart-TV ACR ingest, the IP side of [../DNS/acr/](../DNS/acr/) |
| [datto-kaseya/](datto-kaseya/) | 69 | Datto RMM and Kaseya, the IP side of [../DNS/datto-kaseya/](../DNS/datto-kaseya/) |

The smart-TV list exists because a DNS block is not always enough there. Samsung
and LG sets carry resolver addresses in the firmware and several models fall back
to DNS-over-HTTPS when the resolver handed out over DHCP refuses to answer, so the
set never sees your Pi-hole. Redirect outbound port 53 and 853 back to your own
resolver at the router, and drop these addresses as well.

A good number of these addresses sit on shared CDNs like Cloudflare, Akamai and
AWS CloudFront, so they change over time and can also front unrelated sites. The
DNS list is the more reliable way to block Datto and Kaseya. Treat the IPs as a
backstop and re-check them now and then.

## Other IP lists worth running

If you want broader coverage at the IP layer, these are solid public feeds.

- abuse.ch Feodo Tracker for active botnet C2 addresses
- Spamhaus DROP and EDROP for hijacked and malicious netblocks
- FireHOL IP lists for aggregated reputation feeds
