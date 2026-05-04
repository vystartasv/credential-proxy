"""
Credential Proxy — Encrypted credential store for autonomous agents.

Solves the 1Password dead-end: agents call a local Unix socket daemon
instead of needing interactive Touch ID auth.

Usage:
    # CLI
    credential-proxy import-chrome ~/Downloads/Google\ Passwords.csv
    credential-proxy add github.com myuser mytoken
    credential-proxy get github.com
    credential-proxy serve  # Start daemon

    # Client library (from agent scripts)
    from credential_proxy.client import get_credential
    gh = get_credential("github.com")
"""

from .core import CredentialStore
