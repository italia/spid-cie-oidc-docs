import hashlib
import base64
import secrets
import string

# https://datatracker.ietf.org/doc/html/rfc7636#section-4.1
def get_pkce(code_challenge_method: str = "S256", code_challenge_length: int = 64):
    hashers = {"S256": hashlib.sha256}
    alpha = string.ascii_letters + string.digits + "-._~"
    code_verifier_length = secrets.choice(range(43, 128 + 1))
    code_verifier = "".join([secrets.choice(alpha) for _ in range(code_verifier_length)])

    code_challenge = hashers.get(code_challenge_method)(
        code_verifier.encode("utf-8")
    ).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
    code_challenge = code_challenge.replace("=", "")

    return {
        "code_verifier": code_verifier,
        "code_challenge": code_challenge,
        "code_challenge_method": code_challenge_method,
    }
