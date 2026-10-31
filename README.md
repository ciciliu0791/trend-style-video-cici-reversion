# Trend Style Video

参考驱动的视频创作技能：统一分析 Hook、观感、风格与主要吸引点，再确认采用“复刻”还是“改写故事”。

## 入口

- [统一技能入口](.trae/skills/trend-style-video/SKILL.md)
- [共享分析正文](Skills/viral-remake-skill/prompts/analysis.md)
- [复刻与改写故事交互](.trae/skills/trend-style-video/references/adaptation-modes.md)
- [项目模板](.trae/skills/trend-style-video/assets/PROJECT.template.md)
- [工作区 Viral 兼容入口](Skills/viral-remake-skill/SKILL.md)

两种模式都保留选定的 Hook、观感、风格关系和主要吸引机制。复刻侧重保留主要段落、镜头功能、动作调度与节奏；改写故事允许重新设计剧情、镜头顺序和结尾。用户已明确选择时不重复询问；只做分析时不强制选择或启动生成。

## 使用

将整个仓库作为项目工作区打开，或保留相对目录结构接入自己的项目。不要只复制 `.trae/skills/trend-style-video`，它引用了 `Skills/` 中的共享分析、分镜及项目控制文件。

示例请求：

> 分析这段参考视频的 Hook、观感、风格和吸引点，然后让我选择复刻还是改写故事。

> 改写一个新故事，但保留参考片的仪式感、反差和节奏。

## 范围与依赖

本仓库是技能源码快照，不包含完整视频生产环境。附带工作区 Viral、Cici 项目控制和短剧设计依赖；不包含全局版 Viral、模型凭据、输入素材、历史生成结果或真实生产批准包。

- 生成优先使用独立 Seedance/Seedream MCP，可用性不足时按技能要求使用独立 BytePlus `arkcli`。工具需在使用环境中另行配置。
- HyperFrames 等外部工具技能不随本仓库分发。
- 历史 Viral 脚本适配器仍仅支持其文档声明的服务，不因分析合并而获得 BytePlus 支持。
- `AGENTS.md` 保留原工作区规则背景，但已移除私人素材文件夹地址。历史授权不能转移给新用户或新项目。
- Manyue 身份素材、系列规则及 `videos/`、`ProjectPlan/` 中的私人案例未包含。文档中指向这些历史记录的引用仅在原工作区可访问；不能据此声称已查阅原始证据。普通新项目不需要这些案例素材。
- 原始技能、参考方法及出处保留；本次上传不另行授予第三方内容的许可，也不代表可以公开再分发私人案例。

## 验证

需要 Python 3.9+。Viral 的媒体测试还需要 ffmpeg/ffprobe 和其 `requirements.txt` 所列依赖。

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s Skills/viral-remake-skill/tests -v
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s Skills/cinematic-project-skills-cici/tests -v
```

这些是离线兼容性与项目状态测试，不证明模型生成效果。模式行为另见统一技能的验收场景。

## 更新

此目录是独立 Git 仓库副本，不会自动同步原工作区中的后续修改。更新时只同步技能源文件和必要依赖，复核差异后提交；不要同步输入、运行记录、素材、凭据或缓存。
