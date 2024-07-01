import subprocess


class PipManager:
    @staticmethod
    def run_command(command):
        result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr

    def list_installed_packages(self):
        print("Listing installed packages...")
        output = self.run_command("pip list")
        print(output)

    def install_package(self, package_name):
        print(f"Installing package: {package_name}...")
        output = self.run_command(f"pip install {package_name}")
        print(output)

    def uninstall_package(self, package_name):
        print(f"Uninstalling package: {package_name}...")
        output = self.run_command(f"pip uninstall -y {package_name}")
        print(output)

    def update_package(self, package_name):
        print(f"Updating package: {package_name}...")
        output = self.run_command(f"pip install --upgrade {package_name}")
        print(output)

    def freeze_requirements(self, filename):
        print(f"Freezing requirements to {filename}...")
        output = self.run_command(f"pip freeze > {filename}")
        print(output)

    def install_requirements(self, filename):
        print(f"Installing packages from {filename}...")
        output = self.run_command(f"pip install -r {filename}")
        print(output)


def main():
    manager = PipManager()

    while True:
        print("\nPip Manager")
        print("1. 列出已安装包")
        print("2. 安装包")
        print("3. 卸载包")
        print("4. 升级包")
        print("5. 将当前环境中的包及其版本保存到指定文件")
        print("6. 从本地安装包")
        print("7. 退出")

        choice = input("键入你的选项: ")

        if choice == '1':
            manager.list_installed_packages()
        elif choice == '2':
            package_name = input("键入要安装包的名称: ")
            manager.install_package(package_name)
        elif choice == '3':
            package_name = input("键入要卸载包的名称: ")
            manager.uninstall_package(package_name)
        elif choice == '4':
            package_name = input("键入要更新包的名称: ")
            manager.update_package(package_name)
        elif choice == '5':
            filename = input("键入指定文件夹名称: ")
            manager.freeze_requirements(filename)
        elif choice == '6':
            filename = input("键入本地安装包: ")
            manager.install_requirements(filename)
        elif choice == '7':
            break
        else:
            print("无效的选项，请重试.")


if __name__ == "__main__":
    main()
