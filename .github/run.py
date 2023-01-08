import os


if __name__ == "__main__":
    print("LinuxProfile!")
    print(os.environ.get("TEST"))
    print(os.getenv("TEST"))
