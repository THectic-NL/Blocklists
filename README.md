# DNS Block Lists

DNS blocklists for ads, tracking, and unwanted domains.

## Lists

Each list lives in its own folder with two formats:

| Folder | Domains | Blocks |
|---|---|---|
| [tiktok/](tiktok/) | 6601 | TikTok, ByteDance |
| [meta/](meta/) | 38 | Facebook, Instagram, Meta tracking |
| [google/](google/) | 24 | Google Ads, Analytics, DoubleClick |
| [microsoft/](microsoft/) | 20 | Windows telemetry |
| [chinese-shops/](chinese-shops/) | 42 | Temu, AliExpress, Shein, Wish |
| [scam/](scam/) | 14 | Known scam/fraud sites |
| [tracking/](tracking/) | 31 | General tracking, Snapchat, Amazon Ads |
| [smart-tv/](smart-tv/) | 48 | Samsung/LG/Roku/Samba TV telemetry & ACR |
| [datto-kaseya/](datto-kaseya/) | 6 | Datto RMM, Kaseya |
| [allowlist/](allowlist/) | 139 | Explicitly allowed domains |

Each folder contains:
- `hosts.txt` — hosts file format (`0.0.0.0 domain.com`), for Pi-hole and AdGuard Home
- `domains.txt` — plain domain list, for NextDNS and other tools

## Usage

**NextDNS** — via [nextdnsctl](https://github.com/danielmeint/nextdnsctl):

```sh
pip install nextdnsctl
nextdnsctl auth <api-key>

# Replace denylist with all blocklists
for list in tiktok meta google microsoft chinese-shops scam tracking smart-tv datto-kaseya; do
  nextdnsctl denylist import <profile-id> $list/domains.txt
done

# Replace allowlist
nextdnsctl allowlist clear <profile-id> --yes
nextdnsctl allowlist import <profile-id> allowlist/domains.txt
```

**Pi-hole / AdGuard Home** — add the raw GitHub URLs as adlists:

```
https://raw.githubusercontent.com/THectic-NL/DNS-Blocklists/main/tiktok/hosts.txt
https://raw.githubusercontent.com/THectic-NL/DNS-Blocklists/main/meta/hosts.txt
https://raw.githubusercontent.com/THectic-NL/DNS-Blocklists/main/google/hosts.txt
https://raw.githubusercontent.com/THectic-NL/DNS-Blocklists/main/smart-tv/hosts.txt
```

## Recommended public lists

- **HaGeZi Multi PRO++** — ads, trackers, phishing, malware
- **OISD** — all-in-one
- **AdGuard DNS Filter** — ads and tracking
- **EasyList + EasyPrivacy** — general purpose
