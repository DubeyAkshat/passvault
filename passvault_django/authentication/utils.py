def normalize_email(email):
    # Removing leading and trailing spaces and Lowercasing the entire email address
    normalized_email = email.strip().lower()
    # Apply specific normalization rules (e.g., removing dots from the local part)
    local_part, domain = normalized_email.split('@')
    local_part = local_part.replace('.', '')
    normalized_email = f"{local_part}@{domain}"
    return normalized_email