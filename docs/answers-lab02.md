# Lab 02 — Câu hỏi thảo luận

### Câu 1: Vì sao phải đồng bộ `master` trước khi tạo hoặc merge Pull Request?

**Trả lời:**

Cần đồng bộ với `master` mới nhất để đảm bảo nhánh đang phát triển không bị lỗi thời so với mã nguồn chính.

Việc đồng bộ giúp:
- Phát hiện và giải quyết merge conflict sớm.
- Kiểm tra tính tương thích của chức năng mới với các thay đổi đã được merge vào `master`.
- Hạn chế lỗi phát sinh khi tích hợp Pull Request.


### Câu 2: Khi nào không được rebase?

**Trả lời:**

Không nên rebase các commit trên nhánh đã được chia sẻ và đang được người khác sử dụng, đặc biệt khi việc rebase sẽ thay đổi lịch sử commit mà họ đang dựa vào.
Nguyên nhân là `git rebase` tạo lại commit với SHA mới. Điều này có thể gây phân kỳ lịch sử, xung đột và buộc các thành viên phải đồng bộ lại.


### Câu 3: Branch `feature/*` khác `topic/*` như thế nào?

**Trả lời:**

Cả hai đều là nhánh được tạo từ `master` để phát triển độc lập và tích hợp thông qua Pull Request. Điểm khác biệt chủ yếu nằm ở mục đích sử dụng.

| Tiêu chí | `feature/*` | `topic/*` |
|---|---|---|
| Mục đích | Phát triển chức năng mới | Thực hiện một công việc cụ thể |
| Phạm vi | Thường liên quan đến chức năng phần mềm | Có thể là tài liệu, cấu hình hoặc công việc khác |
| Ví dụ | `feature/cart-print` | `topic/use-case-diagram` |
| Tích hợp | Pull Request vào `master` | Pull Request vào `master` |
