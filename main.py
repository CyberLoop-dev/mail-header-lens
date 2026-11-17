import argparse,json
from email import policy
from email.parser import BytesParser
from pathlib import Path
def inspect(path):
 m=BytesParser(policy=policy.default).parsebytes(Path(path).read_bytes())
 sender=m.get("From",""); reply=m.get("Reply-To","")
 return {"from":sender,"reply_to":reply,"received":m.get_all("Received",[]),"auth_results":m.get_all("Authentication-Results",[]),"warning":"Header claims are not cryptographic verification." if m.get_all("Authentication-Results") else "No Authentication-Results header found."}
def main():
 p=argparse.ArgumentParser(description="Inspect a local .eml message");p.add_argument("message");p.add_argument("--json",action="store_true");a=p.parse_args();d=inspect(a.message)
 print(json.dumps(d,indent=2) if a.json else f"From: {d['from']}\\nReply-To: {d['reply_to']}\\nReceived hops: {len(d['received'])}\\nAuth results: {d['auth_results']}\\n{d['warning']}")
if __name__=="__main__":main()
