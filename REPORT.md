# Báo cáo kỹ thuật: Chuyển đổi từ VPS sang Docker Container

## 1. So sánh VM và Container

| Tiêu chí | Virtual Machine (VM) | Container (Docker) |
| :--- | :--- | :--- |
| Dung lượng Image | GB (Chứa cả OS hoàn chỉnh) | MB (Chỉ chứa ứng dụng và libs) |
| Thời gian khởi động | Phút (Boot OS) | Giây (Process start) |
| Hao phí OS | Cao (Hypervisor + Guest OS) | Thấp (Chia sẻ Kernel chủ) |
| Mức độ cô lập | Rất cao (Phần cứng riêng biệt) | Trung bình (Cô lập tầng OS) |
| Khả năng mở rộng | Chậm, tốn tài nguyên | Rất nhanh, linh hoạt |

## 2. Cơ chế cốt lõi của Linux Container

Container không phải là một máy ảo, chúng là các tiến trình được cô lập bởi Kernel Linux thông qua:
- **Namespaces**: Cung cấp lớp ảo hóa hệ thống. Ví dụ: PID Namespace giúp tiến trình thấy được các process riêng, Network Namespace cho phép card mạng ảo, và Mount Namespace quản lý file system tách biệt.
- **Control Groups (cgroups)**: Đảm bảo tài nguyên không bị lạm dụng. Cgroups giới hạn hạn mức RAM, CPU cho từng container, giúp ngăn chặn một container bị lỗi làm treo toàn bộ máy chủ.

## 3. Thông số hệ thống (docker info)

Dựa trên dữ liệu thực thi hệ thống:
- **Server Version**: 24.0.7
- **Cgroup Driver**: cgroupfs
- **Số lượng Containers**: 5 (Đang chạy: 2, Dừng: 3)
- **Số lượng Images**: 12

Kết luận: Việc chuyển đổi sang Docker giúp tối ưu hóa hiệu suất tài nguyên và tăng tốc độ triển khai CI/CD cho doanh nghiệp.