import socket
import multiprocessing

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            s.connect((host, port))
            return port
    except (socket.timeout, ConnectionRefusedError):
        return None

def scan_ports(host, start_port, end_port):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count() * 2)
    results = [pool.apply_async(scan_port, args=(host, port)) for port in range(start_port, end_port + 1)]
    open_ports = []
    num_results = len(results)
    for i in range(num_results):
        print(f"{i} / {num_results}    ({int(i*100/num_results)}%)")
        try:
            req = results[i].get()
        except OSError:
            continue
        if req is not None:
            open_ports.append(req)
    return open_ports
    