# Blocklists

DNS and IP blocklists for privacy and security. They block trackers, telemetry,
ads, scams and a handful of platforms at the network level.

The lists are split by what they match. Domain lists live under DNS/, IP lists
under IP/.

## Structure

| Folder | Matches | Use with |
|---|---|---|
| [DNS/](DNS/) | Domain names | Pi-hole, AdGuard Home, NextDNS, Unbound, dnsmasq |
| [IP/](IP/) | IP addresses and ranges | pfSense, OPNsense, iptables/nftables, router ACLs |

## DNS lists

Each list has its own folder under DNS/.

| Folder | Domains | Blocks |
|---|---|---|
| [DNS/tiktok/](DNS/tiktok/) | 6601 | TikTok, ByteDance |
| [DNS/meta/](DNS/meta/) | 38 | Facebook, Instagram, Meta tracking |
| [DNS/google/](DNS/google/) | 24 | Google Ads, Analytics, DoubleClick |
| [DNS/microsoft/](DNS/microsoft/) | 20 | Windows telemetry |
| [DNS/chinese-shops/](DNS/chinese-shops/) | 42 | Temu, AliExpress, Shein, Wish |
| [DNS/scam/](DNS/scam/) | 14 | Known scam and fraud sites |
| [DNS/tracking/](DNS/tracking/) | 31 | General tracking, Snapchat, Amazon Ads |
| [DNS/smart-tv/](DNS/smart-tv/) | 48 | Samsung, LG, Roku and Samba TV telemetry and ACR |
| [DNS/datto-kaseya/](DNS/datto-kaseya/) | 6 | Datto RMM, Kaseya |
| [DNS/allowlist/](DNS/allowlist/) | 139 | Domains that should never be blocked |

Each folder has two files. hosts.txt is for Pi-hole and AdGuard Home, with lines
like `0.0.0.0 domain.com`. domains.txt is a plain list for NextDNS and anything
else that takes one.

## IP lists

These block at the firewall instead of the resolver. See [IP/](IP/).

| Folder | IPs | Notes |
|---|---|---|
| [IP/datto-kaseya/](IP/datto-kaseya/) | 73 | Datto RMM and Kaseya addresses |

Each folder has an ips.txt with one address per line, ready for ipset/nftables,
pfSense/pfBlockerNG, OPNsense or a router ACL.

## Usage

NextDNS, with nextdnsctl:

```sh
pip install nextdnsctl
nextdnsctl auth <api-key>

# Replace the denylist with every blocklist
for list in tiktok meta google microsoft chinese-shops scam tracking smart-tv datto-kaseya; do
  nextdnsctl denylist import <profile-id> DNS/$list/domains.txt
done

# Replace the allowlist
nextdnsctl allowlist clear <profile-id> --yes
nextdnsctl allowlist import <profile-id> DNS/allowlist/domains.txt
```

Pi-hole or AdGuard Home, add the raw GitHub URLs as adlists:

```
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/tiktok/hosts.txt
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/meta/hosts.txt
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/google/hosts.txt
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/smart-tv/hosts.txt
```

## Other lists worth running

The lists here are small and specific on purpose, so it helps to run a big
general list next to them.

- HaGeZi Multi PRO++ for ads, trackers, phishing and malware
- OISD as an all-in-one
- AdGuard DNS Filter for ads and tracking
- EasyList and EasyPrivacy for general use
