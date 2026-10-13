import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Lỗi khi chạy lệnh: {e}"

def check_docker():
    print("--- Kiểm tra Docker ---")
    print("Docker Version:")
    print(run_command("docker version --format '{{.Server.Version}}'"))
    print("\nDocker Info (Cgroup Driver):")
    print(run_command("docker info | grep -i cgroup"))

if __name__ == '__main__':
    check_docker()