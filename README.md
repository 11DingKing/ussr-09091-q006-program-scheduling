# 研学课程容量编排

项目面向纪念馆研学活动的课程、教室和讲解员资源编排。课程候选、资源锁定和通知是不同职责，时间计算统一使用带时区的时间值。

## 目录约定

- `src/program_scheduling/domain.py`：课程和资源的领域类型。
- `src/program_scheduling/`：约束计算、锁定和通知适配器。
- `tests/`：排课冲突和边界时间测试。

## 运行

需要 Python 3.11+，执行 `python -m unittest discover -s tests`。本地开发不要求容器运行时。
