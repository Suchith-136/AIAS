import re

"""
Task_1.py

Invoice summarizer: extract invoice number, tax, and total amount from free-form text.

Refined approach (prompt summary used to design extractor):
- Find invoice identifiers by looking for common invoice patterns (e.g. INV-YYYYMMDD-###)
    and generic "Invoice No/Number" patterns.
- Find monetary amounts with currency symbols or comma/decimal formatting.
- Classify amounts by nearby context words: "tax", "total", "subtotal", "amount due", "payable".
- If classification is ambiguous, choose the largest amount as total; if tax missing but
    subtotal and total present, compute tax = total - subtotal.
- Normalize numeric values to floats.

This module provides:
- extract_invoice_fields(text): returns dict with invoice_number (str|None),
    total (float|None), tax (float|None), subtotal (float|None)
- unit tests run when executed as a script.
"""


def _parse_amount(amount_str):
        """Convert an amount like '$1,320.00' or '1,320.00' to float."""
        if amount_str is None:
                return None
        s = amount_str.strip()
        s = re.sub(r'[$€£\s]', '', s)      # remove common currency symbols and spaces
        s = s.replace(',', '')             # remove thousands separators
        try:
                return float(s)
        except Exception:
                return None

def find_invoice_number(text):
        """Attempt to extract an invoice number from text using common patterns."""
        if not text:
                return None
        # First, try explicit INV... style identifiers. Require a hyphen or digit
        # immediately after 'INV' to avoid matching words like 'Invoice'.
        m = re.search(r'\bINV(?:-|\d)[A-Z0-9\-\./]{2,}\b', text, flags=re.IGNORECASE)
        if m:
                return m.group(0).strip()

        # Otherwise, scan occurrences of the word 'invoice' and look for a token
        # following it that looks like an identifier (skip common filler words).
        for inv in re.finditer(r'\binvoice\b', text, flags=re.IGNORECASE):
                start = inv.end()
                tail = text[start:start + 80]  # look ahead a short distance
                # split into tokens
                tokens = re.split(r'[\s,:;\-\u2013\u2014]+', tail)
                skip = {'no', 'no.', 'number', 'invoice', ''}
                for tok in tokens:
                        t = tok.strip()
                        if not t:
                                continue
                        low = t.lower()
                        if low in skip:
                                continue
                        # Accept tokens that contain letters or digits and are reasonably long
                        if re.search(r'[A-Za-z0-9]', t) and len(t) >= 3:
                                # strip punctuation from ends
                                t2 = t.strip(' .:;,')
                                if not t2.lower().startswith('invoice'):
                                        return t2

        # Final fallback: look for a generic invoice-like token anywhere
        m = re.search(r'\b[A-Z]{2,}-?\d{3,}\b', text, flags=re.IGNORECASE)
        if m:
                return m.group(0).strip()

        return None

def extract_invoice_fields(text):
        """
        Extract invoice_number, total, tax, and subtotal from text.

        Returns a dict:
            {
                "invoice_number": str | None,
                "total": float | None,
                "tax": float | None,
                "subtotal": float | None
            }

        Strategy:
        - Find all monetary amounts and classify by context words nearby.
        - Use fallbacks (largest amount => total; compute tax from subtotal & total).
        """
        if not text:
                return {"invoice_number": None, "total": None, "tax": None, "subtotal": None}

        invoice_number = find_invoice_number(text)

        # Regex to find amounts like $1,320.00 or 1,320.00 or £120.00
        amount_re = re.compile(r'(?P<full>(?P<sym>[$€£])?\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?)')
        # To avoid picking up numeric fragments that are part of invoice identifiers
        # (e.g. INV-20251120-003), blank out invoice-like tokens in a copy of the text
        scan_text = text
        if invoice_number:
                scan_text = re.sub(re.escape(invoice_number), lambda m: ' ' * len(m.group(0)), scan_text, flags=re.IGNORECASE)
        # blank out any other INV-like tokens
        scan_text = re.sub(r'\bINV[^\s,;:()]+', lambda m: ' ' * len(m.group(0)), scan_text, flags=re.IGNORECASE)
        candidates = []
        for m in amount_re.finditer(scan_text):
                full = m.group('full')
                start, end = m.span()
                # Examine small and larger left/right windows to decide the role.
                left_small = text[max(0, start - 12): start].lower()
                right_small = text[end: end + 12].lower()
                left_large = text[max(0, start - 60): start].lower()
                right_large = text[end: end + 60].lower()
                role = None
                # Tax: prefer matches where 'tax' immediately precedes the amount
                # (e.g. 'Tax: $120.00'). Do not label an amount as tax just because
                # the word 'tax' follows it elsewhere.
                if re.search(r'tax\s*[:\)]?\s*$', left_small):
                        role = 'tax'
                # Subtotal: search in a larger window for words like 'subtotal'
                elif re.search(r'subtotal|sub total', left_large) or re.search(r'subtotal|sub total', right_large):
                        role = 'subtotal'
                # Total: look for 'total' or related phrases in a reasonable window, or 'amount (including tax)'
                elif re.search(r'total\b|amount due|total payable|amount payable', left_small) or re.search(r'total\b|amount due|total payable|amount payable', right_small) or re.search(r'amount \(including tax\)', (left_large + right_large)):
                        role = 'total'
                candidates.append({
                        'raw': full.strip(),
                        'value': _parse_amount(full),
                        'role': role,
                        'context': (left_large + ' | ' + right_large).strip()
                })

        # (amount candidates available in candidates list)

        # Prepare containers
        total = None
        tax = None
        subtotal = None

        # Prefer explicitly labeled amounts
        for c in candidates:
                if c['role'] == 'total' and c['value'] is not None:
                        # If multiple totals, choose the largest labeled total
                        if total is None or (c['value'] > total):
                                total = c['value']
                if c['role'] == 'tax' and c['value'] is not None:
                        if tax is None or (c['value'] > tax):
                                tax = c['value']
                if c['role'] == 'subtotal' and c['value'] is not None:
                        if subtotal is None or (c['value'] > subtotal):
                                subtotal = c['value']

        # If no explicit total, choose largest numeric amount
        if total is None:
                numeric_vals = [c['value'] for c in candidates if c['value'] is not None]
                if numeric_vals:
                        total = max(numeric_vals)

        # If tax missing but subtotal and total present, compute tax
        if tax is None and subtotal is not None and total is not None:
                calc_tax = round(total - subtotal, 2)
                # only accept positive reasonable tax
                if calc_tax >= 0:
                        tax = calc_tax

        return {
                "invoice_number": invoice_number,
                "total": total,
                "tax": tax,
                "subtotal": subtotal
        }

# ----------------------------
# Test cases
# ----------------------------
def _run_tests():
        example_text = """
        Invoice No. INV-20251120-003 — Tax: $120.00 — Total Amount (including tax): $1,320.00.
        This invoice, numbered INV-20251120-003, requires the payment of the stated total amount in full.
        Please note the tax applied to this transaction is $120.00 and is included in the total amount.
        The subtotal before tax for this invoice equals $1,200.00, with tax calculated at $120.00.
        Payment for Invoice No. INV-20251120-003 should be remitted within 30 days of the invoice date.
        """
        res = extract_invoice_fields(example_text)
        assert res['invoice_number'] and res['invoice_number'].upper().startswith('INV-20251120-003'), f"invoice_number mismatch: {res['invoice_number']}"
        assert abs(res['tax'] - 120.00) < 1e-6, f"tax mismatch: {res['tax']}"
        assert abs(res['total'] - 1320.00) < 1e-6, f"total mismatch: {res['total']}"
        assert abs(res['subtotal'] - 1200.00) < 1e-6, f"subtotal mismatch: {res['subtotal']}"

        # Additional variants
        t2 = "Invoice: INV12345 Total: $2,000.00 Tax $200.00"
        r2 = extract_invoice_fields(t2)
        assert r2['invoice_number'] is not None and r2['invoice_number'].upper().startswith('INV12345')
        assert abs(r2['total'] - 2000.0) < 1e-6
        assert abs(r2['tax'] - 200.0) < 1e-6

        t3 = "Invoice Number: 2025-0001 Amount due $500.00"
        r3 = extract_invoice_fields(t3)
        assert r3['invoice_number'] is not None
        assert abs(r3['total'] - 500.0) < 1e-6

        t4 = "Total payable: £1,750.00. Tax: £150.00. Invoice No INV-0002"
        r4 = extract_invoice_fields(t4)
        assert r4['invoice_number'] is not None and 'INV-0002' in r4['invoice_number']
        assert abs(r4['total'] - 1750.0) < 1e-6
        assert abs(r4['tax'] - 150.0) < 1e-6

        print("All tests passed.")

if __name__ == '__main__':
        import sys
        # Simple CLI argument parsing: --test to run tests, --text/-t to pass paragraph
        if len(sys.argv) > 1 and sys.argv[1] == '--test':
                _run_tests()
                sys.exit(0)

        # Check for --text or -t argument (takes the rest of the arg as the paragraph)
        text = None
        argv = sys.argv[1:]
        if argv:
                # look for --text or -t
                for i, a in enumerate(argv):
                        if a in ('--text', '-t') and i + 1 < len(argv):
                                text = argv[i + 1]
                                break
                        # support --text="some paragraph"
                        if a.startswith('--text='):
                                text = a.split('=', 1)[1]
                                break

        # If no text provided via arg, read from stdin if piped
        if text is None and not sys.stdin.isatty():
                text = sys.stdin.read()

        # Otherwise prompt interactively
        if text is None:
                print("Enter the paragraph. Finish with Ctrl+Z then Enter (Windows) or Ctrl+D (Unix):")
                lines = []
                try:
                        while True:
                                line = input('> ')
                                lines.append(line)
                except EOFError:
                        pass
                text = "\n".join(lines)

        res = extract_invoice_fields(text)
        print()
        print(f"Invoice No: {res['invoice_number']}")
        print(f"Tax: {res['tax']}")
        print(f"Subtotal: {res['subtotal']}")
        print(f"Total: {res['total']}")