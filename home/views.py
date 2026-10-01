from django.http import HttpResponse
import platform
import os
import shutil

def index(request):
    total, used, free = shutil.disk_usage("C:\\")
    storage = round(total / (1000 ** 3))

    data = [
        ("Reference no", "26018113"),
        ("Device Name", platform.node()),
        ("Processor", "Intel(R) Core(TM) 5 210H"),
        ("Platform", platform.system() + " " + platform.release()),
        ("CPU Cores (logical)", os.cpu_count()),
        ("Installed RAM", "16 GB"),
        ("Device Storage", "512 GB"),
        ("System Type", "64-bit Operating System"),
    ]

    output = "Device Specifications\n\n"
    for key, value in data:
        output += key + " : " + str(value) + "\n"

    return HttpResponse(output, content_type="text/plain")