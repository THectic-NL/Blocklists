# Blocklists

Curated **DNS and IP blocklists for privacy and security** — block trackers,
telemetry, ads, scams, and unwanted platforms at the network level.

> Lists are split by what they match: **domains** live under [`DNS/`](DNS/),
> **IP addresses / ranges** under [`IP/`](IP/).

## Structure

| Folder | Layer | Use with |
|---|---|---|
| [`DNS/`](DNS/) | Domain names | Pi-hole, AdGuard Home, NextDNS, Unbound, dnsmasq |
| [`IP/`](IP/) | IP addresses / CIDR | pfSense, OPNsense, `iptables`/`nftables`, router ACLs |

## DNS lists

Each list lives in its own folder under [`DNS/`](DNS/):

| Folder | Domains | Blocks |
|---|---|---|
| [DNS/tiktok/](DNS/tiktok/) | 6601 | TikTok, ByteDance |
| [DNS/meta/](DNS/meta/) | 38 | Facebook, Instagram, Meta tracking |
| [DNS/google/](DNS/google/) | 24 | Google Ads, Analytics, DoubleClick |
| [DNS/microsoft/](DNS/microsoft/) | 20 | Windows telemetry |
| [DNS/chinese-shops/](DNS/chinese-shops/) | 42 | Temu, AliExpress, Shein, Wish |
| [DNS/scam/](DNS/scam/) | 14 | Known scam/fraud sites |
| [DNS/tracking/](DNS/tracking/) | 31 | General tracking, Snapchat, Amazon Ads |
| [DNS/smart-tv/](DNS/smart-tv/) | 48 | Samsung/LG/Roku/Samba TV telemetry & ACR |
| [DNS/datto-kaseya/](DNS/datto-kaseya/) | 6 | Datto RMM, Kaseya |
| [DNS/allowlist/](DNS/allowlist/) | 139 | Explicitly allowed domains |

Each folder contains:
- `hosts.txt` — hosts file format (`0.0.0.0 domain.com`), for Pi-hole and AdGuard Home
- `domains.txt` — plain domain list, for NextDNS and other tools

## IP lists

For firewall-level blocking (rather than DNS resolvers), see [`IP/`](IP/):

| Folder | IPs | Notes |
|---|---|---|
| [IP/datto-kaseya/](IP/datto-kaseya/) | 18 | Datto RMM / Kaseya IP fallback addresses |

Each folder contains `ips.txt` — a plain IP list for `ipset`/`nftables`,
pfSense/pfBlockerNG, OPNsense, and router ACLs.

## Usage

**NextDNS** — via [nextdnsctl](https://github.com/danielmeint/nextdnsctl):

```sh
pip install nextdnsctl
nextdnsctl auth <api-key>

# Replace denylist with all blocklists
for list in tiktok meta google microsoft chinese-shops scam tracking smart-tv datto-kaseya; do
  nextdnsctl denylist import <profile-id> DNS/$list/domains.txt
done

# Replace allowlist
nextdnsctl allowlist clear <profile-id> --yes
nextdnsctl allowlist import <profile-id> DNS/allowlist/domains.txt
```

**Pi-hole / AdGuard Home** — add the raw GitHub URLs as adlists:

```
https://raw.githubusercontent.com/THectic-NL/DNS-Blocklists/main/DNS/tiktok/hosts.txt
https://raw.githubusercontent.com/THectic-NL/DNS-Blocklists/main/DNS/meta/hosts.txt
https://raw.githubusercontent.com/THectic-NL/DNS-Blocklists/main/DNS/google/hosts.txt
https://raw.githubusercontent.com/THectic-NL/DNS-Blocklists/main/DNS/smart-tv/hosts.txt
```

> If the repository is renamed to `Blocklists`, GitHub auto-redirects the old
> URLs above, so existing adlists keep working — swap `DNS-Blocklists` for
> `Blocklists` at your convenience.

## Recommended public lists

For broad coverage, pair these curated lists with a comprehensive public feed:

- **HaGeZi Multi PRO++** — ads, trackers, phishing, malware
- **OISD** — all-in-one
- **AdGuard DNS Filter** — ads and tracking
- **EasyList + EasyPrivacy** — general purpose
