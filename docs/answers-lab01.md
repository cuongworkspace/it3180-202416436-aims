# Thảo luận Lab 01 - Git, cấu hình & Refactor

	1.Vì sao dùng git mv? 
	-Giải thích: Lệnh này di chuyển tệp và đưa thay đổi vào staging;
	Nếu sử dụng mv của OS thì cần phải thao thác git add vì khi mv file cũ git sẽ coi là deleted còn file mới sẽ có state là untracked


	2.release/lab01 có phải baseline không?
	-Giải thích: Có vì 
		+nó trỏ đến một commit SHA
		+chương trình chạy đúng
		+Thay đổi refactor đã được merger
	
	3.Vì sao không commit trực tiếp master?
	-Giải thích: Để thay đổi được review/test qua nhánh và PR, giảm nguy cơ vô tình đưa code lỗi vào baseline.

