"""团队编排 —— 把员工与任务组装成可运行的部门。"""

from crewai import Crew, Process, Task

from .employees import analyst, researcher, writer


def build_research_crew(topic: str) -> Crew:
    """组建调研部，围绕 topic 执行三步 SOP。"""
    emp_researcher = researcher()
    emp_analyst = analyst()
    emp_writer = writer()

    task_research = Task(
        description=(
            f"围绕主题「{topic}」搜集关键信息：\n"
            "1. 领域现状与规模\n"
            "2. 主要参与者与代表案例\n"
            "3. 近期重要动态\n"
            "输出要点式的研究材料。"
        ),
        expected_output="要点式研究材料，包含现状、参与者、动态三部分",
        agent=emp_researcher,
    )

    task_analyze = Task(
        description=(
            f"基于研究员的材料，对「{topic}」做结构化分析：\n"
            "1. 核心趋势（2-3 条）\n"
            "2. 机会与风险\n"
            "3. 给决策者的建议\n"
            "输出分析结论。"
        ),
        expected_output="结构化分析：趋势、机会、风险、建议",
        agent=emp_analyst,
    )

    task_write = Task(
        description=(
            f"把分析结论整理成「{topic}」调研简报（Markdown 格式）：\n"
            "标题 + 摘要 + 趋势 + 机会与风险 + 建议，控制在 500 字以内。"
        ),
        expected_output="一份 500 字以内的 Markdown 调研简报",
        agent=emp_writer,
    )

    return Crew(
        agents=[emp_researcher, emp_analyst, emp_writer],
        tasks=[task_research, task_analyze, task_write],
        process=Process.sequential,
        verbose=True,
    )