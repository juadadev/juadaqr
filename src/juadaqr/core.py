import qrcode


def generate_qr_terminal(content: str):
    if not content:
        raise ValueError("Content is empty")

    qr = qrcode.QRCode(border=1)
    qr.add_data(content)
    qr.make(fit=True)

    import io

    output = io.StringIO()
    qr.print_ascii(out=output, invert=True)
    return output.getvalue()
