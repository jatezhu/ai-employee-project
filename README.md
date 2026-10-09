# AI 员工项目（ai-employee-project）

基于 CrewAI 的数字员工平台原型 —— 把 AI 组织成有岗位、有流程、有交付的团队。

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置密钥（复制 .env.example 为 .env 并填入 OPENAI_API_KEY）

# 3. 试运行（不调用模型）
python main.py --dry-run

# 4. 正式运行：三位 AI 员工协作产出调研简报
python main.py "AI 员工行业趋势"
```

## 架构

```
main.py                    入口：解析参数、运行演示
ai_employee/
  employees.py             AI 员工定义（岗位档案）
  crews.py                 团队编排（员工 + 任务 + 流程）
output/                    交付成果（自动生成的简报）
```

## 当前团队（调研部）

| 工号 | 岗位 | 职责 |
|------|------|------|
| EMP-001 | 行业研究员 | 信息搜集 |
| EMP-002 | 战略分析师 | 洞察提炼 |
| EMP-003 | 报告撰写人 | 成果交付 |

## 路线图

- [x] 最小可运行原型（CrewAI 三员工协作）
- [ ] 消息渠道集成（企微/钉钉/飞书）
- [ ] 审批流（人类治理节点）
- [ ] 可视化 SOP 编排器
- [ ] 员工记忆与知识库

## 调研报告

详见 [docs/AI员工开源项目调研报告.md](docs/AI员工开源项目调研报告.md)