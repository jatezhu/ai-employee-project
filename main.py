"""AI 员工项目入口 —— 运行最小可执行演示。"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from ai_employee.crews import build_research_crew


def main() -> int:
    parser = argparse.ArgumentParser(description="AI 员工调研部演示")
    parser.add_argument("topic", nargs="?", default="AI 员工行业趋势", help="调研主题")
    parser.add_argument("--dry-run", action="store_true", help="仅打印执行计划，不调用模型")
    args = parser.parse_args()

    load_dotenv()

    if not args.dry_run and not os.getenv("OPENAI_API_KEY"):
        print("未检测到 OPENAI_API_KEY，请复制 .env.example 为 .env 并填入密钥，或使用 --dry-run")
        return 1

    print("=" * 60)
    print("AI 员工调研部 · 最小可运行原型")
    print(f"主题：{args.topic}")
    print("=" * 60)

    crew = build_research_crew(args.topic)

    if args.dry_run:
        print("\n[执行计划]")
        for i, task in enumerate(crew.tasks, 1):
            print(f"  步骤 {i}：{task.agent.role} —— {task.description[:40]}...")
        print("\n（dry-run 模式：未调用模型）")
        return 0

    print("\n[开始协作] 三位 AI 员工将依次完成：研究 → 分析 → 撰稿\n")
    result = crew.kickoff()

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"简报_{timestamp}.md"
    output_file.write_text(str(result), encoding="utf-8")

    print("\n" + "=" * 60)
    print(f"[交付完成] 报告已保存：{output_file}")
    print("=" * 60)
    print(str(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())