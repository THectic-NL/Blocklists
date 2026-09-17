import os, re, sys, glob, ipaddress
ok = True
def fail(m):
    global ok; ok = False; print("FAIL:", m)
# underscore labels are legal in DNS record names (_dmarc, _srv) and appear in the
# pre-existing TikTok list, so they are allowed here.
VALID = re.compile(r"^(?=.{1,253}$)(?!-)[a-z0-9_-]{1,63}(?<!-)(\.(?!-)[a-z0-9_-]{1,63}(?<!-))+$")
allow = {l.strip() for l in open("DNS/allowlist/domains.txt") if l.strip()}
for dom in sorted(glob.glob("DNS/*/domains.txt")):
    name = dom.split("/")[1]
    raw = open(dom).read(); lines = raw.splitlines()
    doms = [l for l in lines if l.strip()]
    if not raw.endswith("\n"): fail(f"{dom}: no final newline")
    if "\r" in raw: fail(f"{dom}: CRLF")
    if any(l != l.strip() for l in lines): fail(f"{dom}: stray whitespace")
    if len(doms) != len(set(doms)):
        d=[x for x in set(doms) if doms.count(x)>1]; fail(f"{dom}: duplicates {d[:3]}")
    # the allowlist is grouped by purpose by hand, so it is not expected to be sorted
    if name != "allowlist" and doms != sorted(doms): fail(f"{dom}: not sorted")
    bad = [d for d in doms if not VALID.match(d)]
    if bad: fail(f"{dom}: invalid entries {bad[:5]}")
    if name != "allowlist":
        clash = sorted(set(doms) & allow)
        if clash: fail(f"{dom}: also in allowlist: {clash[:5]}")
    hp = f"DNS/{name}/hosts.txt"; hraw = open(hp).read(); hl = hraw.splitlines()
    if not hraw.endswith("\n"): fail(f"{hp}: no final newline")
    if "\r" in hraw: fail(f"{hp}: CRLF")
    for i, l in enumerate(hl, 1):
        if l != l.rstrip(): fail(f"{hp}:{i}: trailing whitespace")
    hd = [l.split("\t",1)[1] for l in hl if l.startswith("0.0.0.0\t")]
    nonhost = [l for l in hl if l.strip() and not l.startswith(("#","0.0.0.0\t"))]
    if nonhost: fail(f"{hp}: malformed {nonhost[:3]}")
    if hd != doms: fail(f"{hp}: hosts/domains mismatch ({len(hd)} vs {len(doms)})")
    m = re.search(r"^# Total domains: (\d+)$", hraw, re.M)
    if not m: fail(f"{hp}: no Total domains header")
    elif int(m.group(1)) != len(doms): fail(f"{hp}: header {m.group(1)} != {len(doms)}")
    d = re.search(r"^# Last updated: (\S+)$", hraw, re.M)
    if not d: fail(f"{hp}: no Last updated")
    elif d.group(1) != "2026-09-17": fail(f"{hp}: stale date {d.group(1)}")
    print(f"  ok  {name:15s} {len(doms):5d}")
for ipf in sorted(glob.glob("IP/*/ips.txt")):
    raw = open(ipf).read()
    if not raw.endswith("\n"): fail(f"{ipf}: no final newline")
    if "\r" in raw: fail(f"{ipf}: CRLF")
    for i, l in enumerate(raw.splitlines(), 1):
        if l != l.rstrip(): fail(f"{ipf}:{i}: trailing whitespace")
    ips = [l.strip() for l in raw.splitlines() if l.strip() and not l.startswith("#")]
    for i in ips:
        try: ipaddress.ip_address(i)
        except ValueError:
            try: ipaddress.ip_network(i, strict=False)
            except ValueError: fail(f"{ipf}: not an IP/CIDR: {i}")
    if len(ips) != len(set(ips)):
        d=[x for x in set(ips) if ips.count(x)>1]; fail(f"{ipf}: duplicate IPs {d[:5]}")
    print(f"  ok  {ipf:28s} {len(ips):5d}")
print("\nRESULT:", "all checks passed" if ok else "PROBLEMS FOUND")
sys.exit(0 if ok else 1)
