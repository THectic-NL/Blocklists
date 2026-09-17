#!/usr/bin/env python3
"""Enumerate Samsung/LG per-country ACR and ad endpoints over DNS.

Usage:  python3 acr-enum.py > live-hosts.txt
Writes enum-live.json alongside it with the resolved addresses.

Every pattern below returns NXDOMAIN for a nonsense label, so a hit is a real
individually provisioned record rather than a wildcard. Add patterns as vendors
add infrastructure; the country-code table is the expensive part and it is done.
"""
import socket, concurrent.futures as cf, sys, json

CC = """ad ae af ag ai al am ao ar as at au aw az ba bb bd be bf bg bh bi bj bm bn bo br bs bt bw by bz
ca cd cf cg ch ci ck cl cm cn co cr cu cv cw cy cz de dj dk dm do dz ec ee eg er es et fi fj fk fm fo fr
ga gb gd ge gf gg gh gi gl gm gn gp gq gr gt gu gw gy hk hn hr ht hu id ie il im in iq ir is it je jm jo jp
ke kg kh ki km kn kp kr kw ky kz la lb lc li lk lr ls lt lu lv ly ma mc md me mg mh mk ml mm mn mo mp mq mr
ms mt mu mv mw mx my mz na nc ne ng ni nl no np nr nu nz om pa pe pf pg ph pk pl pr ps pt pw py qa re ro rs
ru rw sa sb sc sd se sg si sk sl sm sn so sr ss st sv sx sy sz tc td tg th tj tm tn to tr tt tw tz ua ug uk
us uy uz va vc ve vg vi vn vu ws xk ye yt za zm zw eu apac emea latam sea mea global prd""".split()

EXTRA = ["eu1","eu2","eu3","eu4","eu5","eu6","eu7","eu8","us1","us2","us3","aic","eic","sic","jic","kic","nic","ric"]

def tpl(patterns):
    out = []
    for p in patterns:
        for c in CC + EXTRA:
            out.append(p.format(c=c))
    return out

PATTERNS = [
    # Samsung ACR regional ingest
    "acr-{c}-prd.samsungcloud.tv",
    "acr-{c}.samsungacr.com",
    "log-{c}.samsungacr.com",
    "osb-{c}svc.samsungqbe.com",
    # LG ad / data platform behind AWS
    "{c}-ad-lgsmartad-com.aws-prd.net",
    "{c}-info-lgsmartad-com.aws-prd.net",
    "{c}-rdx2-lgtvsdp-com.aws-prd.net",
    # LG service delivery platform
    "{c}.nextlgsdp.com",
    "{c}.lgtvsdp.com",
    "{c}.rdx2.lgtvsdp.com",
    "{c}.ad.lgsmartad.com",
    "{c}.info.lgsmartad.com",
    "{c}.lgsmartad.com",
    # LG webOS home-screen data / nudge / recommendation
    "{c}.cdpbeacon.lgtvcommon.com",
    "{c}.cdpsvc.lgtvcommon.com",
    "{c}.rdl.lgtvcommon.com",
    "{c}.nudge.lgtvcommon.com",
    "{c}.recommend.lgtvcommon.com",
    "{c}.service.lgtvcommon.com",
    "{c}.homeprv.lgtvcommon.com",
    "{c}.ibs.lgappstv.com",
    "{c}.lgrecommends.lgappstv.com",
]

hosts = sorted(set(tpl(PATTERNS)))
print(f"probing {len(hosts)} hostnames", file=sys.stderr)

def probe(h):
    try:
        ips = sorted({x[4][0] for x in socket.getaddrinfo(h, None)})
        return h, ips
    except Exception:
        return h, None

live = {}
with cf.ThreadPoolExecutor(max_workers=120) as ex:
    for h, ips in ex.map(probe, hosts):
        if ips:
            live[h] = ips

print(f"live: {len(live)}", file=sys.stderr)
json.dump(live, open("enum-live.json","w"), indent=0, sort_keys=True)
for h in sorted(live):
    print(h)
