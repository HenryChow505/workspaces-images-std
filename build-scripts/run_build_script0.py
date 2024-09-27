import yaml
import subprocess

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
        "bash", "build.sh",
        name, base, dockerfile
    ]

    # 打印命令以供调试
    print("Running command:", " ".join(command))

    # 执行命令
    result = subprocess.run(command, capture_output=True, text=True)

    # 打印输出
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

    # 检查命令是否成功
    if result.returncode != 0:
        raise Exception(f"Command failed with return code {result.returncode}")

# 从 YAML 文件中加载数据
with open('images0.yaml', 'r') as file:
    data = yaml.safe_load(file)

# 获取镜像信息列表
images = data.get("images", [])

# 遍历镜像信息列表并运行脚本
for image in images:
    try:
        run_build_script(image)
    except Exception as e:
        print(f"Failed to build image {image['name1']} {image['name2']}: {e}")