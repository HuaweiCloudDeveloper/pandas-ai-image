

<h1 align="center">pandas-ai智能数据分析助手</h1>
<p align="center">
  <a href="README.md"><strong>English</strong></a> | <strong>简体中文</strong>
</p>



## 目录

- [仓库简介](#项目介绍)
- [前置条件](#前置条件)
- [镜像说明](#镜像说明)
- [获取帮助](#获取帮助)
- [如何贡献](#如何贡献)

## 项目介绍

[pandas-ai](https://github.com/sinaptik-ai/pandas-ai) 是基于人工智能的数据分析增强工具，专为使用python和pandas进行数据处理和分析的用户打造。支持上传CSV文件，进行数据分析问答，提升工作效率。本商品基于鲲鹏服务器的Huawei Cloud EulerOS 2.0 64bit系统，提供开箱即用的pandas-ai。

## 核心特性

- **自然语言交互式数据分析：** 用户无需掌握 SQL 或 Python，只需用中文提问（如“销售额最高的城市是哪个？”），即可获得精准的数据洞察，显著降低数据分析门槛
- **深度集成华为 ModelArts MaaS 平台：** 支持通过 `base_url` 和 API Key 安全调用部署在华为云上的大模型（如 DeepSeek-R1），充分利用国产化 AI 基础设施能力，保障服务稳定与合规
- **轻量级 Web 可视化界面：** 基于 Streamlit 快速构建交互式前端，支持文件上传、问题输入、实时响应与历史记录展示，操作简洁直观，适合非技术用户使用
- **上下文感知的智能推理：** 系统自动提取 CSV 表头与前几行数据作为上下文注入提示词（prompt），使大模型能准确理解表格结构并生成合理回答

本项目提供的开源镜像商品[pandas-ai智能数据分析助手](https://marketplace.huaweicloud.com/hidden/contents/fac2ad81-404e-46ec-959c-221a692dda1d#productid=OFFI1144193316944424960) 已预先安装3.0.0-beta.17版本的pandas-ai及其相关运行环境，并提供部署模板。快来参照使用指南，轻松开启“开箱即用”的高效体验吧。

> **系统要求如下：**
>
> - CPU: 2vCPUs 或更高
> - RAM: 4GB 或更大
> - Disk: 至少 40GB

## 前置条件

[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## 镜像说明

| 镜像规格                                                     | 特性说明                                                 | 备注 |
| ------------------------------------------------------------ | -------------------------------------------------------- | ---- |
| [pandas-ai-3.0.0-beta.17-kunpeng](https://github.com/HuaweiCloudDeveloper/pandas-ai-image/tree/pandas-ai-3.0.0-beta.17-kunpeng) | 基于鲲鹏服务器 + Huawei Cloud EulerOS 2.0 64bit 安装部署 |      |

## 获取帮助

- 更多问题可通过 [issue](https://github.com/HuaweiCloudDeveloper/pandas-ai-image/issues) 或 华为云云商店指定商品的服务支持 与我们取得联系
- 其他开源镜像可看 [open-source-image-repos](https://github.com/HuaweiCloudDeveloper/open-source-image-repos)

## 如何贡献

- Fork 此存储库并提交合并请求
- 基于您的开源镜像信息同步更新 README.md
