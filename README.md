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
| [DNS/tiktok/](DNS/tiktok/) | 6916 | TikTok, ByteDance |
| [DNS/smart-tv/](DNS/smart-tv/) | 1955 | Everything a smart TV phones home: ACR, ads, telemetry |
| [DNS/acr/](DNS/acr/) | 765 | Automatic Content Recognition only, the narrow cut |
| [DNS/tracking/](DNS/tracking/) | 79 | General tracking, session replay, Snapchat, Amazon Ads |
| [DNS/chinese-shops/](DNS/chinese-shops/) | 62 | Temu, AliExpress, Shein, Wish |
| [DNS/meta/](DNS/meta/) | 51 | Facebook, Instagram, Threads, Meta tracking |
| [DNS/microsoft/](DNS/microsoft/) | 50 | Windows telemetry |
| [DNS/google/](DNS/google/) | 49 | Google Ads, Analytics, DoubleClick, Android TV |
| [DNS/scam/](DNS/scam/) | 14 | Known scam and fraud sites |
| [DNS/datto-kaseya/](DNS/datto-kaseya/) | 6 | Datto RMM, Kaseya |
| [DNS/allowlist/](DNS/allowlist/) | 137 | Domains that should never be blocked |

Each folder has two files. hosts.txt is for Pi-hole and AdGuard Home, with lines
like `0.0.0.0 domain.com`. domains.txt is a plain list for NextDNS and anything
else that takes one.

## About the TV lists

ACR is the fingerprinting built into the set. It samples what is on screen, or
the audio passing through it, hashes that, and sends the hash to the vendor to
be matched against a reference catalogue. What comes back is a second-by-second
record of what you watch, including input from a console, a Blu-ray player or a
laptop that was never online. Vendors sell that record or use it to target ads.

Two lists, because the trade-off is different:

- [DNS/acr/](DNS/acr/) is the narrow one. It blocks the fingerprint ingest
  endpoints and the ACR companies themselves, and leaves the app store, firmware
  updates, sign-in and the streaming apps alone. Start here.
- [DNS/smart-tv/](DNS/smart-tv/) is the superset and the aggressive one. It adds
  home-screen profiling, recommendation engines, diagnostics and usage telemetry
  for LG, Samsung, Sony, Panasonic, Philips, Hisense/VIDAA, TCL, Toshiba, Vizio,
  Roku, Fire TV and Xiaomi, plus HbbTV red-button tracking from broadcasters.

Most of the LG entries are per-country hostnames found by enumerating LG's
regional endpoints. Each one is an individually provisioned DNS record rather
than a wildcard, which is why they have to be listed out.

Two caveats worth knowing before you rely on this:

- **The allowlist can cancel part of it.** NextDNS matches allowlist entries
  against subdomains too, so an apex in [DNS/allowlist/](DNS/allowlist/) switches
  entries back on. The two LG apexes that did this have been removed;
  `samsungcloudsolution.com` and `samsung.com` stay and shadow 30 entries between
  them, because Samsung sign-in and the app store run on them. Pi-hole matches
  exactly and is unaffected.
- **The TV may not use your resolver.** Samsung and LG sets ship with DNS servers
  in the firmware and some fall back to DNS-over-HTTPS. Redirect outbound port 53
  and 853 to your own resolver at the router, and use
  [IP/smart-tv/](IP/smart-tv/) as the backstop.

## IP lists

These block at the firewall instead of the resolver. See [IP/](IP/).

| Folder | IPs | Notes |
|---|---|---|
| [IP/smart-tv/](IP/smart-tv/) | 315 | ACR ingest addresses, for TVs that bypass DNS |
| [IP/datto-kaseya/](IP/datto-kaseya/) | 69 | Datto RMM and Kaseya addresses |

Each folder has an ips.txt with one address per line, ready for ipset/nftables,
pfSense/pfBlockerNG, OPNsense or a router ACL.

## Usage

NextDNS, with nextdnsctl:

```sh
pip install nextdnsctl
nextdnsctl auth <api-key>

# Replace the denylist with every blocklist
for list in tiktok meta google microsoft chinese-shops scam tracking acr smart-tv datto-kaseya; do
  nextdnsctl denylist import <profile-id> DNS/$list/domains.txt
done

# Replace the allowlist
nextdnsctl allowlist clear <profile-id> --yes
nextdnsctl allowlist import <profile-id> DNS/allowlist/domains.txt
```

Pi-hole or AdGuard Home, add the raw GitHub URLs as adlists:

```
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/acr/hosts.txt
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/smart-tv/hosts.txt
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/tiktok/hosts.txt
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/meta/hosts.txt
https://raw.githubusercontent.com/THectic-NL/Blocklists/main/DNS/google/hosts.txt
```

## Other lists worth running

The lists here are specific on purpose, so it helps to run a big general list
next to them.

- HaGeZi Multi PRO++ for ads, trackers, phishing and malware
- OISD as an all-in-one
- AdGuard DNS Filter for ads and tracking
- EasyList and EasyPrivacy for general use
