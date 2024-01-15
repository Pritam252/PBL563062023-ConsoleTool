import argparse
import requests

def main():
    print('PBL563062023 Configuration Tool.')

    parser = argparse.ArgumentParser(
        prog = 'PBL563062023-ConsoleTool',
        description = 'Console based Configuration Tool for Configuring the PBL563062023 Project wirelessly.',
        epilog = 'Every option here needs an IP address in the argument, example: [Command] [IP Address]'
    )

    #All the arguments:
    parser.add_argument('--code', type=str, help='Use this argument to change Lua Code on machine.')
    parser.add_argument('--sta_ssid', type=str, help='Use this argument to change WiFi Station mode SSID of machine.')
    parser.add_argument('--sta_pass', type=str, help='Use this argument to change WiFi Station mode password of machine.')
    parser.add_argument('--softap_ssid', type=str, help='Use this argument to change WiFi SoftAP mode SSID of machine.')
    parser.add_argument('--softap_pass', type=str, help='Use this argument to change WiFi SoftAP mode password on machine.')
    #REQUIRED.
    parser.add_argument('target_ip', type=str, help='[REQUIRED] Machine IP Address')

    args = parser.parse_args()

    args.target_ip = "http://" + args.target_ip

    #Now do the HTTP requests.
    if args.code:
        try:
            print("PBL Code upload tool:")
            requests.post(args.target_ip + "/code_post", args.code)
        finally:
            pass
    if args.sta_ssid:
        try:
            print("PBL Station SSID Modification Tool: ")
            print("Previous SSID: ")
            print(requests.get(args.target_ip + "/stationssid_get").content)
            requests.post(args.target_ip + "/stationssid_change", args.sta_ssid)
            print("SSID Changed.")
        finally:
            pass
    if args.sta_pass:
        try:
            print("PBL Station PASS Modification Tool: ")
            requests.post(args.target_ip + "/stationpass_change", args.sta_pass)
            print("Password changed.")
        finally:
            pass
    if args.softap_ssid:
        try:
            print("PBL SoftAP SSID Modification Tool: ")
            print("Previous SSID")
            print(requests.get(args.target_ip + "/softapssid_get").content)
            requests.post(args.target_ip + "/softapssid_change", args.softap_ssid)
            print("SSID changed.")
        finally:
            pass
    if args.softap_pass:
        try:
            print("PBL SoftAP PASS Modification Tool: ")
            requests.post(args.target_ip + "/softappass_change", args.softap_pass)
            print("Password changed.")
        finally:
            pass
main()
