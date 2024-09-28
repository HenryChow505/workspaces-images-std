import yaml
import subprocess
import sys

def run_build_script(image):
    """
    运行 build.sh 脚本并传递相应的参数。

    :param image: 包含镜像信息的字典
    """
    name = image.get("name")
    base = image.get("base")
    dockerfile = image.get("dockerfile")

    # 构建命令
    command = [
        "bash", "build-scripts/build.sh",
        name, base, dockerfile
    ]

    # 打印命令以供调试
    print("Running command:", " ".join(command))

    # 执行命令并实时打印输出build-scripts/
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True) as process:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip(), flush=True)

    # 检查命令是否成功
    if process.returncode != 0:
        raise Exception(f"Command failed with return code {process.returncode}")

# 从 YAML 文件中加载数据
with open('build-scripts/images.yaml', 'r') as file:
    data = yaml.safe_load(file)

# 获取镜像信息列表
images = data.get("images", [])

# 遍历镜像信息列表并运行脚本
for image in images:
    try:
        run_build_script(image)
    except Exception as e:
        print(f"Failed to build image {image['name']} {image['base']}: {e}")