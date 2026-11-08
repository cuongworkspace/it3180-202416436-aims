# AIMS-mini

**IT3180 — Software Configuration Management | Git & GitHub Labs**

Repository thực hành quản lý cấu hình phần mềm bằng Git và GitHub trên dự án AIMS-mini (Python).

## Labs

| Lab | Nội dung |
|---|---|
| Lab 01 | Git fundamentals & Refactor Flow |
| Lab 02 | Feature/Topic Flow & Pull Requests |
| Lab 03 | Bugfix Flow, Merge Conflict & Revert |
| Lab 04 | Release Flow, Semantic Versioning & Tags |
| Lab 05 | Hotfix Flow, Cherry-pick & GitHub Actions CI |

## Run

```bash
python main.py
```

## Unit Tests

```bash
python -m unittest discover -s tests -v
```

## Releases

- `v0.1.0` — Lab 01
- `v0.2.0` — Lab 02
- `v0.3.0` — Lab 03
- `v1.0.0` — Lab 04
- `v1.0.1` — Hotfix
- `v1.1.0` — Lab 05

## Documentation

Bài trả lời thảo luận được lưu trong thư mục `docs/answers-labXX.md`.

## CI

GitHub Actions chạy unit tests khi có Pull Request vào `master` hoặc các nhánh `release/*`, và khi có commit được push lên `master`.