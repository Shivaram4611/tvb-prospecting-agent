import re
import dns.resolver

def get_mx_host(domain: str) -> str | None:
    """Checks if the company domain has active Mail Exchange (MX) records."""
    try:
        resolver = dns.resolver.Resolver()
        resolver.timeout = 2.0
        resolver.lifetime = 2.0
        records = resolver.resolve(domain, "MX")
        if records:
            return str(records[0].exchange).rstrip(".")
    except Exception:
        return None
    return None

def verify_email_format(email: str) -> bool:
    """Validates standard RFC syntax and blocks generic inboxes."""
    if not email or not isinstance(email, str):
        return False
    clean = email.strip().lower()

    # Disqualify non-executive addresses
    generic_prefixes = ["info@", "contact@", "support@", "admin@", "sales@", "hello@", "team@"]
    if any(clean.startswith(p) for p in generic_prefixes):
        return False

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, clean))

def resolve_founder_email(founder_name: str, domain: str) -> str | None:
    """
    Derives standard executive email patterns (first@domain or first.last@domain)
    and verifies that the target domain has live MX servers capable of receiving mail.
    Leaves the field blank (None) if unverified.
    """
    if not founder_name or not domain or "." not in domain:
        return None

    # Filter out generic placeholder phrases
    if any(term in founder_name.lower() for term in ["not specified", "unknown", "none", "n/a"]):
        return None

    clean_domain = domain.replace("https://", "").replace("http://", "").split("/")[0].replace("www.", "").strip()

    # Verify domain actually accepts mail
    mx = get_mx_host(clean_domain)
    if not mx:
        return None

    # Clean name tokens
    parts = [re.sub(r'[^a-zA-Z]', '', p.lower()) for p in founder_name.strip().split()]
    parts = [p for p in parts if p]
    if not parts:
        return None

    first = parts[0]
    last = parts[-1] if len(parts) > 1 else ""

    candidate = f"{first}.{last}@{clean_domain}" if last else f"{first}@{clean_domain}"

    if verify_email_format(candidate):
        return candidate

    return None