    p = win32print.OpenPrinter('fax')
    job = win32print.StartDocPrinter(p, 1, ("test of raw data", None, "RAW"))
    win32print.StartPagePrinter(p)
    pr = win32print.WritePrinter(p, bytes(dic))
    win32print.EndPagePrinter(p)

    return JsonResponse(dic)

def get_printers():
    data = subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\n')
    print(data)
    data = data[1:]

    printers = []
    for lines in data:
        for printer in lines.split("  "):
            if (printer != ""):
                printers.append(printer)
                break

    return HttpResponse(json.dumps({"ptinter":printers}))
